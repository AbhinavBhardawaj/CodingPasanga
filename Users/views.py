from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomSignupForm
from django.contrib.auth import authenticate,login
#from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import get_user_model
from .forms import EditProfile
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from datetime import date
from .models import DailyActivity
from .models import  DailyDsaActivity
import requests
from .leetcode import fetch_leetcode_solved


User = get_user_model()
# Create your views here.
def login_view(request):
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                
                if user is not None:
                    login(request,user)
                    messages.success(request, "Login successful!")
                    return redirect('home')
                
                else:
                    messages.error(request,'Invalid email or password.')

            except User.DoesNotExist:
                messages.error(request,'User with this email does not exist.')

        return render(request,'Users/login.html')

def signup(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully!')
            return redirect('login')

        else:
            messages.error(request,'Please correct the below.')
    
    else:
        form = CustomSignupForm()

    return render(request,'Users/signup.html',{'form':form})

def forgotpswd(request):
    return render(request,'Users/forgotpswd.html')

def newpswd(request):
    return render(request,'Users/newpasswd.html')

def pswd_reset_done(request):
    return render(request,'Users/pswd_reset_done.html')

@login_required
def profile_view(request):
    if request.method == "POST":
        form = EditProfile(request.POST,request.FILES,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    else:
        form = EditProfile(instance=request.user)

    return render(request,'Users/profile.html',{'form':form})

@csrf_exempt
def track_time(request):
    if request.method == "POST" and request.user.is_authenticated:
        data = json.load(request.body)
        minutes = int(data.get('minutes',0))
        activity,_ = DailyActivity.objects.get_or_create(user=request.user, date=date.today())
        activity.duration_minutes += minutes
        activity.save()
        return JsonResponse({'status':'success'})


def update_dsa_activity(user, source ,new_solved):
    activity,created =  DailyDsaActivity.objects.get_or_create(user=user, date=date.today, source =source)
    problems_to_add = new_solved - activity.problems_solved
    if problems_to_add>0:
        activity.problems_solved+=problems_to_add
        activity.save()

def leetcode_update_view(request):
    if request.user.is_authenticated:
        username = request.user.leetcode_username
        new_total = fetch_leetcode_solved(username)
        update_dsa_activity(request.user, 'leetcode',new_total)
        return JsonResponse({'message':'Leetcode activity updated successfully.'})
    return JsonResponse({'error':'User not authenticated'},status = 403)

def leetcode_progress(request, username):
    url = "https://leetcode.com/graphql"
    query = """
    query userStats($username: String!) {
      allQuestionsCount {
        difficulty
        count
      }
      matchedUser(username: $username) {
        submitStats {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """
    variables = {"username": username}
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://leetcode.com",
        "Referer": f"https://leetcode.com/{username}/",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        ),
        # "Cookie": "LEETCODE_SESSION=xxxx; csrftoken=xxxx",  # if needed
    }

    r = requests.post(url, json={"query": query, "variables": variables}, headers=headers, timeout=10)
    if "application/json" not in r.headers.get("Content-Type", ""):
        return JsonResponse({"error": "Upstream returned non-JSON (blocked or challenge)."}, status=502)

    data = r.json()
    if not data.get("data") or not data["data"].get("matchedUser"):
        return JsonResponse({"error": "User not found or upstream error.", "upstream": data.get("errors")}, status=404)

    totals_list = data["data"]["allQuestionsCount"] or []
    solved_list = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"] or []

    totals = {it["difficulty"]: it["count"] for it in totals_list}
    solved = {it["difficulty"]: it["count"] for it in solved_list}

    return JsonResponse({
        "totalSolved":  solved.get("All", 0),
        "easySolved":   solved.get("Easy", 0),
        "mediumSolved": solved.get("Medium", 0),
        "hardSolved":   solved.get("Hard", 0),

        "totalQuestions": totals.get("All", 0),
        "easyTotal":      totals.get("Easy", 0),
        "mediumTotal":    totals.get("Medium", 0),
        "hardTotal":      totals.get("Hard", 0),
    })
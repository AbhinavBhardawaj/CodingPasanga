from django.db import models
import random,os
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

def get_default_pic():
    # default_img = ['pf1.png','pf2.png','pf3.png','pf4.png']
    # random_pic = random.choice(default_img)
    # print(f"Selected default profile picture: {random_pic}")
    # #return os.path.join(settings.MEDIA_URL, f"profile_pics/{random_pic}")
    # return f"profile_pics/{random_pic}"
    return f"profile_pics/{random.choice(['pf1.png', 'pf2.png', 'pf3.png', 'pf4.png'])}"

class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    profile_pic = models.ImageField(upload_to='profile_pics/',default= get_default_pic, blank=True ,null= True)
    linkedin_id = models.URLField(blank=True, null=True)
    github_id = models.URLField(blank=True,null=True)
    leetcode_username = models.CharField(max_length=100,blank=True,null=True)
    gfg_username = models.CharField(max_length=100,blank=True,null=True)

User = get_user_model()

class DailyActivity(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)
    login_time = models.DateTimeField(auto_now_add=True)
    duration_minutes = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user','date')

class DailyDsaActivity(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    source = models.CharField(max_length=50,choices=[('leetcode','LeetCode'),('gfg','GFG')])
    problems_solved = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user','date','source')
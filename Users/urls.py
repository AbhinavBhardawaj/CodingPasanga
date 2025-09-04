"""
URL configuration for CodingPasanga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup,name='signup'),
    # path('forgotpswd/',views.forgotpswd,name='forgotpswd'),
    # path('newpswd/',views.newpswd,name='newpswd'),
    # path('pswd_reset/',views.pswd_reset_done, name='pswd_reset')
    path('accounts/', include('allauth.urls')),
    path('forgotpswd/',auth_views.PasswordResetView.as_view(
        template_name='Users/forgotpswd.html'
    ), name = 'forgotpswd'),

    path('forgotpswd/done/',auth_views.PasswordResetDoneView.as_view(
        template_name = 'Users/pswd_reset_done.html'
    ), name = 'password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'Users/newpasswd.html'
    ), name = 'password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'Users/reset_done.html'
    ), name = 'password_reset_complete'),

    path('logout/',LogoutView.as_view(next_page = 'home'),name = 'logout'),

    path('profile/',views.profile_view, name = 'profile'),
    path('track-time/',views.track_time,name='track-time'),
    path("api/leetcode/<str:username>/",views.leetcode_progress,name="leetcode_progress"),

]

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import DailyActivity
from datetime import date

@receiver(user_logged_in)
def create_login_activity(sender,request,user, **kwargs):
    DailyActivity.objects.get_or_create(user=user, date=date.today())
        
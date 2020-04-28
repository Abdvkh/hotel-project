from django.shortcuts import render
from .models import Hotel,\
                    OpeningHours,\
                    Image
from django.http import Http404
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from djeym.models import Placemark

import calendar
from datetime import datetime

    # SIMPLE EXAMPLE.
    # 1. Notify administrator of a new custom marker.
    # 2. Notify user about successful moderation of his marker.
    # Mail server for testings: $ python -m smtpd -n -c DebuggingServer localhost:1025
@receiver(post_save, sender=Placemark)
def notify_email(instance, **kwargs):
    """Notify by email of a new custom marker."""

    """
    # May come in handy. (Может пригодится.)
    title = instance.header  # (html)
    description = instance.body  # (html)
    image_url = instance.user_image.url
    """
    # Notify administrator of a new custom marker.
    if instance.is_user_marker and not instance.is_sended_admin_email:
        subject = 'Text subject'
        message = 'Text message - Url: ' + \
            'http(s)://your.domain/admin/djeym/placemark/{}/change/'.format(instance.pk)
        from_email = 'admin@site.net'  # or corporate email
        recipient_list = ['admin@site.net']  # Your work email
        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)
        # Required
        instance.is_sended_admin_email = True
        instance.save()
    # Notify user about successful moderation of his marker.
    elif instance.active and instance.is_user_marker and not instance.is_sended_user_email:
        subject = 'Text subject'
        message = 'Text message'
        from_email = 'admin@site.net'  # Your work email
        recipient_list = [instance.user_email]
        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)
        # Required
        instance.is_sended_user_email = True
        instance.save()

def home(request):
    open_hours = OpeningHours.objects.all() if OpeningHours.objects.all() else {}

    # working days given in database
    opening_hours = {f"{working.weekday}": f"{str(working.from_hour)[:-3]} - {str(working.to_hour)[:-3]}" for working in open_hours}

    today = datetime.now()
    cal = calendar.TextCalendar(calendar.MONDAY)

    # creating calendar regarding working hours of hotel
    business_cal = []
    for day in cal.itermonthdays(today.year, today.month):
        weekday = calendar.weekday(today.year, today.month, day) if day != 0 else -1

        # if current weekday is equal to the weekday in database circle it
        if str(weekday + 1) in opening_hours:
            item = {'day': day, 'hours': opening_hours[str(weekday + 1)]}
        else:
            item = {'day': day, 'hours': ''}
        business_cal.append(item)

    hotel = Hotel.objects.all()
    if not hotel:
        raise Http404("No hotel details")

    images = Image.objects.all()
    if not images:
        raise Http404("No images")
    context = {'hotel': hotel[0],# the first hotel in db
               'stars': hotel[0].stars * '⭐',
               'business_cal': business_cal,
               'images': images}

    return render(request, 'home.html', context)

def about_us(request):
    context = {}
    return render(request, 'about_us.html', context)

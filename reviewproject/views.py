from django.core.mail import send_mail
from django.http import HttpResponse

def emailfunc(request):
    send_mail(
        'タイトル',
        '本文.',
        'kiyokiyotatu@gmail.com',
        ['kiyoshi536536@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('')
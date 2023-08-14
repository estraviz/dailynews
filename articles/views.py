from django.http import HttpResponse

# https://docs.djangoproject.com/en/4.2/topics/http/views/

def index(request):
    return HttpResponse('Hello, DailyNews!')

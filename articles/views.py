from django.shortcuts import render

# https://docs.djangoproject.com/en/4.2/topics/http/views/


def index(request):
    return render(request, 'articles/home.html', {'title': 'Daily News!'})

from django.shortcuts import render
from common.utils import getResults
import config

# https://docs.djangoproject.com/en/4.2/topics/http/views/

links = [
    {"name": "Home", "path": "/"},
    {"name": "Top Stories", "path": "/topstories"},
    {"name": "Most Popular", "path": "/popular"},
    {"name": "Real Time Feed", "path": "/feed"}
]


def home(request):
    apis = [
        {"name": "Top Stories API", "path": "/topstories"},
        {"name": "Most Popular API", "path": "/popular"},
        {"name": "Times Wire API", "path": "/feed"},
    ]
    return render(
        request,
        'articles/home.html',
        {'title': 'Daily News!', "apis": apis}
    )


def topstories(request):
    results = getResults(f"https://api.nytimes.com/svc/topstories/v2/arts.json?api-key={config.api_key}")
    print(results)
    return render(
        request,
        'articles/results.html',
        {
            'title': 'Daily News!',
            "subtitle": "Top Stories",
            "results": results,
            "links": links
        }
    )

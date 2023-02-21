from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from django.http import HttpResponse


data = [
    {
        "id": 1,
        "title": "Article 1",
        "body": "This is the first article"
    },
    {
        "id": 2,
        "title": "Article 2",
        "body": "This is the second article"
    }
]

def article_list(request):
    if request.method == 'GET':
        return JsonResponse(data, safe=False)

def all_articles(request):
    articles = [
        {
            'id': 1,
            'title': 'First Article',
            'body': 'This is the first article.'
        },
        {
            'id': 2,
            'title': 'Second Article',
            'body': 'This is the second article.'
        },
        {
            'id': 3,
            'title': 'Third Article',
            'body': 'This is the third article.'
        },
    ]
    return JsonResponse({'articles': articles})

def article_detail(request, article_id):
    article = {
        'id': article_id,
        'title': 'Article {}'.format(article_id),
        'body': 'This is article {}.'.format(article_id)
    }
    return JsonResponse(article)
def hello(request):
    return HttpResponse("Hello, world!")

def goodbye(request):
    return HttpResponse("Goodbye, world!")

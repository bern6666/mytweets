# tweets/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "tweets/about.html"


def index(request):
    return HttpResponse("Hello world, you are at MyTweets")


def about(request):
    return render(request, 'tweets/about.html', {})

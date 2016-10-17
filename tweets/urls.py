# tweets/urls.py
from django.conf.urls import url
from . import views
from tweets.views import AboutView, TimeView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'time/$', views.daytime, name='time'),
    url(r'dtime/$', TimeView.as_view(), name='dtime'),
    url(r'^show/$', AboutView.as_view()),
    # variable urls localhost8000/tweets/month/0 or ../month/9
    # two digits 0 to 9 are captured as positional parameter
    url(r'^month/(\d{1,2})/$', views.month, name='month'),
    url(r'^day/(\d)/$', views.day, name='day'),
    url(r'^image/$', views.image, name='image'),
    url(r'^pil/$', views.pil_image, name='pil_image'),
    url(r'^graphics/$', views.graphics, name='graphics'),
    ]

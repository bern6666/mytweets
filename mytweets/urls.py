# mytweets/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^tweets/', include('tweets.urls')),
    url(r'^admin/', admin.site.urls),
]

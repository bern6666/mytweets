# mytweets/urls.py
from django.conf.urls import url, include
from django.contrib import admin
# from tweets.views import TimeView
from tweets.views import daytime

urlpatterns = [
    # url(r'^$', TimeView.as_view()),
    url(r'^$', daytime),
    url(r'^tweets/', include('tweets.urls')),
    url(r'^admin/', admin.site.urls),
]

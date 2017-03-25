from django.conf.urls import url
import app.views as app

urlpatterns = [
    url(r'^$', app.index),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post-message$', views.post_message),
    url(r'^post-comment$', views.post_comment),
]

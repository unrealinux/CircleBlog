from django.conf.urls import url

from . import views
from django.conf.urls.i18n import urlpatterns

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
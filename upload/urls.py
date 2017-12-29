from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Instructions page
    url(r'^instructions/$', views.instructions, name='instructions'),
]

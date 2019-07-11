from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.LoadView.as_view(), name='load'),
]

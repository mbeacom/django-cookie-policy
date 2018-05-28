from django.conf.urls import re_path

from . import views

app_name = 'cookie_policy'
urlpatterns = [
    re_path(r'^policy/?', views.policy_view, name='cookie_policy'),
    re_path(r'^accept-cookie-policy/?', views.accept_cookie_policy, name='accept_cookie_policy'),
]

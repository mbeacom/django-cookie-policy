#-*- coding: utf-8 -*-
import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render


def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT"
    )
    response.set_cookie(key, value, max_age=max_age, expires=expires)


# Cookie Law Decorator
def cookie_law_decorator(function):
    def wrap(request, *args, **kwargs):
        if request.GET.get('cookie_accepted', None):
            return function(request, *args, **kwargs)
        elif request.COOKIES.get('cookielaw', False):
            return function(request, *args, **kwargs)
        return HttpResponseRedirect('/en/european-cookie-law')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def accept_cookie_policy(request):
    if 'HTTP_REFERER' in request.META:
        response = HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        response = HttpResponseRedirect('/')
    set_cookie(response, 'cookie_accepted', 1, days_expire=365)
    return response


def policy_view(request):
    return render(request, 'cookie_policy/policy.html', {})

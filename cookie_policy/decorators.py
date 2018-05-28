#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def cookie_policy(function):
    """
    This decorator can be used to redirect the visitor to the cookie policy page
    when it has not been accepted
    """

    def wrap(request, *args, **kwargs):
        if request.COOKIES.get('cookie_accepted', False):
            return function(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('cookie_policy'))

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

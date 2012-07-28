from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import resolve

def home(request):
    ctx = {
    }
    return render_to_response("home.html", ctx, RequestContext(request))

def test(request):
    s="/2012/07/udvozlo/"
    s="/tortenetek/szultan-kutya/"
    import simplejson
    func, args, kwargs = resolve(s)
    print func, args, kwargs
    pass
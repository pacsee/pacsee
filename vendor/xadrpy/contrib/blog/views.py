from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import Http404
import logging
from django.utils.safestring import mark_safe
from xadrpy.contrib.blog.models import Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import resolve
logger = logging.getLogger("blog.views")

def column(request, route, page=1, **kwargs):
    ctx = route.get_context(request, kwargs={'page':page})
    route.increment_view_count(request)
    return render_to_response(request.theme.template().column, ctx, RequestContext(request))

def categories(request, slug, route=None, page=1, **kwargs):
    category = get_object_or_404(Category, slug=slug)
    paginator = Paginator(category.get_entries(), 5)
    try:    
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages) 
    ctx = {
        'category': category,
        'entries': entries,
        'paginator': paginator,
        'stub': category.get_absolute_url()
    }
    return render_to_response("xadrpy/blog/categories.html", ctx, RequestContext(request))

def tag(request, route, **kwargs):
    pass

def posts(request, route, title, **kwargs):        
    posts = route.get_entries(**kwargs)
    ctx = {
        'column': route,
        'title': title % kwargs,
        'posts': posts,
    }
    return render_to_response("post_list.html", ctx, RequestContext(request))

def entry(request, route, **kwargs):
    entry = route.get_entry(**kwargs)
    entry.permit(request)
    ctx = dict(route.get_context(request),
               **entry.get_context(request))
    entry.increment_view_count(request)
    return render_to_response("xadrpy/blog/entry.html", ctx, RequestContext(request))

    
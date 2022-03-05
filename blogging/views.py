# blogging/views.py

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class StubView(View):
    def get(self, request, *args, **kwargs):
        body = "Stub View\n\n"
        if args:
            body += "Args:\n"
            body += "\n".join(["\t%s" % a for a in args])
        if kwargs:
            body += "Kwargs:\n"
            body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
        return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'


class PostDetailView(DetailView):
    #model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    #queryset = Post.objects.filter(published_date__exact!=Null)
    template_name = 'blogging/detail.html'
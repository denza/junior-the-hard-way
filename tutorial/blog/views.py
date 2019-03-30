from django.shortcuts import render
from .models import Blog
from django.views import View

class IndexView(View):
    def get(self, request):
        context = { 'all_blogs' : Blog.objects.all}
        return render(request, 'index.html', context )

class DetailView(View):
    def get(self,request,**kwargs):
        blog_id = kwargs.get('pk')
        context = {'blog' :  Blog.objects.get(id = blog_id)}
        return render(request, 'detail.html', context)

       

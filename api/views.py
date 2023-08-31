from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'api/home.html', context)

class BlogListView(ListView):
    model = Blog
    template_name = 'api/home.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    
class BlogDetailView(DetailView):
    model = Blog
    

class BlogCreatelView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user, self.request.FILES
        return super().form_valid(form)

# def blog_detail(request, pk):
#     blog = Blog.objects.get(id=pk)
#     context = {
#         'blog':blog
#     }
#     return render(request, 'api/detail.html', context)
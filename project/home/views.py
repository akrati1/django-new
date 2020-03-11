from django.shortcuts import render
from django.views.generic import ListView
from user.models import Post


# Create your views here.
def home(request):
    context1 = {'post': Post.objects.all()}
    return render(request, 'home_page.html',context1)


class PostListView(ListView):
    model = Post
    template_name = 'home_page.html'
    context_object_name = 'post'

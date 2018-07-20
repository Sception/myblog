from django.shortcuts import render
from blog.models import BlogsPost

# Create your views here.
def blog_index(request):
    # 获取所有数据
    blog_list = BlogsPost.objects.all()
    # 返回index.html页面
    return render(request, 'index.html', {'blog_list': blog_list})
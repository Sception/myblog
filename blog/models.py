from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    # 博客标题
    title = models.CharField(max_length = 150)
    # 博客正文
    body  = models.TextField()
    # 创建时间
    timestamp = models.DateTimeField()



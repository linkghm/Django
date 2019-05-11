from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogArticles(models.Model):
    # 字段title属性charfield
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    # 规定blog article的显示顺序
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

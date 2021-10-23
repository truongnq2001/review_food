from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    slug = models.SlugField
    image = models.CharField(max_length=255, verbose_name="image")
    address = models.CharField(max_length=255, verbose_name="address")
    price = models.IntegerField(blank=False, default=0, verbose_name="price")
    excerpt = models.CharField(max_length=500, verbose_name="excerpt")
    content = models.TextField(verbose_name="content")
    score = models.IntegerField(blank=True, default=0, verbose_name="score")
    is_active = models.BooleanField(default=True, verbose_name="is_active")
    post_date = models.DateTimeField(auto_now_add=True, verbose_name="post date")
    modified = models.DateTimeField(null=True, verbose_name="modified")
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
        verbose_name="posted by", on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
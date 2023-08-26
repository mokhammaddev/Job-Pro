from django.db import models
from django.db.models.signals import post_save

from account.models import Account
from ckeditor.fields import RichTextField

from config import settings


class TagBlog(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = RichTextField()
    image = models.ImageField(upload_to='blog/')
    tags = models.ManyToManyField(TagBlog)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SubContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='content/')
    description = RichTextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=221, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(max_length=221, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if self.author:
            return f"comment of {self.author} ({self.id})"
        return f"comment of {self.name} ({self.id})"

    @property
    def get_related_comments(self):
        qs = Comment.objects.filter(top_level_comment_id=self.id).exclude(id=self.id)
        if qs:
            return qs
        return None


def comment_post_save(instance, sender, created, *args, **kwargs):
    if created:
        top_level_comment = instance
        while top_level_comment.parent_comment:
            top_level_comment = top_level_comment.parent_comment
        instance.top_level_comment_id = top_level_comment.id
        instance.save()


post_save.connect(comment_post_save, sender=Comment)


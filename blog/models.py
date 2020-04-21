from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime


class Post (models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} posted on the {1}'.format(self.title, self.date_posted.strftime('%B %d %y'))

    def get_absolute_url(self):
        return reverse('blog:blog_list')


class Comment(models.Model):
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return '{0} on {1}'.format(self.author, self.post)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.post.pk})

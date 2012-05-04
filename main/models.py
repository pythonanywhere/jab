from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    published = models.DateTimeField()

    author = models.ForeignKey(User, null=True)

    title = models.CharField(max_length=1024)

    contents = models.TextField()


    @models.permalink
    def get_absolute_url(self):
        return ('view_post', [str(self.id)])

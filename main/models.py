from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    publication_date = models.DateTimeField()

    author = models.ForeignKey(User, null=True)

    title = models.CharField(max_length=1024)

    contents = models.TextField()

    link_from_header = models.BooleanField(default=False)

    show_in_list_and_rss = models.BooleanField(default=True)


    @models.permalink
    def get_absolute_url(self):
        return ('view_post', [str(self.id)])

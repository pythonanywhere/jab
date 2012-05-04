from django.contrib.auth.models import User
from django.db import models


class STATUSES(object):
    DRAFT = 0
    PUBLISHED = 1

    NAMES = {
        DRAFT : 'Draft',
        PUBLISHED : 'Published',
    }


class Post(models.Model):

    status = models.IntegerField(choices=STATUSES.NAMES.items(), default=STATUSES.DRAFT)

    publication_date = models.DateTimeField()

    author = models.ForeignKey(User, null=True)

    title = models.CharField(max_length=1024)

    contents = models.TextField()

    link_from_header = models.BooleanField(default=False)

    show_in_list_and_rss = models.BooleanField(default=True)


    @models.permalink
    def get_absolute_url(self):
        return ('view_post', [str(self.id)])


Post.PUBLISHED_POSTS = Post.objects.filter(status=STATUSES.PUBLISHED).order_by("-publication_date")

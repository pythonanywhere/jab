from django.db import models

class Post(models.Model):

    posted = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=1024)

    contents = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('view_post', [str(self.id)])
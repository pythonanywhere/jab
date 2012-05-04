from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed 

from jab.main.models import Post


# Keep Chrome happy as per http://stackoverflow.com/a/1081023/32846 -- thanks to
# David and Everyblock 
class CorrectMimeTypeFeed(Rss201rev2Feed):
    mime_type = 'application/xml'


class LatestEntriesFeed(Feed):
    feed_type = CorrectMimeTypeFeed
    
    title = settings.BLOG_NAME
    link = "/"
    description = settings.BLOG_DESCRIPTION
    
    description_template = 'feed_description.html'

    def items(self):
        return Post.objects.order_by('-published')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.contents
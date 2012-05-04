from django.conf.urls.defaults import patterns, include, url
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import create_object
from django.views.generic.list_detail import object_detail

from jab.main.feeds import LatestEntriesFeed
from jab.main.models import Post


urlpatterns = patterns("",
    url(
        r"^$",
        direct_to_template,
        {
            "template": "main_page.html",
            "extra_context": {
                "posts": lambda: Post.PUBLISHED_POSTS.filter(show_in_list_and_rss=True),
            }
        },
        name="main_page"
    ),
    url(
        r'^(?P<object_id>\d+)/$',
        object_detail,
        {
            "queryset": Post.objects.all(),
            "template_name": "post.html",
            "template_object_name": "post"
        },
        name="view_post"
    ),
    url(
        r'^feed/$',
        LatestEntriesFeed(),
        name="feed"
    ),
)

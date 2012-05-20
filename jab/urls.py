from django.conf.urls.defaults import patterns, include, url
from django.core.urlresolvers import reverse
from django.views.generic.create_update import create_object
from django.views.generic.list_detail import object_detail, object_list

from blog.jab.feeds import LatestEntriesFeed
from blog.jab.models import Post


urlpatterns = patterns("",
    url(
        r"^$",
        object_list,
        {
            "queryset": Post.published_posts().filter(show_in_list_and_rss=True),
            "template_name": "main_page.html",
            "template_object_name": "post",
            "paginate_by": 10,
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

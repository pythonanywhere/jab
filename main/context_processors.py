from django.conf import settings

def add_blog_settings(context):
    return {
        'blog_name': settings.BLOG_NAME,
    }
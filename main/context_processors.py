from django.conf import settings

def add_blog_settings(context):
    return {
        'blog_name': getattr(settings, "BLOG_NAME", ""),
        'blog_description': getattr(settings, "BLOG_DESCRIPTION", ""),
        'blog_author': getattr(settings, "BLOG_AUTHOR", ""),
        'blog_author_email': getattr(settings, "BLOG_AUTHOR_EMAIL", ""),
        'blog_author_twitter': getattr(settings, "BLOG_AUTHOR_TWITTER", ""),
    }
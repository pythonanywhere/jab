DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

BLOG_NAME = "JAB default blog"
BLOG_DESCRIPTION = "Just another JAB blog"
BLOG_AUTHOR = "Joe Blogs"
BLOG_AUTHOR_EMAIL = "someone@example.com"   # Make blank if you don't want it
BLOG_AUTHOR_TWITTER = "a_twitter_id"        # Make blank if you don't want it

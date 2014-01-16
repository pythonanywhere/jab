Just Another (Django) Blog
==========================

Yes, it's another Django blog.  Not a blogging framework, though -- just a blog.
No bells or whistles.  Designed to just get up and running with a basic blog as
quickly as possible.  No comments, no categories, no tagging.  Themes are all
template-based.

Getting started
---------------

* You'll need Django installed, and some way of hosting it -- the default
  runserver, Apache with mod_wsgi, or (of course) a
  [PythonAnywhere](http://www.pythonanywhere.com) account.
* You'll also need the
  [South Django migrations package](http://south.aeracode.org/): if you're on
  PythonAnywhere, you'll have it already. If not, `pip install south`.
* `git checkout git://github.com/resolversystems/jab.git`
* `cd jab`
* `cp local_settings_template.py local_settings.py`
* Edit `local_settings.py`, and change the variables in there to point to an
  appropriate database etc.  The Twitter and email fields are optional, just
  miss them out if you don't want to use them.
* `python manage.py syncdb`
* `python manage.py migrate`

...and you're done!  Log in to the admin GUI using the admin username you
created during the syncdb, and add `Post` objects to post; set the status to
"Published" when you want a post to go live.  Posts `contents` are written
in [Markdown](http://daringfireball.net/projects/markdown/syntax).  It's worth
noting that you can just put any HTML in there too -- it'll get passed straight
through.  So, for example, YouTube embed code will work just fine unchanged.

If you want to add something to the header (like, say, an "About" page) then set
the "Link from header" checkbox to true -- and you might want to also set the
"Show in list and rss" checkbox to false.

If you want something to appear in a sidebar (the default template puts it on
the right) then just add a `SidebarItem` object; its `contents` field is also
written in Markdown.

A neat hack -- if you use Google Analytics and want to put the code in your
blog, you can just create a new `SidebarItem` with the embed code in it -- it
will work!

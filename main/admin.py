from django.contrib import admin
from jab.main.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('publication_date', 'title', 'status',)

    ordering = ('-publication_date',)


admin.site.register(Post, PostAdmin)

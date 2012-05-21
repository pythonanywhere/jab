from django.contrib import admin
from jab.models import Post, SidebarItem


class PostAdmin(admin.ModelAdmin):
    list_display = ('publication_date', 'title', 'status',)

    ordering = ('-publication_date',)

admin.site.register(Post, PostAdmin)


class SidebarItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(SidebarItem, SidebarItemAdmin)

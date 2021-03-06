from django.contrib import admin
from btds.models import *

class NameOnlyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class NameLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ['name']

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso')
    search_fields = ['name']

class NovelAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'illustrator')
    search_fields = ['name', 'author__name', 'illustrator__name']

class VolumeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'novel', 'year', 'isbn')
    search_fields = ['name', 'novel__name', 'isbn']
    list_filter = ('novel', 'year')

class LinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'file_format', 'visible', 'protected', 'closed')
    search_fields = ['link', 'user__username']
    list_filter = ('visible', 'protected', 'closed')

class MetaAdmin(admin.ModelAdmin):
    list_display = ('bt_title', 'uuid')
    search_fields = ['bt_title', 'editor__name', 'translator__name']
    list_filter = ('genre__name', 'modified')

admin.site.register(Author, NameOnlyAdmin)
admin.site.register(Illustrator, NameOnlyAdmin)
admin.site.register(Translator, NameLinkAdmin)
admin.site.register(Editor, NameLinkAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Publisher, NameLinkAdmin)
admin.site.register(Genre, NameOnlyAdmin)
admin.site.register(Novel, NovelAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Meta, MetaAdmin)
admin.site.register(Image)

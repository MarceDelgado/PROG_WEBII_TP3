from django.contrib import admin
from .models import Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fechaDepublicacion', 'autor')
    search_fields = ('titulo',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date')
    search_fields = ('content',)

    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
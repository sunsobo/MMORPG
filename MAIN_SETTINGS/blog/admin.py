from django.contrib import admin


from .models import PostCategory, Post, PostReply

# BEGIN PostCategory
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'create',
        'update',
        'id',
    ]
    
    prepopulated_fields = {
        'slug': ('title',)
    }
admin.site.register(PostCategory, PostCategoryAdmin)
# END PostCategory


# BEGIN Post
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'user',
        'create',
        'update',
        'id',
    ]
    
    list_filter = [
        'category',
    ]

admin.site.register(Post, PostAdmin)
# END Post


# BEGIN PostReply
class PostReplyAdmin(admin.ModelAdmin):
    list_display = [
        'post',
        'user',
        'text',
        'create',
        'update',
        'id',
    ]

admin.site.register(PostReply, PostReplyAdmin)
# END PostReply
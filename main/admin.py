from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "truncated_content", "status", )
    fields = ("title", "content", "image", "status", )
    search_fields = ("title", "content", )
    list_filter = ("status", )

    def truncated_content(self, obj):
        # Adjust the length as needed
        max_length = 80
        return (obj.content[:max_length] + '...') if len(obj.content) > max_length else obj.content

    truncated_content.short_description = 'Content'

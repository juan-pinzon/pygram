"""Posts admin Clasess"""

from django.contrib import admin
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """Posts Admin"""
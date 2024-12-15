from django.contrib import admin
# from .models import Voetbalspelers
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'created_date','published_date')
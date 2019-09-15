from django.contrib import admin
from . import models

class TweetTagAdmin(admin.ModelAdmin):
    list_display = ('tweet_id', 'tweet_text', 'tweet_user_name', 'tag_list', 'updated_at')
    ordering = ['-updated_at']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())
    
    def tweet_id(self, obj):
        return obj.tweet.id

    def tweet_text(self, obj):
        return obj.tweet.text

    def tweet_user_name(self, obj):
        return obj.tweet.user_name

admin.site.register(models.TweetTag, TweetTagAdmin)

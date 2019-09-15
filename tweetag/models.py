from django.db import models
from tweet.models import Tweet
from taggit.managers import TaggableManager

class TweetTag(models.Model):
    tweet = models.OneToOneField(Tweet, primary_key=True)
    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
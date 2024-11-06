# admin.py
from django.contrib import admin
from .models import Profile, Post, Comment, Subscription, Notification


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'bio')
    list_filter = ('followers',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('post__title', 'author__username', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notif_type', 'from_user', 'post', 'created_at', 'is_read')
    search_fields = ('user__username', 'from_user__username', 'notif_type')
    list_filter = ('notif_type', 'is_read', 'created_at')
    ordering = ('-created_at',)

#from django.contrib import admin

# Register your models here.

# conversations/admin.py
from django.contrib import admin
from .models import Conversation

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')  # Display title and summary
    search_fields = ('title', 'content')

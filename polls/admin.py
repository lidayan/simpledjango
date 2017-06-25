# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    fieldsets = [
        ('board1', {'fields': ['question_text']}),
        ('board2', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
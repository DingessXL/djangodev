# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_name', 'subcategory', ]
    list_filter = ['category_name']


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'answer_text', 'question_category', ]

    search_fields = ['question_text', 'question_category', ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)

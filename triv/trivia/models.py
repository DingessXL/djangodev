# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    answer_text = models.CharField(max_length=255)
    question_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    class Meta:
        unique_together = ["question_text", "answer_text", "question_category"]

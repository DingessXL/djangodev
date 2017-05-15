# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import modelformset_factory, forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .models import Question, Category
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm, CategoryForm


# Create your views here.
class CreateQuestionView(CreateView):
    model = Question
    template_name = 'trivia/manage.html'
    form_class = QuestionForm


class UpdateQuestionView(UpdateView):
    model = Question
    template_name = 'trivia/edit.html'
    form_class = QuestionForm


class CreateCategoryView(CreateView):
    model = Category
    template_name = 'trivia/new_cat.html'
    form_class = CategoryForm


def last_ten_questions(request):
    questions = Question.objects.all()  # .order_by('-id')[:10][::-1]
    return render(request, 'trivia/base.html', {'questions': questions})

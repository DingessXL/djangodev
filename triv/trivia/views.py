# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import modelformset_factory, forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .models import Question, Category
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm, CategoryForm


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list, }
    return HttpResponse(template.render(context, request))


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
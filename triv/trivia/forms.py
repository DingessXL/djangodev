from django.forms import ModelForm
from .models import Question, Category
from django.core.exceptions import ValidationError
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

form = QuestionForm()


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

cat_form = CategoryForm()

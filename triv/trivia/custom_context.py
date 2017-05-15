from .models import *


def last_ten(request):
    last_10_list = Question.objects.all()
    return {'last_10_list': last_10_list}

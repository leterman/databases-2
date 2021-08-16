from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'

    students_list = Student.objects.all() \
        .order_by(ordering) \
        .prefetch_related('teacher')

    context = {'students_list': students_list}

    return render(request, template, context)

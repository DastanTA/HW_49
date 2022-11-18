from django.shortcuts import render, get_object_or_404
from task_tracker.models import Task
from django.views.generic import View, TemplateView


class MainPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        print(context)
        return context

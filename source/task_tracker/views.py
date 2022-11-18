from django.shortcuts import render, get_object_or_404, redirect
from task_tracker.models import Task
from django.views.generic import View, TemplateView
from task_tracker.forms import TaskForm


class MainPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        print(context)
        return context


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class CreateTask(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        context = {'form': form}
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            Task.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status'),
                type=form.cleaned_data.get('type')
            )
            return redirect('main')
        else:
            return render(request, 'create.html', {'form': form})

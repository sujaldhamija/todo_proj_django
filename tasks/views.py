from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy


# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    ordering = ['is_done', '-id']
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(title__icontains=q)
        return qs



class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'is_done']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'is_done']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')


class TaskDelete(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:list')

@require_POST
def toggle_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('tasks:list')

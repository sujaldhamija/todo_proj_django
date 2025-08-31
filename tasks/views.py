from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy


# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    ordering = ['is_done', '-id']
    paginate_by = 2

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'is_done']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # 👈 assign current user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'is_done']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


@require_POST
def toggle_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_done = not task.is_done
    task.save()
    return redirect('tasks:list')

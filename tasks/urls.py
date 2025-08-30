from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path("", views.TaskList.as_view(), name='list'),
    path("new/", views.TaskCreate.as_view(), name='create'),
    path("<int:pk>/edit/", views.TaskUpdate.as_view(), name='update'),
    path("<int:pk>/delete/", views.TaskDelete.as_view(), name='delete'),
    path("<int:pk>/toggle/", views.toggle_done, name='toggle'),
]

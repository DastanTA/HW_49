from django.contrib import admin
from django.urls import path
from task_tracker.views import MainPage, TaskView, CreateTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main'),
    path('task/<int:pk>', TaskView.as_view(), name='view_task'),
    path('add/', CreateTask.as_view(), name='add_task'),
]

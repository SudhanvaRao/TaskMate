from todolist_app import views
from django.urls import path,include

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>', views.edit, name='edit'),
    path('done/<id>', views.done, name='done'),
    path('not_done/<id>', views.not_done, name='not_done'),
]

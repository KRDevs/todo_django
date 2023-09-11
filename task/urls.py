from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('<int:pk>/list_table/', views.list_table, name='list_table'),
    path('lists/', views.lists, name='lists'),
    path('new_task/', views.new_task, name='new_task'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit_task, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]

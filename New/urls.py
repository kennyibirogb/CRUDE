from django.urls import path
from . import views

urlpatterns = [
  path('edit/<int:post_id>/', views.form_create_or_edit, name='form_edit'),
  path('', views.form_create_or_edit, name = 'form_create'),
  path('delete/<int:post_id>/', views.form_delete, name='form_delete'),
  
]

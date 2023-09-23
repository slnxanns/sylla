from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('create/', views.create_document, name='create_document'),
    path('edit/<int:pk>/', views.edit_document, name='edit_document'),
    path('delete/<int:pk>/', views.delete_document, name='delete_document'),
]

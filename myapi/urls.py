
from django.urls import path
from myapi import views

urlpatterns = [
    path('all/', views.all_entries, name='all_entries'),
    path('one/<int:pk>/', views.one_entry, name='one_entry'),
    path('delete/<int:pk>/', views.delete_entry, name='delete_entry'),
    path('update/<int:pk>/', views.update_entry, name='update_entry'),
    path('create/', views.create_entry, name='create_entry'),

]

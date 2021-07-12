from typing import Pattern
from django.urls import path
from . import views
from django.conf import settings


from .views import GeneratePdf

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('client/', views.client, name='dashboard-client'),
    path('client/detail/<int:pk>/', views.client_detail, name='dashboard-client-detail'),
    path('inward/', views.inward, name='dashboard-inward'),
    path('inward/delete/<int:pk>/', views.inward_delete, name='dashboard-inward-delete'),
    path('inward/update/<int:pk>/', views.inward_update, name='dashboard-inward-update'),
    path('dispatch/', views.dispatch, name='dashboard-dispatch'),

    
    path('dispatch/pdf/', GeneratePdf.as_view()), 
    
]

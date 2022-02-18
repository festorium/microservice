from django.urls import path
from . import views

urlpatterns = [
    path('customer-list/', views.ShowAll, name='customer-list'),
    path('customer-detail/<int:pk>/', views.ViewCustomer, name='customer-detail'),
    path('customer-create/', views.CreateCustomer, name='customer-create'),
    path('customer-update/<int:pk>/', views.updateCustomer, name='customer-update'),
    path('customer-delete/<int:pk>/', views.deleteCustomer, name='customer-delete'),

]
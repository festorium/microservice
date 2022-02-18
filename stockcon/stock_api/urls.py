from django.urls import path
from . import views

urlpatterns = [
    path('item-list/', views.ShowAllItem, name='item-list'),
    path('item-create/', views.CreateItem, name='item-create'),
    path('item-update/<str:pk>/', views.updateItem, name='item-update'),
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/', views.updateOrder, name='update_order'),
    path('delete_order/', views.deleteOrder, name='delete_order'),
]


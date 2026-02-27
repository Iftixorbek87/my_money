from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_transaction_view, name='add_transaction'),
    path('list/', views.transaction_list_view, name='transaction_list'),
    path('delete/<int:pk>/', views.delete_transaction_view, name='delete_transaction'),
    path('statistics/', views.statistics_view, name='statistics'),
]

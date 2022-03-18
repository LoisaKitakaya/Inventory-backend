from django.urls import path
from api import views

urlpatterns = [
    path('items/', views.InventoryList.as_view()),
    path('items/<int:pk>/', views.InventoryListDetail.as_view()),
]
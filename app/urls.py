from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('store/add-item/', views.add_item, name='add_item'),
    path('store/<slug:slug>/', views.store_item, name='store_item'),
    path('store/edit-item/<slug:slug>/', views.edit_item, name='edit_item'),
    path('store/delete-item/<int:id>/', views.delete_item, name='delete_item'),
]
from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('items/', views.inventory_list),
    path('items/<int:pk>/', views.inventory_item_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
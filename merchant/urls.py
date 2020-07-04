from django.urls import path
from . import views

app_name = 'merchant'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('order/', views.OrderView.as_view(), name='order-summary'),
    path('order2/', views.OrderView.as_view(), name='order-confirm'),
    path('confirm-order/<slug>/', views.confirm_order, name='confirm-order'),
    path('remove-order/<slug>/', views.remove_order, name='remove-order'),
    path('order-detail/<slug>', views.OrderDetailView.as_view(), name='order-detail'),
]
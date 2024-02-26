from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('success/', CheckoutSuccessView.as_view(), name='success'),
    path('failed/', views.CheckoutFailedView.as_view(), name='failed_payment'),
]
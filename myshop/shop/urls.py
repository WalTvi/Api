from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CartItemViewSet, SaleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'cart_items', CartItemViewSet, basename='cartitem')
router.register(r'sales', SaleViewSet, basename='sale')

urlpatterns = [
    path('', include(router.urls)),
]


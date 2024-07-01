from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.views import UserViewSet, CartItemViewSet, SaleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cart_items', CartItemViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),
]

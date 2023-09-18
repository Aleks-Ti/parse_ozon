from django.urls import include, path
from rest_framework import routers
from api.views import ProductView

router = routers.DefaultRouter()
router.register('products', ProductView, basename='product')

urlpatterns = [
    path('v1/', include(router.urls)),
]

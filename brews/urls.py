from django.urls import path, include
# from .views import BrewList, BrewDetail
from rest_framework.routers import DefaultRouter
from .views import BrewViewSet

router = DefaultRouter()
router.register(r'', BrewViewSet, basename='brew')

urlpatterns = [
  path('', include(router.urls)),
]
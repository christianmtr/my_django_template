from django.urls import path, include
from rest_framework.routers import SimpleRouter

from core.api import viewsets as core_viewsets

router = SimpleRouter()
router.register('users', core_viewsets.UserViewSets, basename='users')
router.register('organizations', core_viewsets.OrganizationViewSets, basename='organizations')

urlpatterns = [
    path('', include(router.urls))
]

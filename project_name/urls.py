"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, authentication
from rest_framework_simplejwt import authentication as jwt_authentication
from rest_framework_simplejwt.views import TokenRefreshView

from core.api.viewsets import MyTokenObtainPairView

schema_view = get_schema_view(
    openapi.Info(
        title="{{ project_name }} API reference",
        default_version='v1',
        description="{{ project_name }}",
        terms_of_service="f",
        contact=openapi.Contact(email="development@{{ project_name }}.com"),
        license=openapi.License(name="{{ project_name }} 2020. All rights reserved."),
    ),
    public=False,
    authentication_classes=(authentication.SessionAuthentication, jwt_authentication.JWTAuthentication,),
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('core/', include('core.urls')),
        # include here others app's `urls.py` files
    ])),
    re_path(r'^api/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'rest_framework.exceptions.server_error'

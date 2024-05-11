"""
URL configuration for transpone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from transpone_coursework.views import MatrixViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('matrices/transpose', MatrixViewSet.as_view({'get': 'get_matrix_list', 'post': 'post_transpose_matrix'}),
         name='matrix_transpose'),
    path('matrices/transpose/redact', MatrixViewSet.as_view({'get': 'get_transpose_matrix', 'post': 'post_delete_matrix'}), name='matrix_change'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

"""
URL configuration for drfTest_swh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import PostViewSet

from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from sports.views import SportsViewSet

# 자동으로 rest api crud 제공 해주는 라우터
router = DefaultRouter()
router.register(r"posts", PostViewSet)   # /api/posts/
router.register(r"sports", SportsViewSet)  # /api/sports/

# Swagger 설정
schema_view = get_schema_view(
    openapi.Info(
        title="Django API 문서",
        default_version="v1",
        description="Django REST Framework를 사용한 API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL 패턴 정의
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),  # 🔥 API 엔드포인트 한 번만 포함!

    # ✅ Swagger UI (웹 브라우저용)
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

    # ✅ ReDoc (대체 UI)
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # ✅ API 명세 (JSON / YAML)
    re_path(r"^swagger\.(json|yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]


"""profiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    HelloApiView, HelloViewSet, UserFeedViewSet, UserLoginApiView,
    UserProfileViewSet,
)

router = DefaultRouter()
router.register("HelloViewSet", HelloViewSet, "test")
router.register("profile", UserProfileViewSet)
router.register("feed", UserFeedViewSet)

urlpatterns = [path("api-view", HelloApiView.as_view(), name = "test_api"),
               path("login", UserLoginApiView.as_view()),
               path("view-set/", include(router.urls))]

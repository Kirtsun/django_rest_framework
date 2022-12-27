from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf import views


router = DefaultRouter()
router.register(r'post', views.PostViewSet, basename="snippet")
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'comment', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]

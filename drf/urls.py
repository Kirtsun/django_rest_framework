from django.urls import include, path

from drf import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'post', views.PostViewSet, basename="post")
router.register(r'user', views.UserViewSet, basename="user")
router.register(r'comment', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]

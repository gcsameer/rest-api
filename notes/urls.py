from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
from .views_auth import register_user
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user),
    path('token/', obtain_auth_token),   # login
]

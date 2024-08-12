from django.urls import path,include
from .views import register_user, user_login, user_logout
from rest_framework import routers
from .views import UploadViewSet
router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")


urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]



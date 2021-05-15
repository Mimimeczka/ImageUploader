from django.urls import path, include
from rest_framework import routers
from ImageUploaderApp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='User')

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:user_id>/images/', views.create_image, name='create_image'),
    path('users/<int:user_id>/images/<int:image_id>/', views.select_image, name='select_image'),
    path('users/<int:user_id>/images/<int:image_id>/<str:type>/', views.get_image, name='get_image')

]
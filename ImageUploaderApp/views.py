from .serializers import UserSerializer, ImageTypeSerializer
from rest_framework import viewsets
from .models import User, Image
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .validators import check_account_type, check_image_type
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def create_image(request, user_id):
    user = get_object_or_404(User, id=user_id)
    request_image = request.data['image']
    check_image_type(request_image.name)
    image = Image.objects.create(
            user_id=user,
            photo=request_image
        )
    return HttpResponse(f'Image added: {image.pk}')


@api_view(['GET'])
def get_image(request, user_id, image_id, type):
    user = get_object_or_404(User, id=user_id)
    image = get_object_or_404(Image, id=image_id)
    check_account_type(type, user.account_type.types)
    return HttpResponse(image.photo, content_type='image/jpg')


@api_view(['GET'])
def select_image(request, user_id, image_id):
    user = get_object_or_404(User, id=user_id)
    image = get_object_or_404(Image, id=image_id)
    serializer = ImageTypeSerializer(image)

    return Response(serializer.data)
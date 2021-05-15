from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User, Image
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def create_image(request, user_id):
    user = get_object_or_404(User, id=user_id)
    print(user)
    request_image = request.data['image']
    image = Image.objects.create(
            user_id=user,
            photo=request_image
        )
    return HttpResponse('Image added')


@api_view(['GET'])
def get_image(request, user_id, image_id, type):
    user = get_object_or_404(User, id=user_id)
    image = get_object_or_404(Image, id=image_id)
    if type == "small":
        return HttpResponse(image.photo, content_type='image/jpg', )

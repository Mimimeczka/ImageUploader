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
def image(request, user_id, ):
    user = get_object_or_404(User, id=user_id)
    print(user)
    request_image = request.data['image']
    image = Image.objects.create(
            user_id=user,
            photo=request_image
        )
    return HttpResponse('Image added')

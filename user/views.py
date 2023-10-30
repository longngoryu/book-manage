from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


from .models import User
from .serializers import UserSerializer
from .tokens import get_tokens_for_user


class UserApiView(APIView):
  def get(self, request, *args, **kwargs):
    queryset = User.objects.all()
    serializer = UserSerializer(instance=queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterApiView(APIView):
  def post(self, request, *args, **kwargs):
    data = {
       "username": request.data.get("username"),
       "password": request.data.get("password"),
       "email": request.data.get("email"),
       "image_url": request.data.get("image_url"),
       "is_staff" : request.data.get("is_staff") if "is_staff" in request.data else False,
       "is_active": request.data.get("is_active") if "is_active" in request.data else True,
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class LoginApiView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = User.objects.filter(username=username, password=password).first()

        if user is None:
            raise AuthenticationFailed("Login false!")
        
        tokens = get_tokens_for_user(user)
        return Response({"message": "success", "token": tokens}, status=status.HTTP_200_OK)
    
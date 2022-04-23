from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.generics import CreateAPIView, GenericAPIView
from django.contrib.auth import get_user_model # If used custom user model

from authorization.serializers import UserSerializer


# class CreateUserView(CreateAPIView):

#     model = get_user_model()
#     permission_classes = [
#         permissions.AllowAny # Or anon users can't register
#     ]
#     serializer_class = UserSerializer


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated, permissions.AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(CreateUserViewSet, self).get_permissions()
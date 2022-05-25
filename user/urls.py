from rest_framework import routers

from user.views import CreateUserViewSet

registration_router = routers.SimpleRouter()
registration_router.register(r"register", CreateUserViewSet, "register")
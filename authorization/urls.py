from rest_framework import routers

from authorization.views import CreateUserViewSet

registration_router = routers.SimpleRouter()
registration_router.register(r"register", CreateUserViewSet, "register")
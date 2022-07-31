from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth.hashers import make_password


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    def create(self, validated_data):
        if validated_data["password"] != validated_data["password2"]:
            raise serializers.ValidationError({"password": "Passwords must match."})

        user = UserModel.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data['password']
        )
        
        return user

    class Meta:
        model = UserModel
        fields = ("username", "email", "password", "password2")

        extra_kwargs = {
            "password": {"write_only": True},
        }
from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"]
        )

        password = validated_data["password"]
        password2 = validated_data["password2"]
        
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})

        user.set_password(validated_data["password"])
        return user

    class Meta:
        model = UserModel
        fields = ("username", "email", "password", "password2")

        extra_kwargs = {
            "password": {"write_only": True},
        }
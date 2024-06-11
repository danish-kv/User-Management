from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username","phone", "email", "password", "profile_image"]
        extra_kwargs = {"password" : {"write_only" : True}}


        def create(self, validated_data):
            password = validated_data.pop("password", None)
            user = User.objects.create_user(**validated_data)
            if password is not None:
                user.set_password(password)
            user.save()
            return  user
        
        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.profile_image = validated_data.get('profile_image', instance.profile_image)
            password = validated_data.get('password')
            if password:
                instance.set_password(password)
            instance.save()
            return instance
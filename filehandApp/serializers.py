from rest_framework import serializers
from .models import CustomUser
from rest_framework.serializers import Serializer, FileField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


from .models import fileUpload

class UploadSerializer(serializers.ModelSerializer):    
    class Meta:
        model=fileUpload
        fields = '__all__'


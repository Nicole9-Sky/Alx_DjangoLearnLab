from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ('id', 'username', 'email' 'bio', 'profile_picture')
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def create(self, validated_date):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
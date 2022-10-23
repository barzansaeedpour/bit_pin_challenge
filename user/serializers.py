from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Profile,AccessLevel,UserAccessLevel

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField()
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','password')
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password=user.password
        user.set_password(validated_data['password'])
        user.save()
        user.password=password
        # user = User.objects.create_user(**validated_data)
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('role','phone_number','birth_date')
        depth=1
        
class AccessLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLevel
        fields = "__all__"
        
class UserAccessLevelSerializer(serializers.ModelSerializer):
    access_level = AccessLevelSerializer()
    class Meta:
        model = UserAccessLevel
        fields = "__all__"
        # fields = ('user','access_level')
     
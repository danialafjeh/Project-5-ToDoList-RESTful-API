from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password','user_permissions', 'groups')
    
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'email': {
                'required': True
                }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
           **validated_data        
        )
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Task
        fields = "__all__"
        read_onlyfield = ['created_at','updated_at','is_completed']
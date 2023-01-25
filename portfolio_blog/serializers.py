from rest_framework import serializers
from .models import Post, Comments
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = '__all__'  
        read_only_fields= ['created_at', ]



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'comment', 'user', 'post')



# class CustomAuthTokenSerializer(AuthTokenSerializer):
#     def create(self, validated_data):
#         user = self.context['request'].user
#         validated_data['user_id'] = user.id
#         return super().create(validated_data)
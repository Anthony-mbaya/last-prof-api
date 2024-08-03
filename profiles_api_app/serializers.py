from rest_framework import serializers
from profiles_api_app import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=5)
    age = serializers.IntegerField(min_value=18)
    
class StudMarksSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    marks = serializers.IntegerField(min_value=0, max_value=100)
    
#use metaclass to point to specific in model - ModelSerializer
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        #point to our model
        model = models.UserProfile
        #list of fields to manage using our serializer
        fields = ('id', 'email', 'name', 'password')
        #extra args to specify how to handle password
        extra_kwargs = {
            'password' : {
                'write_only' : True, #only allow write operation on password
                'style' : {'input_type' : 'password'} #hide password input in form
            }
        }
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
        
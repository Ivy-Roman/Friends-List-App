from django.contrib.auth import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializers):
    password = serializers.CharField(
        max_length=65, min_length=8,write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=4)
    last_name = serializers.CharField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields=['username', 'firstname', 'lastname', 'email']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['emails']).exists():
            raise serializers.ValidationError(
                {'email', ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(validated_data)
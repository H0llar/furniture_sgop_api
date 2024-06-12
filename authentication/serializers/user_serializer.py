from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True, 'required': True},
            'username': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(username=validated_data['username'],
                                             first_name=validated_data['first_name'],
                                             last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_password(self, value):
        validate_password(value)
        return value

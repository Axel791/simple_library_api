from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UsersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(read_only=True, source="user.email")
    user_status = serializers.CharField(read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'user_status',
            'address',
            'last_action',
            'created_at'
        )

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        for k, v in user_data.items():
            setattr(user, k, v)
        instance.address = validated_data.get("address", instance.address)
        user.save()
        instance.save()
        return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    password1 = serializers.CharField(max_length=30)
    password2 = serializers.CharField(max_length=30)
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'address',
        )

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_data["password"] = make_password(validated_data.get("password1"))
        user = User.objects.create(**user_data)
        user.save()
        user_profile = UserProfile.objects.create(
            user=user,
            address=validated_data.get("address")
        )
        user_profile.save()
        return user_profile

    def validate_username(self, value):
        user = User.objects.filter(username=value).first()
        if user is not None:
            raise serializers.ValidationError("This username is used.")
        return value

    def validate_email(self, value):
        user = User.objects.filter(email=value).first()
        if user is not None:
            raise serializers.ValidationError("This email is used.")
        return value

    def validate(self, data):
        password1 = data.get("password1")
        password2 = data.get("password2")
        if password1 != password2:
            raise serializers.ValidationError("Password mismatch.")
        return data



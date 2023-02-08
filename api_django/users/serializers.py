from rest_framework import serializers
from users.models import UserProfile


class UsersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(read_only=True, source="user.email")
    phone_number = serializers.CharField(read_only=True)
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
            'phone_number',
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


class UserRegistrationSerializer(serializers.Serializer):
    pass


class UserLoginSerializer(serializers.Serializer):
    pass





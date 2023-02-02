from rest_framework import serializers
from users.models import UserProfile


class UsersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(read_only=True, source="user.email")
    phone_number = serializers.CharField(read_only=True)

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
        instance.fist_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.user_status = validated_data.get("user_status", instance.user_status)
        instance.address = validated_data.get("address", instance.address)
        instance.save()
        return instance



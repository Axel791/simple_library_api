from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from users.serializers import UsersSerializer
from utils.responses import SuccessResponse, ErrorResponse
from django.shortcuts import get_object_or_404

from users.models import UserProfile

from utils.base_permissions import IsOwnerOrReadOnly
from utils import errors


class UserProfileView(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UsersSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserProfile.objects.all()

    def get_object(self):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(UserProfile, id=pk)
        self.check_object_permissions(self.request, user)
        return user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        return SuccessResponse(
            data=UsersSerializer(user).data,
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UsersSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessResponse(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return SuccessResponse(
            data="User deleted.",
            status=status.HTTP_200_OK
        )


class UsersListView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()

    @action(detail=False, methods=['GET'], url_path=r'by_status/(?P<status>\w+)')
    def list_user_by_status(self, request, *args, **kwargs):
        user_status = self.kwargs.get("status")
        if user_status not in [
            UserProfile.ORDINARY_USER,
            UserProfile.LIBRARY_ASSISTANT,
            UserProfile.ADMINISTRATOR,
            UserProfile.MODERATOR
        ]:
            return ErrorResponse(
                error_type=errors.STATUS_NOT_FOUND,
                status=status.HTTP_404_NOT_FOUND,
                description=errors.STATUS_NOT_FOUND
            )
        users = UserProfile.objects.filter(user_status=user_status)
        return SuccessResponse(
            data=UsersSerializer(users, many=True).data,
            status=status.HTTP_200_OK
        )

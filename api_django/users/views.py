from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from users.serializers import UsersSerializer
from utils.responses import ErrorResponse, SuccessResponse
from django.shortcuts import get_object_or_404

from users.models import UserProfile

from utils import errors


class UsersView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(UserProfile, id=pk)
        serializer = UsersSerializer(user)
        return SuccessResponse(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        instance = get_object_or_404(UserProfile, id=pk)
        serializer = UsersSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessResponse(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_name="status", url_path=r"list_status_user/(?P<status>\w+)")
    def list_status_user(self, request, *args, **kwargs):
        user_status = self.kwargs.get("status")
        if user_status not in [UserProfile.ORDINARY_USER, UserProfile.LIBRARY_ASSISTANT,
                               UserProfile.ADMINISTRATOR, UserProfile.MODERATOR]:

            return ErrorResponse(
                error_type=errors.STATUS_NOT_FOUND,
                status=status.HTTP_404_NOT_FOUND,
                description=errors.STATUS_NOT_FOUND_DESCRIPTION
            )
        users = UserProfile.objects.filter(user_status=user_status)

        return SuccessResponse(
            data=UsersSerializer(users, many=True).data,
            status=status.HTTP_200_OK
        )


# TODO починить обновление данных у связанных моделей


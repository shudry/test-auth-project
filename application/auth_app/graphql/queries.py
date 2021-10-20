from graphene import List

from django.contrib.auth import get_user_model

from .types import UserType


class UsersQuery:
    users = List(UserType)

    def resolve_users(self, info, **kwargs):
        ''' Get list of all users '''
        return get_user_model().objects.all()

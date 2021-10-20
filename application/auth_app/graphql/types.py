from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username',
                  'is_staff', 'is_superuser', 'date_joined', )

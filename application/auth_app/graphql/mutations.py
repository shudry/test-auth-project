import graphql_jwt

from graphene import (
        Mutation as GrapheneMutation, Field, String, Boolean
    )
from django.contrib.auth import get_user_model
from django.core.validators import (
        validate_email, MinLengthValidator, MaxLengthValidator
    )
from django.core.exceptions import ValidationError

from auth_app.utils import generate_username
from .types import UserType


validate_min_length = MinLengthValidator(8)
validate_max_length = MaxLengthValidator(24)


class Registration(GrapheneMutation):
    ''' New user registration '''

    class Arguments:
        name = String(required=True)
        email = String(required=True)
        password = String(required=True)

    user = Field(UserType)

    success = Boolean()
    error_code = String()

    @staticmethod
    def mutate(root, info, name, email, password):
        exist_users = get_user_model().objects.filter(email=email).count()

        # Check if user already exist
        if exist_users > 0:
            return Registration(success=False, error_code='user-already-exist')

        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            return Registration(success=False, error_code='invalid_email')

        # Validate password
        try:
            validate_min_length(password)
            validate_max_length(password)
        except ValidationError:
            return Registration(success=False, error_code='invalid_password')

        user = get_user_model()(
            first_name=name,
            email=email,
            username=generate_username()
        )
        user.set_password(password)
        user.save()

        return Registration(success=True, user=user)


class AuthMutation:
    registration = Registration.Field()
    login = graphql_jwt.ObtainJSONWebToken.Field()

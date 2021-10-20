from graphene import (
        Mutation as GrapheneMutation, Field, String, Boolean
    )

from .types import UserType


class Registration(GrapheneMutation):
    ''' New user registration '''

    class Arguments:
        name = String(required=True)
        email = String(required=True)
        password = String(required=True)

    user = Field(UserType)

    success = Boolean()
    error = String()

    @staticmethod
    def mutate(root, info, name, email, password):
        return Registration(success=True)


class AuthMutation:
    registration = Registration.Field()

import graphene

from auth_app.graphql.queries import UsersQuery
from auth_app.graphql.mutations import AuthMutation


class Query(graphene.ObjectType,
            UsersQuery):
    pass


class Mutation(graphene.ObjectType,
               AuthMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

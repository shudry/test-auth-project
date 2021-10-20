import uuid


def generate_username() -> str:
    return str(uuid.uuid4())

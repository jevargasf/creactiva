from django.contrib.auth.models import User
from main.models import Perfil

def crear_usuario(username: str, first_name: str, last_name: str, email: str, password: str):
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )
    user.save()
    perfil = Perfil.objects.create(
        codigo='100',
        user=user
    )
    perfil.save()
    return True

# Form choices
def get_tipos_organizacion():
    pass
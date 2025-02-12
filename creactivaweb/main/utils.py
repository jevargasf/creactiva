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
        codigo='000',
        user=user
    )
    perfil.save()
    return True

def get_representantes():
    data = Perfil.objects.filter(codigo='010')
    if len(data) != 0:
        lista_rep = [['0', 'Seleccione al representante de la organización']]
        for rep in data:
            lista_rep.append([str(rep.id), f'{rep.user} | {rep.user.first_name} {rep.user.last_name}'])
        return lista_rep
    else:
        return None
    
# SIGUIENTE: probar cómo funciona esto. Continuar con el proceso de capturar la data del formulario
# de solicitud.
    # 1. Guardar la data de 1 solicitud
    # 2. Recuperarla con autollenado en el formulario de admin
        # - Primero, elegir al representante que se desea registrar (realizar post)
        # - Segundo, redirigir a otro formulario previamente autollenado, que este sea el final
        # para realizar el registro de la suscripción
    
# SIGUIENTE: Programa que identifique cuándo la suscripción es caduca. Esto quiere decir:
# dejar una tarea programada en el servidor
    
# SIGUIENTE 2: Desarrollar la pantalla de "detalle" de la compra de suscripción individual
# REQUISITO PREVIO: Agregar los datos de las suscripciones individuales a una tabla en la bd
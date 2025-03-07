from django.contrib.auth.models import User
from main.models import Perfil
from jwt import JWT
from jwt.jwk import OctetJWK
from django.utils import timezone
from creactivaweb.settings import JWT_SECURE
from suscripciones.models import Planes, Suscripcion, PerfilSuscripcion, CursosSuscripcion
from django.utils.timezone import now
from cursos.models import Curso
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from smtplib import SMTPException

def crear_usuario(username: str, first_name: str, last_name: str, email: str, password: str):
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        is_active=False
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
    
def crear_token(**kwargs):
    jwt = JWT()
    jwk = OctetJWK(key=JWT_SECURE.encode('utf-8'))
    
    ts = str(timezone.now())
    payload = {
        'ts': ts
    }

    for key, arg in kwargs.items():
        payload[key] = arg
        
    token = jwt.encode(payload, jwk, alg='HS256')
    return token

def traducir_token(token):
    jwt = JWT()
    jwk = OctetJWK(key=JWT_SECURE.encode('utf-8'))

    mensaje = jwt.decode(token, jwk, do_time_check=True)
    return mensaje

def crear_usuario_creactiva(username: str):
    try:
        user_object = User.objects.get(username=username)
        user_object.is_active = True
        perfil_object = Perfil.objects.get(user_id=user_object.id)
        plan_object = Planes.objects.get(pk=7)
        # CREAR UN PLAN INFINITO EN LA BD
        # CREAR UNA SUSCRIPCIÓN, UN PERFILSUSCRIPCION Y UN CURSOSUSCRIPCION
        # ACTUALIZAR CÓDIGO PERFIL
        perfil_object.codigo = '100'
        suscripcion_object = Suscripcion(
            fecha_inicio=now(),
            fecha_termino=now(),
            monto=plan_object.monto,
            codigo_promocional=plan_object.nombre,
            plan=plan_object
        )
        suscripcion_object.save()
        cursos_data = Curso.objects.all()
        for curso in cursos_data:
            cursosuscripcion_object = CursosSuscripcion(
                suscripcion=suscripcion_object,
                curso=curso
            )
            cursosuscripcion_object.save()

        perfilsuscripcion_object = PerfilSuscripcion(
            suscripcion=suscripcion_object,
            perfil=perfil_object,
            codigo_promocional=None,
            estado_suscripcion='1'
        )
        user_object.save()
        perfil_object.save()
        perfilsuscripcion_object.save()
        return True
    except Exception as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")

def enviar_correo(r_nombre: str, r_email: str, e_mail: str, asunto: str, app: str, archivo: str, url=None):
    try:
        if url == None:
            context = {
                'nombre': r_nombre
            }
        else:
            context = {
                'nombre': r_nombre,
                'url': url
            }
        ruta = f"/home/creacti3/creactivaweb/templates/mails/{app}/{archivo}.txt"
        text_content = render_to_string(
        ruta,
        context
        )
        #ruta_html=f'/home/creacti3/creactivaweb/templates/mails/{app}/{archivo}.html'
        
        #html_content = render_to_string(
        #    ruta_html,
        #    context
        #)
        msg = EmailMultiAlternatives(
            asunto,
            text_content,
            e_mail,
            [r_email]
        )
        #msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except SMTPException as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
        return False
    
def enviar_correo_admin(r_email: str, e_mail: str, asunto: str, app: str, archivo: str, form: dict):
    try:
        context = {'form': form}
        
        ruta = f"/home/creacti3/creactivaweb/templates/mails/{app}/{archivo}.txt"
        text_content = render_to_string(
        ruta,
        context
        )
        
        #ruta_html = f'/home/creacti3/creactivaweb/templates/mails/{app}/{archivo}.html'
        #html_content = render_to_string(
        #    ruta_html,
        #    context
        #)
        msg = EmailMultiAlternatives(
            asunto,
            text_content,
            e_mail,
            [r_email]
        )
        #msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except SMTPException as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
        return False
    
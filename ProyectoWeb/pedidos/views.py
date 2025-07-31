from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido

from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import Producto

@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
     # Crear el pedido
    pedido = Pedido.objects.create(user=request.user)

    # Obtener el carro del usuario
    carro = Carro(request)
    
    # Guardar todas las líneas de pedido en la base de datos
    lineas_pedido = []

    # Crear las líneas del pedido desde los productos en el carro
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)

    # Enviar correo al usuario
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
    )

    messages.success(request, "El pedido se ha creado correctamente")


    carro.limpiar_carro()

    return redirect('../tienda')


def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    
    # Renderizar el contenido del correo en HTML
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario")
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "ivancondori321@gmail.com"
    to = kwargs.get("email_usuario")

    try:
        validate_email(to)  # Validar dirección de correo
        send_mail(
            asunto,
            mensaje_texto,
            from_email,
            [to],
            html_message=mensaje,
            fail_silently=False  # Mostrar errores si algo falla
        )
        print(f"✅ Correo enviado a {to}")
    except ValidationError:
        print(f"❌ Email inválido: {to}")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")
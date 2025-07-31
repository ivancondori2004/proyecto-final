from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage


# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email_usuario=request.POST.get("email")
            contenido=request.POST.get("contenido")


            email=EmailMessage("Mensaje desde App Django",
                f"El usuario con nombre {nombre} con la dirección {email_usuario} escribe lo siguiente:\n\n {contenido}",
                "ivancondori321@gmail.com",
                ["ivancondori321@gmail.com"]
                ,reply_to=[email_usuario])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except Exception as e:
                print("ERROR AL ENVIAR EL CORREO:", e) 
                return redirect("/contacto/?novalido")



    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
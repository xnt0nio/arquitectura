from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import * 
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group



def grupo_requerido(nombre_grupo):
    def decorator(view_fuc):
        @user_passes_test(lambda user: user.groups.filter(name=nombre_grupo).exists())
        def wrapper(request, *arg, **kwargs):
            return view_fuc(request, *arg, **kwargs)
        return wrapper
    return decorator


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            grupo = Group.objects.get(name="usuario")
            user.groups.add(grupo)
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #redirigir al home
            return redirect(to="index")
        data["form"] = formulario    
    return render(request, 'registration/registro.html',data)



def contacto(request):
    if request.method == 'POST':
        form = Contacto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensaje enviado correctamente")
            return redirect('contacto')
    else:
        form = Contacto()
    return render(request, 'core/contacto.html', {'form': form})




def index(request):
    return render(request, 'core/index.html')



def comentarios(request):
    comentario = ContactForm.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(comentario, 3)
    page_obj = paginator.page(page_number)

    data = {   
        'comentarios': comentario,    
        'historial_compras': page_obj,         
    }    

    return render(request, 'core/comentarios.html',data)



def nodisponible(request, invalid_path=None):
    return render(request, 'core/nodisponible.html')



def menu(request):
    productosAll = Producto.objects.all()
    tipos_productos = TipoProducto.objects.all()
    categoria_seleccionada = request.GET.get('categoria')

    if categoria_seleccionada:
        productosAll = Producto.objects.filter(tipo__descripcion=categoria_seleccionada)
    else:
        productosAll = Producto.objects.all()

    categorias = []

    for tipo_producto in tipos_productos:
        productos = productosAll.filter(tipo=tipo_producto)
        if productos.exists():
            categorias.append({
                'tipo_producto': tipo_producto,
                'productos': productos
            })

    data = {
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,
        'tipos_productos': tipos_productos,
        'productos' : productosAll
    }
    return render(request, 'core/menu.html', data)





@grupo_requerido('vendedor')
def adm(request):
    productosAll = Producto.objects.all() 
    tipos_productos = TipoProducto.objects.all()
    categoria_seleccionada = request.GET.get('categoria')

    if categoria_seleccionada:
        productosAll = Producto.objects.filter(tipo__descripcion=categoria_seleccionada)
    else:
        productosAll = Producto.objects.all()

    categorias = []

    for tipo_producto in tipos_productos:
        productos = productosAll.filter(tipo=tipo_producto)
        if productos.exists():
            categorias.append({
                'tipo_producto': tipo_producto,
                'productos': productos
            })  

    data = {
        'listaProductos': productosAll,    
        'categoria_seleccionada': categoria_seleccionada,
        'tipos_productos': tipos_productos,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,     
        'productos' : productosAll             
    }
    return render(request, 'core/adm.html', data)


@grupo_requerido('vendedor')
def add(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")
    return render(request, 'core/add-product.html', data)


@grupo_requerido('vendedor')
def update(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' : ProductoForm(instance=producto) 
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)



@grupo_requerido('admin')
def delete(request, id):
    producto = Producto.objects.get(id=id) 
    producto.delete()
    return redirect(to="adm")


@grupo_requerido('vendedor')
def deleteComent(request, id):
    comentario = ContactForm.objects.get(id=id)
    comentario.delete()
    return redirect(to="comentarios")
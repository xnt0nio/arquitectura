from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
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





#esto son solo los add

#1
def addinstructor(request):
    data = {
        'form' : InstructorForm()
    }

    if request.method == 'POST':
        formulario = InstructorForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")
    return render(request, 'core/addinstructor.html', data)



#2
def addadultomayor(request):
    data = {
        'form' : AdultoMayorForm()
    }

    if request.method == 'POST':
        formulario = AdultoMayorForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")
    return render(request, 'core/addadultomayor.html', data)






#3
def materiales(request):
    data = {
        'form' : MaterialesForm()
    }

    if request.method == 'POST':
        formulario = MaterialesForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")    
    return render(request, 'core/materiales.html', data)




#4
def sala(request):
    data = {
        'form' : SalaForm()
    }

    if request.method == 'POST':
        formulario = SalaForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")      
    return render(request, 'core/materiales.html', data)





#5
def addtalleres(request):
    data = {
        'form' : TalleresForm()
    }

    if request.method == 'POST':
        formulario = TalleresForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save()
     
            messages.success(request, "Producto almacenado correctamente")      
    return render(request, 'core/addtalleres.html', data)    



#6
def postulaciontaller(request):
    data = {
        'form' : PostulacionTallerForm()
    }

    if request.method == 'POST':
        formulario = PostulacionTallerForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")      
    return render(request, 'core/postulaciontaller.html', data)   





#7
def addMuni(request):
    data = {
        'form' : MunicipalidadForm()
    }

    if request.method == 'POST':
        formulario = MunicipalidadForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")      
    return render(request, 'core/addMuni.html', data)       
  




#8
def addpago(request):
    data = {
        'form' : PagoForm()
    }

    if request.method == 'POST':
        formulario = PagoForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")      
    return render(request, 'core/addMuni.html', data)       
  

#9
def addbono(request):
    data = {
        'form' : BonoForm()
    }

    if request.method == 'POST':
        formulario = BonoForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")      
    return render(request, 'core/addMuni.html', data)       


#10
def addusuario(request):
    data = {
        'form' : UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")      
    return render(request, 'core/addMuni.html', data)       


#11
def addcredencial(request):
    data = {
        'form' : CredencialesForm()
    }

    if request.method == 'POST':
        formulario = CredencialesForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")      
    return render(request, 'core/addMuni.html', data)       


#12
def addPostulacionInstructor(request):
    data = {
        'form' : PostulacionInstructorForm()
    }

    if request.method == 'POST':
        formulario = PostulacionInstructorForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            
            messages.success(request, "Producto almacenado correctamente")      
    return render(request, 'core/addMuni.html', data)       
          


#listar aqui son 12
def listar(request):
    instructores = instructor.objects.all()
    adultos_mayores = adulto_mayor.objects.all()
    materiales = Materiales.objects.all()
    sala = Sala.objects.all()
    talleres = Talleres.objects.all()
    postulaciones_taller = postulacion_taller.objects.all()
    municipalidades = Municipalidad.objects.all()
    pagos = pago.objects.all()
    bonos = bono.objects.all()
    usuarios = usuario.objects.all()
    credenciales = credencial.objects.all()
    postulaciones_instructor = postulacion_instructor.objects.all()

    return render(request, 'core/listar.html', {
        'instructores': instructores,
        'adultos_mayores': adultos_mayores,
        'materiales': materiales,
        'sala': sala,
        'tallere': talleres,
        'postulaciones_taller': postulaciones_taller,
        'municipalidades': municipalidades,
        'pagos': pagos,
        'bonos': bonos,
        'usuarios': usuarios,
        'credenciales': credenciales,
        'postulaciones_instructor': postulaciones_instructor,
    })



















#los listar aqui son 12 en total











































































































































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




def delete(request, id):
    producto = Producto.objects.get(id=id) 
    producto.delete()
    return redirect(to="adm")


@grupo_requerido('vendedor')
def deleteComent(request, id):
    comentario = ContactForm.objects.get(id=id)
    comentario.delete()
    return redirect(to="comentarios")







#1
def updateinstructor(request, id):
    instructor = Instructor.objects.get(id=id)
    data = {
        'form' : InstructorForm(instance=instructor) 
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=instructor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)    









#2
def updateadultomayor(request, id):
    adulto = adulto_mayor.objects.get(id=id)
    data = {
        'form' : AdultoMayorForm(instance=adulto) 
    }

    if request.method == 'POST':
        formulario = AdultoMayorForm(data=request.POST, instance=adulto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)








#3
def updatemateriales(request, id):
    material = Materiales.objects.get(id=id)
    data = {
        'form' : MaterialesForm(instance=material) 
    }

    if request.method == 'POST':
        formulario = MaterialesForm(data=request.POST, instance=material, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)





#4
def updatesala(request, id):
    sala = Sala.objects.get(id=id)
    data = {
        'form' : SalaForm(instance=sala) 
    }

    if request.method == 'POST':
        formulario = SalaForm(data=request.POST, instance=sala, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)      





#5
def updatetalleres(request, id):
    taller = Talleres.objects.get(id=id)
    data = {
        'form' : TalleresForm(instance=taller) 
    }

    if request.method == 'POST':
        formulario = TalleresForm(data=request.POST, instance=taller, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)










#6
def updatepostulaciontaller(request, id):
    postulacioninstructor = postulacion_instructor.objects.get(id=id)
    data = {
        'form' : PostulacionInstructorForm(instance=postulacioninstructor) 
    }

    if request.method == 'POST':
        formulario = PostulacionInstructorForm(data=request.POST, instance=postulacioninstructor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)







#7
def updatepostulaciontaller(request, id):
    postulacionTaller = postulacion_taller.objects.get(id=id)
    data = {
        'form' : PostulacionTallerForm(instance=postulacionTaller) 
    }

    if request.method == 'POST':
        formulario = PostulacionTallerForm(data=request.POST, instance=postulacionTaller, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)    







#8
def updatemuni(request, id):
    municipalidad = Municipalidad.objects.get(id=id)
    data = {
        'form' : MunicipalidadForm(instance=municipalidad) 
    }

    if request.method == 'POST':
        formulario = MunicipalidadForm(data=request.POST, instance=municipalidad, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)  




 #9
def updatepago(request, id):
    pago = Pago.objects.get(id=id)
    data = {
        'form' : PagoForm(instance=pago) 
    }

    if request.method == 'POST':
        formulario = PagoForm(data=request.POST, instance=pago, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)  



#10
def updatebono(request, id):
    bono = Bono.objects.get(id=id)
    data = {
        'form' : BonoForm(instance=bono) 
    }

    if request.method == 'POST':
        formulario = BonoForm(data=request.POST, instance=bono, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)  



#11
def updateusuario(request, id):
    usuario = Usuario.objects.get(id=id)
    data = {
        'form' : UsuarioForm(instance=usuario) 
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)              


#12
def updatecredencial(request, id):
    credencial = Credencial.objects.get(id=id)
    data = {
        'form' : CredencialesForm(instance=credencial) 
    }

    if request.method == 'POST':
        formulario = CredencialesForm(data=request.POST, instance=credencial, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)              


#13
def updatepostulacioninstructor(request, id):
    postulacioninstructor = postulacion_instructor.objects.get(id=id)
    data = {
        'form' : PostulacionInstructorForm(instance=postulacioninstructor) 
    }

    if request.method == 'POST':
        formulario = PostulacionInstructorForm(data=request.POST, instance=postulacioninstructor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()           
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 
         
    return render(request, 'core/update-product.html', data)              






































#los delete aqui abajo son 12
def eliminar_instructor(request, id):
    inst_instructor = get_object_or_404(instructor, id=id)
    if request.method == 'POST':
        inst_instructor.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_instructor})


def eliminar_adultomayor(request, id):
    inst_adulto = get_object_or_404(adulto_mayor, id=id)
    if request.method == 'POST':
        inst_adulto.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_adulto})

def eliminar_materiales(request, id):
    inst_materiales = get_object_or_404(Materiales, id=id)
    if request.method == 'POST':
        inst_materiales.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_materiales})

def eliminar_sala(request, id):
    inst_sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        inst_sala.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_sala})


def eliminar_talleres(request, id):
    inst_talleres = get_object_or_404(Talleres, id=id)
    if request.method == 'POST':
        inst_talleres.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_talleres})

def eliminar_postulaciontaller(request, id):
    inst_posttaller = get_object_or_404(postulacion_taller, id=id)
    if request.method == 'POST':
        inst_posttaller.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_posttaller})

def eliminar_Muni(request, id):
    inst_muni = get_object_or_404(Municipalidad, id=id)
    if request.method == 'POST':
        inst_muni.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_muni})

def eliminar_pago(request, id):
    inst_pago = get_object_or_404(pago, id=id)
    if request.method == 'POST':
        inst_pago.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_pago})

def eliminar_bono(request, id):
    inst_bono = get_object_or_404(bono, id=id)
    if request.method == 'POST':
        inst_bono.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_bono})

def eliminar_postulacioninstructor(request, id):
    inst_postinst = get_object_or_404(postulacion_instructor, id=id)
    if request.method == 'POST':
        inst_postinst.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_postinst})

def eliminar_usuario(request, id):
    inst_usuario = get_object_or_404(usuario, id=id)
    if request.method == 'POST':
        inst_usuario.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_usuario})

def eliminar_credencial(request, id):
    inst_credencial = get_object_or_404(credencial, id=id)
    if request.method == 'POST':
        inst_credencial.delete()
        return HttpResponseRedirect(reverse('listar'))
    return render(request, 'core/listar.html', {'elemento': inst_credencial})


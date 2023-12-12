from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('contacto', contacto, name="contacto"),

    path('accounts/', include('django.contrib.auth.urls')),
    path('nodisponible', nodisponible, name="nodisponible"),  
    path('registro/', registro, name='registro'),
    
    
  
    #de arquitectura
    path('addinstructor', addinstructor, name='addinstructor'),
    path('addadultomayor', addadultomayor, name='addadultomayor'),
    path('materiales', materiales, name='materiales'),
    path('sala', sala, name='sala'), 
    path('addtalleres', addtalleres, name='addtalleres'),
    path('postulaciontaller', postulaciontaller, name='postulaciontaller'),
    path('addMuni', addMuni, name="addMuni"),
    path('addpago', addpago, name="addpago"),
    path('addbono', addbono, name="addbono"),
    path('addusuario', addusuario, name="addusuario"),
    path('addcredencial', addcredencial, name="addcredencial"),
    path('addPostulacionInstructor', addPostulacionInstructor, name="addPostulacionInstructor"),
    path('inscripciontaller ', inscripciontaller, name="inscripciontaller"),
    
    
    
    path('listar', listar, name='listar'),
    path('listartalleres', listartalleres, name='listartalleres'),
    #los 12 listar aqui
    
    
    path('updateinstructor/<id>/', updateinstructor, name="updateinstructor"),
    path('updateadultomayor/<id>/', updateadultomayor, name="updateadultomayor"),
    path('updatemateriales/<id>/', updatemateriales, name="updatemateriales"),
    path('updatesala/<id>/', updatesala, name="updatesala"),
    path('updatetalleres/<id>/', updatetalleres, name="updatetalleres"),
    path('updatepostulaciontaller/<id>/', updatepostulaciontaller, name="updatepostulaciontaller"),
    path('updatemuni/<id>/', updatemuni, name="updatemuni"),
    path('updatepago/<id>/', updatepago, name="updatepago"),
    path('updatebono/<id>/', updatebono, name="updatebono"),
    path('updateusuario/<id>/', updateusuario, name="updateusuario"),
    path('updatecredencial/<id>/', updatecredencial, name="updatecredencial"),
    path('updatepostulacioninstructor/<id>/', updatepostulacioninstructor, name="updatepostulacioninstructor"),
    

   #los eliminar aqui
    path('eliminar_instructor/<int:id>/', eliminar_instructor, name='eliminar_instructor'),
    path('eliminar_adultomayor/<int:id>/', eliminar_adultomayor, name='eliminar_adultomayor'),
    path('eliminar_materiales/<int:id>/', eliminar_materiales, name='eliminar_materiales'),
    path('eliminar_sala/<int:id>/', eliminar_sala, name='eliminar_sala'),
    path('eliminar_talleres/<int:id>/', eliminar_talleres, name='eliminar_talleres'),
    path('eliminar_postulaciontaller/<int:id>/', eliminar_postulaciontaller, name='eliminar_postulaciontaller'),
    path('eliminar_Muni/<int:id>/', eliminar_Muni, name='eliminar_Muni'),
    path('eliminar_pago/<int:id>/', eliminar_pago, name='eliminar_pago'),
    path('eliminar_bono/<int:id>/', eliminar_bono, name='eliminar_bono'),
    path('eliminar_usuario/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
    path('eliminar_credencial/<int:id>/', eliminar_credencial, name='eliminar_credencial'),
    path('eliminar_postulacioninstructor/<int:id>/', eliminar_postulacioninstructor, name='eliminar_postulacioninstructor'),




    path('menu', menu, name="menu"),  
    path('adm', adm, name="adm"),  
    path('add', add, name="add"),  
    path('comentarios', comentarios, name="comentarios"), 
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
    path('deleteComent/<id>/', deleteComent, name="deleteComent"),
]





urlpatterns += [
    path('<path:invalid_path>', nodisponible, name="error404"),
]




    


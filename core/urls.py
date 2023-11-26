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




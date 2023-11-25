from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('contacto', contacto, name="contacto"),
    path('menu', menu, name="menu"),  
    path('adm', adm, name="adm"),  
    path('add', add, name="add"),  
    path('comentarios', comentarios, name="comentarios"),  
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
    path('deleteComent/<id>/', deleteComent, name="deleteComent"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('nodisponible', nodisponible, name="nodisponible"),  
    path('registro/', registro, name='registro'),
]

urlpatterns += [
    path('<path:invalid_path>', nodisponible, name="error404"),
]
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.paginaprincipal, name='paginaprincipal'),
    path('contacto/', views.contacto, name='contacto'),
    path('deporte/', views.deporte, name='deporte'),
    path('login', views.login, name='login'),
    path('nacional', views.nacional, name='nacional'),
    path('policial', views.policial, name='policial'),
    path('recuperarcontraseña', views.recuperarcontraseña, name='recuperarcontraseña'),
    path('tendencia', views.tendencia, name='tendencia'),
    path('Nuevanoticia',views.nueva_noticia,name='Nuevanoticia'),
    path('gestion/',views.gesNoticia,name='gestion'),
    path('gestion/editarnoti/<codigo>', views.editarnoti, name='editarnoti'),
    path('gestion/borrarnoticias/<codigo>', views.borrarnoticias, name='borrarnoticias'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
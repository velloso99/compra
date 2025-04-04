from django.urls import path
from .views import lista_produtos


urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('categoria/<int:categoria_id>/', lista_produtos, name='produtos_por_categoria'),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flores', views.listar_flores, name='listar_flores'),
    path('pedido/<int:flor_id>/', views.criar_pedido, name='criar_pedido'),
    path('carrinho/', views.listar_carrinho, name='listar_carrinho'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

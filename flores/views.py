from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm, PedidoForm
from .models import Flor, Pedido, Carrinho
from .forms import RegistroForm
from django.shortcuts import render


def home(request):
    return render(request, 'flores/home.html')


def listar_flores(request):
    flores = Flor.objects.all()
    return render(request, 'flores/listar_flores.html', {'flores': flores})

@login_required
def criar_pedido(request, flor_id):
    flor = get_object_or_404(Flor, id=flor_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.flor = flor
            pedido.cliente = request.user
            pedido.save()
            Carrinho.objects.create(
            cliente=request.user,
            flor=flor,
            quantidade=pedido.quantidade)
            return redirect('listar_carrinho')
    else:
        form = PedidoForm()
    return render(request, 'flores/criar_pedido.html', {'form': form, 'flor': flor})

@login_required
def listar_carrinho(request):
    carrinho = Carrinho.objects.filter(cliente=request.user)
    return render(request, 'flores/listar_carrinho.html', {'carrinho': carrinho})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'flores/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('listar_flores')
    else:
        form = LoginForm()
    return render(request, 'flores/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

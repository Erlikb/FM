from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import TaskForm
import locale



# Create your views here.


def home(request):
    return render(request, 'home.html')


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    "error": 'Username already exists'
                })
        return render(request, 'singup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })


def tasks(request):
    return render(request, 'tasks.html')

def task2(request):
    return render(request, 'task2.html')

def task3(request):
    return render(request, 'task3.html')

def create_task(request):

    if request.method == 'GET':
            return render(request, 'create_task.html', {
        'form': TaskForm
    })
    else: 
        print(request.POST)
        return render(request, 'create_task.html', {
        'form': TaskForm
    })


def singout(request):
    logout (request)
    return redirect('home')

def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html',{
            'form': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST
        ['password'])
        if user is None:
            return render(request, 'singin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')
        
def tema1(request):
    return render(request, 'tema1.html')

def diferenciadecuadrados(request):
    return render(request, 'diferenciadecuadrados.html')

def diferenciadecubos(request):
    return render(request, 'diferenciadecubos.html')

def trinomiocuadradoperfecto(request):
    return render(request, 'trinomiocuadradoperfecto.html')

def tema6(request):
    return render(request, 'tema6.html')

def tema7(request):
    return render(request, 'tema7.html')

def tema8(request):
    return render(request, 'tema8.html')

def calculadora(request):
    return render(request, 'tema1.html')

def factorcomun(request):
    return render(request, 'factorcomun.html')

def tema1(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operacion']
        if operation == 'suma':
            resultado = num1 + num2
        elif operation == 'resta':
            resultado = num1 - num2
        elif operation == 'multiplicacion':
            resultado = num1 * num2
        elif operation == 'division':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = 'Error: División por cero no permitida'
        return render(request, 'tema1.html', {'resultado': resultado})
    return render(request, 'tema1.html')

def factorcomun(request):
    factor_comun = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        number3 = int(request.POST.get('number3'))
        factor_comun = calcular_factor_comun_logica(number1, number2, number3)
    return render(request, 'factorcomun.html', {'factor_comun': factor_comun})

def calcular_factor_comun_logica(a, b, c):
    menor = min(a, b, c)
    factor_comun = 1
    for i in range(1, menor + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            factor_comun = i
    return factor_comun

def diferenciadecuadrados(request):
    diferencia_de_cuadrados = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        diferencia_de_cuadrados = calcular_diferencia_cuadrados_logica(number1, number2)
    return render(request, 'diferenciadecuadrados.html', {'diferencia_de_cuadrados': diferencia_de_cuadrados})

def calcular_diferencia_cuadrados_logica(a, b):
    diferencia_cuadrados = a**2 - b**2
    factorizacion = (a + b) * (a - b)
    return f"La diferencia de cuadrados es {diferencia_cuadrados}, que se factoriza como {factorizacion}."

def diferenciadecubos(request):
    diferencia_de_cubos = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        diferencia_de_cubos = calcular_diferencia_cubos_logica(number1, number2)
    return render(request, 'diferenciadecubos.html', {'diferencia_de_cubos': diferencia_de_cubos})

def calcular_diferencia_cubos_logica(a, b):
    diferencia_de_cubos = a**3 - b**3
    factor_comun = a - b
    suma_cubos = a**2 + a*b + b**2
    return f"La diferencia de cubos es {diferencia_de_cubos}, que se factoriza como ({factor_comun})({suma_cubos})."

def trinomiocuadradoperfecto(request):
    trinomio_cuadrado_perfecto = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        trinomio_cuadrado_perfecto = calcular_trinomio_cuadrado_perfecto_logica(number1, number2)
    return render(request, 'trinomiocuadradoperfecto.html', {'trinomio_cuadrado_perfecto': trinomio_cuadrado_perfecto})

def calcular_trinomio_cuadrado_perfecto_logica(a, b):
    trinomio_cuadrado = a*2 + 2 * a * b + b*2
    binomio_cuadrado = (a + b)**2
    return f"El trinomio cuadrado perfecto es {trinomio_cuadrado}, que se factoriza como {binomio_cuadrado}."





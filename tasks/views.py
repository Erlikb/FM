from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
import locale

# Create your views here.

# Pages

def singup(request):
    return render(request, 'singup.html')

def singin(request):
    return render(request, 'singin.html')

def home(request):
    return render(request, 'home.html')

def task1(request):
    return render(request, 'task1.html')

def task2(request):
    return render(request, 'task2.html')

def task3(request):
    return render(request, 'task3.html')

def task4(request):
    return render(request, 'task4.html')

def task5(request):
    return render(request, 'task5.html')

def task6(request):
    return render(request, 'task6.html')
# Singup


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
                return redirect('task1')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    "error": 'Username already exists'
                })
        return render(request, 'singup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })

# Singout


def singout(request):
    logout(request)
    return redirect('singin')


# Singin

def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
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
            return redirect('task1')
        
#calculadora 

def task1(request):
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
        return render(request, 'task1.html', {'resultado': resultado})
    return render(request, 'task1.html')

#Factor comun

def task2(request):
    factor_comun = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        number3 = int(request.POST.get('number3'))
        factor_comun = calcular_factor_comun_logica(number1, number2, number3)
    return render(request, 'task2.html', {'factor_comun': factor_comun})

def calcular_factor_comun_logica(a, b, c):
    menor = min(a, b, c)
    factor_comun = 1
    for i in range(1, menor + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            factor_comun = i
    return factor_comun

#Diferencia de cuadrados

def task3(request):
    diferencia_de_cuadrados = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        resultado, factorizacion = calcular_diferencia_cuadrados_logica(number1, number2)
        diferencia_de_cuadrados = {"resultado": resultado, "factorizacion": factorizacion}
    return render(request, 'task3.html', {'diferencia_de_cuadrados': diferencia_de_cuadrados})

def calcular_diferencia_cuadrados_logica(a, b):
    # Calcular la diferencia de cuadrados
    resultado = a**2 - b**2
    
    # Factorizar la diferencia de cuadrados
    factorizacion = (a + b, a - b)
    
    return resultado, factorizacion



#Trinomio cuadrado perfecto

def task4(request):
    trinomio_cuadrado_perfecto = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        trinomio_cuadrado_perfecto = calcular_trinomio_cuadrado_perfecto_logica(number1, number2)
    return render(request, 'task4.html', {'trinomio_cuadrado_perfecto': trinomio_cuadrado_perfecto})

def calcular_trinomio_cuadrado_perfecto_logica(a, b):
    trinomio_cuadrado = a**2 + 2 * a * b + b**2
    binomio_cuadrado = f"({a} + {b})^2"
    return f"El trinomio cuadrado perfecto es {trinomio_cuadrado}, que se factoriza como {binomio_cuadrado}."


#Diferencia de cubos 

def task5(request):
    diferencia_de_cubos = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        diferencia_de_cubos = calcular_diferencia_cubos_logica(number1, number2)
    return render(request, 'task5.html', {'diferencia_de_cubos': diferencia_de_cubos})

def calcular_diferencia_cubos_logica(a, b):
    diferencia_de_cubos = a**3 - b**3
    factor_comun = a - b
    suma_cubos = a**2 + a*b + b**2
    return f"La diferencia de cubos es {diferencia_de_cubos}, que se factoriza como ({a} - {b})({suma_cubos})."

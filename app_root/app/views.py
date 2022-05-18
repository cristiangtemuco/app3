#import inline as inline
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
#from .models import Paciente, Contacto, Atencion
#from .forms import ContactoForm, PacienteForm, AtencionForm #CustomUserCreationForm   esto es un ModelForm
from django.forms import inlineformset_factory #esto para inline forms
from django.contrib import messages #para sweet alert
from django.contrib.auth import authenticate, login #esto me permite autenticar inmediatamente despues de reigtrar al usuario
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required

def login(request):
    return redirect(to='accounts/login/')

@login_required
def home(request):
    return render(request, 'app/home.html')
from accounts.forms import UserRegistrationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


# def signup(request):
#     """
#     Função responsável por renderizar o formulário de registro do usuário.
#     """
#     if request.method == 'GET':
#         form = UserRegistrationForm()
    
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.username = obj.email
#             obj.save()
#             messages.success(request, 'A conta foi criada com sucesso! Faça login.')
#             return redirect('login')

#     return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    """
    Carrega uma página com dados da conta acessada.
    """
    if request.method == 'GET':
        return render(request, 'accounts/profile.html')

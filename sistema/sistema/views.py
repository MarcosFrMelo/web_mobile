from django.views.generic import View
from django.shortcuts import render

class Login(View):
    """
    Class based view para autenticação de usuarios.
    """
    def get(self, request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)

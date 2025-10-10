# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse, FileResponse, Http404
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

class ListarVeiculos(LoginRequiredMixin, ListView):
    """
    View para listar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculo/listar.html'


class CriarVeiculos(LoginRequiredMixin, CreateView):
    """
    View para criar um novo veículo.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class EditarVeiculos(LoginRequiredMixin, UpdateView):
    """
    View para editar um veículo existente.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    """
    View para deletar um veículo existente.
    """
    model = Veiculo
    template_name = 'veiculo/deletar.html'  # Apontando para o arquivo correto
    success_url = reverse_lazy('listar-veiculos')

class FotoVeiculo(View):
    """
    View para exibir a foto de um veículo.
    """
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto do Veículo não encontrado")
        except Exception as e:
            raise e
        

from django.forms import ModelForm
from veiculo.models import Veiculo

class FormularioVeiculo(ModelForm):
    """
    Formulário para o modelo Veículo.
    """

    class Meta:
        model = Veiculo
        exclude = []
from django.forms import ModelForm
from .models import Produto

class ProdutoModelForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'marca', 'preco', 'estoque']
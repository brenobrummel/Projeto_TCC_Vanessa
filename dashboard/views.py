from django.shortcuts import render
from estoque.models import Produto
from promocoes.models import RegraDesconto
from doacoes.models import Doacao
from django.utils import timezone

def dashboard_view(request):
    produtos_proximos_vencimento = Produto.objects.filter(validade__lte=timezone.now() + timezone.timedelta(days=7))
    total_estoque = Produto.objects.count()
    total_doacoes = Doacao.objects.count()
    context = {
        'produtos_proximos_vencimento': produtos_proximos_vencimento,
        'total_estoque': total_estoque,
        'total_doacoes': total_doacoes,
    }
    return render(request, 'dashboard/dashboard.html', context)
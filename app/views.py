from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Produto


@require_http_methods("GET")
def listar_produtos(request):
    produtos = Produto.objects.all().values()
    return JsonResponse(list(produtos), safe=False)

@csrf_exempt
@require_http_methods("POST")
def cadastrar_produto(request):
    dados = json.loads(request.body)
    produto = Produto.objects.create(
        nome=dados.get('nome'),
        marca=dados.get('marca'),
        preco=dados.get('preco'),
        estoque=dados.get('estoque')
        )
    return JsonResponse({"id":produto.id, "mensagem": "Produto cadastrado com sucesso"})

@csrf_exempt
@require_http_methods(["PUT"])
def atualizar_produto(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
        dados = json.loads(request.body)
        produto.nome = dados.get('nome', produto.nome)
        produto.marca = dados.get('marca', produto.marca)
        produto.preco = dados.get('preco', produto.preco)
        produto.estoque = dados.get('estoque', produto.estoque)
        produto.save()
        return JsonResponse({"message": "Produto atualizado com sucesso!"})
    except Produto.DoesNotExist:
        return JsonResponse({"error": "Produto não encontrado"}, status=404)

    
@csrf_exempt   
def deletar_produto(request):
    if request.method == 'DELETE':
        try:
            body = json.loads(request.body)  # Lê o corpo da requisição JSON
            produto_remover = body.get('nome')
            if produto_remover in lista_de_produtos:
                lista_de_produtos.remove(produto_remover)
                return JsonResponse({'mensagem': 'Produto removido', 'produtos': lista_de_produtos})
            else:
                return JsonResponse({'erro': 'Produto não encontrado'}, status=404)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'JSON inválido'}, status=400)
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)


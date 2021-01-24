from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'dna_app/index.html',)

def aconselhamento(request):
    return render(request,'dna_app/aconselhamento.html')

def agua_magnetizada_saude(request):
    return render(request,'dna_app/agua_magnetizada_saude.html')

def agua_magnetizada(request):
    return render(request,'dna_app/agua_magnetizada.html')

def arteterapia(request):
    return render(request,'dna_app/arteterapia.html')

def constelacao_familiar(request):
    return render(request,'dna_app/constelacao_familiar.html')

def galeria(request):
    return render(request,'dna_app/galeria.html')

def introducao_constelacao_familiar(request):
    return render(request,'dna_app/introducao_constelacao_familiar.html')

def loja(request):
    return render(request,'dna_app/loja.html')

def mandalas(request):
    return render(request,'dna_app/mandalas.html')

def meditacao_mentalizacao(request):
    return render(request,'dna_app/meditacao_mentalizacao.html')

def pnl(request):
    return render(request,'dna_app/pnl.html')

def quemsomos(request):
    return render(request,'dna_app/quemsomos.html')

def desenvolvimento_pessoal(request):
    return render(request,'dna_app/desenvolvimento_pessoal.html')

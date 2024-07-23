from django.shortcuts import render
from .forms import PreinscricaoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def preinscricao(request):
    if request.method == 'POST':
        form = PreinscricaoForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'success.html')
    else:
        form = PreinscricaoForm()
    return render(request, 'pre-inscricao.html', {'form': form})
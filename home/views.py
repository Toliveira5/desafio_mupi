from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensagem
from .forms import MensagemForm

def landpage(request):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'landpage.html',
                {'form': MensagemForm(), 'success': True}
            )
    else:
        form = MensagemForm()

    return render(request, 'landpage.html', {'form': form})

@login_required
def messages_list(request):
    mensagens = Mensagem.objects.all().order_by('-criado_em')
    return render(request, 'messages_list.html', {'mensagens': mensagens})

@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Mensagem, pk=pk)
    return render(request, 'message_detail.html', {'msg': msg})

@login_required
def message_edit(request, pk):
    msg = get_object_or_404(Mensagem, pk=pk)

    if request.method == 'POST':
        form = MensagemForm(request.POST, instance=msg)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem atualizada com sucesso!')
            return redirect('messages_list')
    else:
        form = MensagemForm(instance=msg)

    return render(request, 'message_edit.html', {'form': form, 'msg': msg})

@login_required
def message_delete_confirm(request, pk):
    msg = get_object_or_404(Mensagem, pk=pk)

    if request.method == 'POST':
        msg.delete()
        messages.success(request, 'Mensagem deletada com sucesso!')
        return redirect('messages_list')

    return render(request, 'message_delete_confirm.html', {'msg': msg})

def enviar_mensagem(request):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensagem_enviada')
    else:
        form = MensagemForm()

    return render(request, 'enviar_mensagem.html', {'form': form})

def mensagem_enviada(request):
    return render(request, 'mensagem_enviada.html')

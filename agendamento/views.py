from django.shortcuts import render, redirect
from agendamento.models import *

# Create your views here.
def ver_consultas(request):
    consultas = Consulta.objects.all()
    consultas_paciente = consultas.filter(status='A')

    return render(request, 'agendamento/consultas.html', {'consultas_paciente': consultas_paciente})


def deletar_consulta(request, id):

    consulta = Consulta.objects.get(pk=id)

    consulta.status = 'C'
    consulta.save()

    return redirect('/')
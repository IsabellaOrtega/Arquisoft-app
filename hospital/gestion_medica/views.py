from django.shortcuts import render
from django.http import JsonResponse
from .logic import gestion_medica_logic as gm
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def gestion_medica_view(request):
    if request.method == 'GET':
        pacientes = gm.get_pacientes()
        consultas = gm.get_consultas()
        pruebas = gm.get_pruebas()
        juntas = gm.get_juntas_medicas()

        datos = {
            'pacientes': pacientes,
            'consultas': consultas,
            'pruebas': pruebas,
            'juntas': juntas
        }

    elif request.method == 'POST':
        data = json.loads(request.body)

        tipo = data.get('tipo') 
        if tipo == 'paciente':
            paciente = gm.create_paciente(data)
            return JsonResponse({'status': 'ok', 'paciente_id': paciente.id})

        elif tipo == 'consulta':
            consulta = gm.create_consulta(data)
            return JsonResponse({'status': 'ok', 'consulta_id': consulta.id})

        else:
            return JsonResponse({'status': 'error', 'message': 'Tipo no reconocido'}, status=400)
        
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            tipo = data.get('tipo')

            if tipo == 'paciente':
                gm.update_paciente(data)
                return JsonResponse({'message': 'Paciente actualizado correctamente'}, status=200)
            else:
                return JsonResponse({'error': 'Tipo no reconocido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request,'gestion_medica.html', datos )
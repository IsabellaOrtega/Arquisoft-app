from ..models import (
    Usuario, Paciente, HistoriaClinica, ProfesionalSalud,
    Doctor, Enfermero, Tecnico, PruebaDiagnostica,
    MRI, EEG, MicroRNA, EventoMedico, Cirugia, Prescripcion,
    Consulta, JuntaMedica, InformeDiagnostico
)
from django.core.exceptions import ObjectDoesNotExist

def get_pacientes():
    pacientes = Paciente.objects.all()
    return pacientes

def get_paciente_id(id):
    try:
        return Paciente.objects.get(id=id)
    except Paciente.DoesNotExist:
        return None
    
def get_usuarios():
    return Usuario.objects.all()

def get_usuario_by_login(login):
    return Usuario.objects.filter(login=login).first()

def get_consultas_por_paciente(paciente_id):
    return Consulta.objects.filter(paciente__id=paciente_id)

def get_historia_clinica_by_paciente(usuario_id):
    return HistoriaClinica.objects.filter(paciente__usuario__id=usuario_id).first()

def get_profesionales():
    return ProfesionalSalud.objects.all()

def get_doctores():
    return Doctor.objects.all()

def get_enfermeros():
    return Enfermero.objects.all()

def get_tecnicos():
    return Tecnico.objects.all()

def get_pruebas_por_tipo(tipo):
    return PruebaDiagnostica.objects.filter(tipo=tipo)

def get_pruebas():
    return PruebaDiagnostica.objects.all()

def get_mris():
    return MRI.objects.all()

def get_eegs():
    return EEG.objects.all()

def get_micrornas():
    return MicroRNA.objects.all()

def get_prueba_by_id(prueba_id):
    return PruebaDiagnostica.objects.filter(id=prueba_id).first()

def get_eventos_medicos():
    return EventoMedico.objects.all()

def get_consultas():
    return Consulta.objects.all()

def get_cirugias():
    return Cirugia.objects.all()

def get_evento_by_id(evento_id):
    return EventoMedico.objects.filter(id=evento_id).first()

def get_prescripcion_by_evento(evento_id):
    return Prescripcion.objects.filter(evento_medico__id=evento_id).first()

def get_juntas_medicas():
    return JuntaMedica.objects.all()

def get_junta_by_id(junta_id):
    return JuntaMedica.objects.filter(id=junta_id).first()

def get_informes_by_junta(junta_id):
    return InformeDiagnostico.objects.filter(junta_medica__id=junta_id)

#POST
def create_paciente(datos):
    nuevo = Paciente.objects.create(
        nombre=datos.get('nombre'),
        edad=datos.get('edad'),
        direccion=datos.get('direccion')
    )
    return {
        "id": nuevo.id,
        "nombre": nuevo.nombre,
        "edad": nuevo.edad,
        "direccion": nuevo.direccion
    }

def create_consulta(datos):
    nueva = Consulta.objects.create(
        paciente_id=datos.get('paciente_id'),
        fecha=datos.get('fecha'),
        motivo=datos.get('motivo')
    )
    return {
        "id": nueva.id,
        "paciente_id": nueva.paciente_id,
        "fecha": nueva.fecha,
        "motivo": nueva.motivo
    }
#UPDATE
def update_usuario(usuario_id, data):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        usuario.nombre = data.get('nombre', usuario.nombre)
        usuario.login = data.get('login', usuario.login)
        usuario.password = data.get('password', usuario.password)
        usuario.rol = data.get('rol', usuario.rol)
        usuario.registro_medico = data.get('registro_medico', usuario.registro_medico)
        usuario.save()
        return usuario
    except ObjectDoesNotExist:
        return None
    
def update_paciente(usuario_id, data):
    try:
        paciente = Paciente.objects.get(usuario__id=usuario_id)
        paciente.email = data.get('email', paciente.email)
        paciente.numero_telefonico = data.get('numero_telefonico', paciente.numero_telefonico)
        paciente.edad = data.get('edad', paciente.edad)
        paciente.genero = data.get('genero', paciente.genero)
        paciente.save()
        return paciente
    except ObjectDoesNotExist:
        return None
    
def update_historia_clinica(paciente_id, data):
    try:
        historia = HistoriaClinica.objects.get(paciente__usuario__id=paciente_id)
        historia.tipo_de_sangre = data.get('tipo_de_sangre', historia.tipo_de_sangre)
        historia.alergias_medicamentos = data.get('alergias_medicamentos', historia.alergias_medicamentos)
        historia.condiciones_medicas = data.get('condiciones_medicas', historia.condiciones_medicas)
        historia.save()
        return historia
    except ObjectDoesNotExist:
        return None

def update_evento_medico(evento_id, data):
    try:
        evento = EventoMedico.objects.get(id=evento_id)
        evento.fecha = data.get('fecha', evento.fecha)
        evento.descripcion = data.get('descripcion', evento.descripcion)
        evento.save()
        return evento
    except ObjectDoesNotExist:
        return None
    
def update_consulta(evento_id, data):
    try:
        consulta = Consulta.objects.get(id=evento_id)
        consulta.motivo_consulta = data.get('motivo_consulta', consulta.motivo_consulta)
        consulta.diagnostico_preliminar = data.get('diagnostico_preliminar', consulta.diagnostico_preliminar)
        consulta.examenes_requeridos = data.get('examenes_requeridos', consulta.examenes_requeridos)
        consulta.observaciones = data.get('observaciones', consulta.observaciones)
        consulta.save()
        return consulta
    except ObjectDoesNotExist:
        return None
    

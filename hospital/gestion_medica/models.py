from django.db import models

# Create your models here.
class Usuario(models.Model):
    id= models.CharField(max_length=50, primary_key=True) #cedula
    nombre = models.CharField(max_length=255)
    login = models.CharField(max_length=50, unique=True)  
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=50)
    registro_medico = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    email = models.EmailField()
    numero_telefonico = models.CharField(max_length=20)
    edad = models.IntegerField()
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.usuario.nombre
    
class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    tipo_de_sangre = models.CharField(max_length=10)
    alergias_medicamentos = models.TextField()
    condiciones_medicas = models.TextField()

    def __str__(self):
        return f"Historia Clínica del paciente: {self.paciente.usuario.nombre}"
    
class ProfesionalSalud(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    registro_medico = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.usuario.nombre

class Doctor(ProfesionalSalud):
    especialidad = models.CharField(max_length=100)
    consultorio = models.IntegerField()

class Enfermero(ProfesionalSalud):
    area_responsable = models.CharField(max_length=100)

class Tecnico(ProfesionalSalud):
    tipo_examen = models.CharField(max_length=100)

class PruebaDiagnostica(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=50)
    resultados_preliminares = models.TextField()

class MRI(PruebaDiagnostica):
    archivo_dicom = models.CharField(max_length=255)
    hallazgos_preliminares = models.TextField()

class EEG(PruebaDiagnostica):
    archivo_eeg = models.CharField(max_length=255)
    duracion = models.IntegerField()
    eventos_detectados = models.TextField()

class MicroRNA(PruebaDiagnostica):
    biomarcadores = models.TextField()
    nivel_expresion = models.IntegerField()

class EventoMedico(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    fecha = models.DateField()
    descripcion = models.TextField()

class Cirugia(EventoMedico):
    tipo = models.CharField(max_length=100)
    riesgos = models.TextField()

class Prescripcion(models.Model):
    evento_medico = models.OneToOneField(EventoMedico, on_delete=models.CASCADE)
    medicamentos = models.TextField()
    dosis = models.TextField()

class Consulta(EventoMedico):
    motivo_consulta = models.TextField()
    diagnostico_preliminar = models.TextField()
    examenes_requeridos = models.TextField()
    observaciones = models.TextField()

class JuntaMedica(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    fecha = models.DateField()
    resumen = models.TextField()

class InformeDiagnostico(models.Model):
    junta_medica = models.ForeignKey(JuntaMedica, on_delete=models.CASCADE)
    field = models.TextField()
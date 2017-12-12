from django.db import models


class Patient(models.Model):
    name = models.CharField(
        'Nome do Paciente',
        max_length=200,
        default='',
    )
    email = models.EmailField(
        'Email',
        max_length=100,
        db_index=True,
        unique=True,
    )

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return "{}".format(self.email)

    def __repr__(self):
        return "{}".format(self.email)


class Procedure(models.Model):
    name = models.CharField('Nome do Procedimento', max_length=200, default='')
    description = models.CharField('Descrição', max_length=200, default='')

    class Meta:
        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}".format(self.name)


#TODO modify procedure field to procedures
class Schedule(models.Model):
    detail = models.CharField('Detalhes', max_length=200, default=None)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    procedure = models.ManyToManyField(Procedure, verbose_name='Procedimentos')
    date = models.DateField('Data da Consulta')
    start_time = models.TimeField('Hora do inicio')
    end_time = models.TimeField('Hora do fim')

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    @property
    def date_formatted(self):
        if self.date:
            return self.date.strftime('%d/%m/%Y')
        return ''

    def __str__(self):
        return "{}".format(self.pk)

    def __repr__(self):
        return "{}".format(self.pk)

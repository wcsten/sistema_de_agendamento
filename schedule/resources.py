from rest_framework import viewsets
from schedule.models import Patient, Procedure, Schedule
from schedule.serializers import (PatientSerializer,
                                  ProcedureSerializer,
                                  ScheduleSerializer)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

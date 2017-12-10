from rest_framework import serializers
from schedule.models import Patient, Procedure, Schedule


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            'name',
            'email',
        ]


class ProcedureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procedure
        fields = [
            'name',
            'description',
        ]


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = [
            'detail',
            'patient',
            'procedure',
        ]

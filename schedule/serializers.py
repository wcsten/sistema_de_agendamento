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
            'date',
            'start_time',
            'end_time',
        ]

        #TODO test the validate start_time and end_time
        def validate(self, data):
            print(data)
            if data['start_time'] > data['end_time']:
                raise serializers.ValidationError(
                    "A hora de Termino não pode ser maior que a hora de inicio")

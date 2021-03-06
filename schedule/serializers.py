from rest_framework import serializers
from schedule.models import Patient, Procedure, Schedule
from datetime import date


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            'name',
            'email',
        ]

    def validate_name(self, value):
        if not len(value.split()) > 1:
            raise serializers.ValidationError(
                'Por Favor insira um nome inteiro'
            )
        return value


class ProcedureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procedure
        fields = [
            'name',
            'description',
        ]

    def validate_name(self, value):
        if not len(value) > 3:
            raise serializers.ValidationError(
                'O nome do procedimento não pode ter menos que 3 caracteres'
            )
        return value

    def validate_description(self, value):
        if not len(value) > 3:
            raise serializers.ValidationError(
                'A descrição do procedimento não pode ter menos que 3 caracteres'
            )
        return value


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

    def validate_detail(self, value):
        if not len(value) > 3:
            raise serializers.ValidationError(
                'A descrição não pode ter menos que 3 caracteres'
            )
        return value

    def validate_date(self, value):
        today = date.today()
        if value < today:
            raise serializers.ValidationError(
                'A data marcada não pode ser menor que a data atual'
            )
        return value

    def validate(self, data):
        validated_data = super().validate(data)
        if validated_data['start_time'] >= validated_data['end_time']:
            raise serializers.ValidationError(
             "A hora de Termino não pode ser maior nem igual que a hora de inicio"
            )
        return validated_data

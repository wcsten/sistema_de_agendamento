import pytest
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from schedule.models import Patient, Procedure, Schedule


pytestmark = pytest.mark.django_db


def test_create_patient_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('patient-list')  # GET list POST create
    # url = reverse('patient-detail') # PUT alterar, GET detail, DELETE (passar ID)

    payload = {
        'name': 'Vladimir',
        'email': 'vladimir@hotmail.com'
    }
    assert Patient.objects.all().count() == 0

    response = client.post(url, data=payload, format='json')
    assert response.status_code == 201

    assert Patient.objects.all().count() == 1


def test_create_patient_error():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('patient-list')

    payload = [{
        'name': 'Vladimir',
        'email': 'gabriel@hotmail.com'
    },
        {
        'name': 'Gabriel',
        'email': 'gabriel_sten@hotmail.com'

    }
    ]
    assert Patient.objects.all().count() == 0

    response = client.post(url, data=payload, format='json')
    assert response.status_code == 400

    assert Patient.objects.all().count() == 0


def test_list_patient_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('patient-list')

    response = client.get(url)
    assert response.status_code == 200


def test_put_patient_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    patient = Patient(name='Gabriel', email='gabriel_sten@hotmail.com')
    patient.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('patient-detail', [patient.id])

    payload = {
        'name': 'Joao',
        'email': 'joao@joao.com'
    }

    response = client.put(url, data=payload, format='json')
    assert response.status_code == 200


def test_delete_patient_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    patient = Patient(name='gabriel', email='gabriel_sten@hotmail.com')
    patient.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('patient-detail', args=[patient.id])

    response = client.delete(url)

    assert response.status_code == 204


def test_create_procedure_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('procedure-list')

    payload = {
        "name": "Raio-x",
        "description": "Raio-x da perna."
    }
    assert Procedure.objects.all().count() == 0

    response = client.post(url, data=payload, format='json')
    assert response.status_code == 201

    assert Procedure.objects.all().count() == 1


def test_list_procedure_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('procedure-list')

    response = client.get(url)
    assert response.status_code == 200


def test_put_procedure_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    procedure = Procedure(name='Exame de Sangue',
                          description='12 horas de jejum')
    procedure.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('procedure-detail', [procedure.id])

    payload = {
        'name': 'Exame de Urina',
        'description': 'Primeira urina do dia'
    }

    response = client.put(url, data=payload, format='json')
    assert response.status_code == 200


def test_delete_procedure_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    procedure = Procedure(name='Raio-x', description='Raio-x da Perna')
    procedure.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('procedure-detail', args=[procedure.id])

    response = client.delete(url)

    assert response.status_code == 204


def test_create_schedule_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    patient = Patient(name='Gabriel', email='gabriel_sten@hotmail.com')
    patient.save()

    procedure = Procedure(name='Exame de sangue',
                          description='12 horas de jejum')
    procedure.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('schedule-list')

    payload = {
        "detail": "exame do gabriel",
        "patient": patient.id,
        "procedure": [procedure.id],
        "date": "2017-12-14",
        "start_time": "14:00:00",
        "end_time": "15:00:00"
    }

    assert Schedule.objects.all().count() == 0

    response = client.post(url, data=payload, format='json')

    assert response.status_code == 201

    assert Schedule.objects.all().count() == 1


def test_create_schedule_error():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    patient = Patient(name='Gabriel', email='gabriel_sten@hotmail.com')
    patient.save()

    procedure = Procedure(name='Exame de sangue',
                          description='12 horas de jejum')
    procedure.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('schedule-list')

    payload = {
        "detail": "exame do gabriel",
        "patient": patient.id,
        "procedure": [procedure.id],
        "date": "2017-12-14",
        "start_time": "15:00:00",
        "end_time": "14:00:00"
    }

    assert Schedule.objects.all().count() == 0

    response = client.post(url, data=payload, format='json')

    assert response.status_code == 400

    assert Schedule.objects.all().count() == 0


def test_list_schedule_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('procedure-list')

    response = client.get(url)
    assert response.status_code == 200


def test_put_schedule_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    patient = Patient(name='Gabriel', email='gabriel_sten@hotmail.com')
    patient.save()

    procedure = Procedure(name='Raio-x', description='Raio-x da Perna')
    procedure.save()

    schedule = Schedule(
        patient=patient,
        detail='Exame do Gabriel',
        date='2017-12-16',
        start_time='15:00:00',
        end_time='16:00:00'
    )
    schedule.save()
    schedule.procedure.add(procedure)
    schedule.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('schedule-detail', [schedule.id])

    payload = {
        "detail": "Exame do Jorge",
        "patient": patient.id,
        "procedure": [procedure.id],
        "date": "2018-12-20",
        "start_time": "20:00:00",
        "end_time": "22:00:00"
    }

    response = client.put(url, data=payload, format='json')
    assert response.status_code == 200


def test_delete_schedule_success():
    user = User(username='gabriel')
    user.set_password('teste')
    user.is_superuser = True
    user.is_staff = True
    user.save()

    patient = Patient(name='Gabriel', email='gabriel_sten@hotmail.com')
    patient.save()

    procedure = Procedure(name='Raio-x', description='Raio-x da Perna')
    procedure.save()

    schedule = Schedule(
        patient=patient,
        detail='Exame do Gabriel',
        date='2017-12-16',
        start_time='15:00:00',
        end_time='16:00:00'
    )
    schedule.save()
    schedule.procedure.add(procedure)
    schedule.save()

    client = APIClient()
    client.login(username='gabriel', password='teste')

    url = reverse('schedule-detail', args=[schedule.id])

    response = client.delete(url)

    assert response.status_code == 204

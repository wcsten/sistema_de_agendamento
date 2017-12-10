from rest_framework.test import APIClient
from django.urls import reverse


def test_create_patient_success():
    client = APIClient()
    url = reverse('pattients')

    payload = {
        'name': 'Bla',
        'email': 'bla@bla.com'
    }

    client.post(url, data=payload, format='json')

import json
from rest_framework import status
from django.test import TestCase
from django.urls import include, path, reverse
from App.Voluntario.models import Voluntario
from App.Voluntario.api.serializers import VoluntarioSerializer


class VoluntarioTests(TestCase):
    """ 
        Testando o método GET, 
        para obter todos os registros
    """

    def setUp(self):
        Voluntario.objects.create(
            nome= 'Wendrew',
            sobrenome= 'Oliveira',
            bairro= 'Vila Virginia',
            cidade= 'Ribeirão Preto',
        )

    def test_get_all_voluntarios(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/voluntarios/')
        voluntarios = Voluntario.objects.all()
        serializer = VoluntarioSerializer(voluntarios, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleVoluntarioTest(TestCase):
    """ 
        Testando metodo GET, 
        passando a ID especifica de um registro.
    """

    def setUp(self):
        self.wendrew = Voluntario.objects.create(
            nome= 'Wendrew',
            sobrenome= 'Oliveira',
            bairro= 'Vila Virginia',
            cidade= 'Ribeirão Preto',
        )
        self.oliver = Voluntario.objects.create(
            nome= 'Oliver',
            sobrenome= 'Oliveira',
            bairro= 'Vila Virginia',
            cidade= 'Ribeirão Preto',
        )

    def test_get_valid_single_voluntario(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/voluntarios/', 
            kwargs={'pk': self.wendrew.pk}
        )
        voluntario = Voluntario.objects.get(pk=self.wendrew.pk)
        serializer = VoluntarioSerializer(voluntario)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_voluntario(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/voluntarios/30/'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewVoluntarioTest(TestCase):
    """ 
        Testando o método POST
    """

    def setUp(self):
        self.valid_payload = {
            'nome': 'Wendrew',
            'sobrenome': 'Oliveira',
            'bairro': 'Vila Virginia',
            'cidade': 'Ribeirão Preto',
        }
        self.invalid_payload = {
            'nome': '',
            'sobrenome': '',
            'bairro': '',
            'cidade': '',
        }

    def test_create_valid_voluntario(self):
        response = self.client.post(
            'http://127.0.0.1:8000/api/v1/voluntarios/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_voluntario(self):
        response = self.client.post(
            'http://127.0.0.1:8000/api/v1/voluntarios/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
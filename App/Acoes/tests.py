import json
from rest_framework import status
from django.test import TestCase
from django.urls import include, path, reverse
from App.Acoes.models import Acao
from App.Acoes.api.serializers import AcaoSerializer


class AcoesTests(TestCase):
    """ 
        Testando o método GET, 
        para obter todos os registros
    """

    def setUp(self):
        Acao.objects.create(
            nome= 'Catadores de lixo eletronico',
            instituicao= 'Lixotronics',
            cidade= 'Ribeirão Preto',
            bairro= 'Vila Virginia',
            endereco= 'Visconde de Inhomerim 323',
            descricao= 'Todo sabado às 8hrs',
        )

    def test_get_all_acoes(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/acoes/')
        acoes = Acao.objects.all()
        serializer = AcaoSerializer(acoes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleAcoesTest(TestCase):
    """ 
        Testando metodo GET, 
        passando a ID especifica de um registro.
    """

    def setUp(self):
        self.lixotronics = Acao.objects.create(
            nome= 'Catadores de lixo eletronico',
            instituicao= 'Lixotronics',
            cidade= 'Ribeirão Preto',
            bairro= 'Vila Virginia',
            endereco= 'Visconde de Inhomerim 323',
            descricao= 'Todo sabado às 8hrs',
        )
        self.rpda = Acao.objects.create(
            nome= 'Reunião de programadores depressivos anonimos',
            instituicao= 'R.P.D.A',
            cidade= 'Ribeirão Preto',
            bairro= 'Vila Virginia',
            endereco= 'Visconde de Inhomerim 323',
            descricao= 'Todo domingo às 18hrs',
        )

    def test_get_valid_single_acoes(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/acoes/', 
            kwargs={'pk': self.lixotronics.pk}
        )
        Acoes = Acao.objects.get(pk=self.lixotronics.pk)
        serializer = AcaoSerializer(Acoes)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_acoes(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/acoes/30/'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewAcoesTest(TestCase):
    """ 
        Testando o método POST
    """

    def setUp(self):
        self.valid_payload = {
            'nome': 'Saltadores de distro anonimos',
            'instituicao': 'S.D.A',
            'cidade': 'Ribeirão Preto',
            'bairro': 'Vila Virginia',
            'endereco': 'Visconde de Inhomerim',
            'descricao': 'Grupo para quem muda de distro a cada semana',
        }
        self.invalid_payload = {
            'nome': '',
            'instituicao': '',
            'cidade': '',
            'bairro': '',
            'endereco': '',
            'descricao': '',
        }

    def test_create_valid_acoes(self):
        response = self.client.post(
            'http://127.0.0.1:8000/api/v1/acoes/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_acoes(self):
        response = self.client.post(
            'http://127.0.0.1:8000/api/v1/acoes/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
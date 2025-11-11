from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from http import HTTPStatus
from core.models import Agenda

class List_Contact_OK_Test(TestCase):
    def setUp(self):
        self.client = Client()

        # Cria usuário corretamente e já com senha
        self.user = User.objects.create_user(
            username='admin',
            email='admin@fatec.sp.gov.br',
            password='fatec'
        )

        self.login_url = reverse('login')
        self.list_url = reverse('show_contact')

        # Contato 1
        self.agenda = Agenda.objects.create(
            nome_completo='rafaela morais',
            telefone='19999999999',
            email='rafaela.morais2@fatec.sp.gov.br',
            observacao='teste'
        )

        # Contato 2 (dados diferentes para casar com asserções)
        self.agenda2 = Agenda.objects.create(
            nome_completo='rafaela morais1',
            telefone='19999999998',
            email='rafaela.lemes2@fatec.sp.gov.br',
            observacao='teste 2'
        )

    def test_Not_Logged_List_Template(self):
        response = self.client.get(self.list_url)
        self.assertNotEqual(response.status_code, HTTPStatus.OK)
        self.assertRedirects(response, f'{self.login_url}?next={self.list_url}')

    def test_Logged_List_Template(self):
        # Login padrão do Django: username + password
        self.client.login(username='admin', password='fatec')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'show_contact.html')

    def test_list_contacts(self):
        self.client.login(username='admin', password='fatec')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'show_contact.html')

        # Nomes
        self.assertContains(response, 'rafaela morais')
        self.assertContains(response, 'rafaela morais1')

        # Telefones
        self.assertContains(response, '19999999999')
        self.assertContains(response, '19999999998')

        # E-mails
        self.assertContains(response, 'rafaela.morais2@fatec.sp.gov.br')
        self.assertContains(response, 'rafaela.lemes2@fatec.sp.gov.br')

    def test_list_contacts_empty(self):
        self.client.login(username='admin', password='fatec')
        Agenda.objects.all().delete()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'show_contact.html')
        self.assertContains(response, 'Nenhum contato encontrado.')

        # Não deve conter dados de contatos
        self.assertNotContains(response, 'rafaela morais')
        self.assertNotContains(response, 'rafaela morais1')
        self.assertNotContains(response, '19999999999')
        self.assertNotContains(response, '19999999998')

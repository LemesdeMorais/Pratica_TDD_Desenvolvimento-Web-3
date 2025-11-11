from django.test import TestCase
from core.models import Agenda

class AgendaModelTest(TestCase):
    def setUp(self):
        self.agenda = Agenda.objects.create(
            nome_completo="Helena Lemes",
            telefone="(19) 000000000",
            email="helena.lemes@example.com",
            observacao="Cliente importante, prefere contato por e-mail."
        )

    def test_agenda_criada_com_sucesso(self):
        self.assertEqual(self.agenda.nome_completo, "Helena Lemes")
        self.assertEqual(self.agenda.telefone, "(19) 000000000")
        self.assertEqual(self.agenda.email, "helena.lemes@example.com")
        self.assertEqual(self.agenda.observacao, "Cliente importante, prefere contato por e-mail.")

    def test_str_retorna_nome_e_email(self):
        self.assertEqual(str(self.agenda), "Helena Lemes - helena.lemes@example.com")

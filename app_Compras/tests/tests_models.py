from django.test import TestCase
from app_Compras.models import *

class TestModels(TestCase):

    def testcreate(self):
        self.Clienteprueba = tblClientes.objects.create(
            id_cliente=1253,
            nombre="mel",
            apellido="mendo",
            factura="prueba"
        )
from django.test import TestCase, Client
from django.urls import reverse
from app_Compras.models import *

class TestViews(TestCase):
    
    def test_view(self):
        client = tblClientes()

        response = client.get(reverse('home'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'inicio2.html')
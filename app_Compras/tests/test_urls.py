from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_compras.views import*


class Testurls(SimpleTestCase):

    def tes_url(self):
        url= reverse('about2')
        print(resolve(url))
        self.assertEquals(resolve(url).func,acerca)
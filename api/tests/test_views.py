from collections import OrderedDict
from typing import List

from api.models import SomeModel
from django.test import TestCase, Client
from django.urls import reverse


class TestSomeModelViews(TestCase):
    @staticmethod
    def n_total(name=''):
        instances = SomeModel.objects.all()

        if len(name) > 0:
            instances = instances.filter(name=name)

        return instances.count()

    def setUp(self) -> None:
        self.client = Client()

        self.name = 'test'
        self.instance = SomeModel(name=self.name, amount=0, distance=0)
        self.instance.save()
        self.pk = self.instance.pk
        self.total_number = self.n_total()

    def test_some_model_list_GET(self):
        url = reverse('api:some_model_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 1)
        self.assertIsInstance(response.data['results'], List)
        self.assertIsInstance(response.data['results'][0], OrderedDict)
        self.assertEqual(response.data['results'][0]["id"], self.pk)

    def test_some_model_add_POST(self):
        url = reverse('api:some_model_create')
        name = 'test_add'
        n_total = self.n_total(name)
        amount = 999
        distance = 999
        response = self.client.post(url, {'name': name, 'amount': amount, 'distance': distance})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.total_number + 1, self.n_total())
        self.assertEqual(n_total + 1, self.n_total(name))
        self.assertEqual(name, SomeModel.objects.get(name=name).name)

    def test_some_model_delete_DELETE(self):
        url = reverse('api:some_model_delete', args=[self.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.total_number - 1, self.n_total())

    def test_some_model_put_PUT(self):
        name = 'test1'
        url = reverse('api:some_model_update', args=[self.pk])
        response = self.client.put(url, {
            "name": name,
            "amount": self.instance.amount,
            "distance": self.instance.distance,
            "date": self.instance.date
        }, content_type="application/json")

        instance = SomeModel.objects.get(pk=self.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.total_number, self.n_total())
        self.assertEqual(instance.name, name)




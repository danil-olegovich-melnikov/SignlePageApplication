from datetime import date

from django.test import TestCase

from api.models import SomeModel


# Create your tests here.
class TestModels(TestCase):
    def setUp(self) -> None:
        self.name = 'Test'
        self.date = date.today()
        self.amount = 1
        self.distance = 1
        self.instance_some_model = SomeModel(
            name=self.name,
            date=self.date,
            amount=self.amount,
            distance=self.distance
        )
        self.instance_some_model.save()

    def test_some_model_slug_test(self):
        self.assertEqual(self.instance_some_model.pk, 1)

    def test_some_model_fields(self):
        self.assertEqual(self.instance_some_model.name, self.name)
        self.assertEqual(self.instance_some_model.amount, self.amount)
        self.assertEqual(self.instance_some_model.distance, self.distance)
        self.assertEqual(self.instance_some_model.date, self.date)

    def test_some_model_default(self):
        instance_some_model1 = SomeModel(
            name=self.name,
            amount=self.amount,
            distance=self.distance
        )
        instance_some_model1.save()

        self.assertIsInstance(instance_some_model1.date, date)
        self.assertEqual(instance_some_model1.date, self.date)

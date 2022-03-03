from django.test import TestCase
from django.urls import reverse, resolve
from api.views import (
    SomeModelCreateApi,
    SomeModelListApi,
    SomeModelUpdateApi,
    SomeModelDeleteApi,
)


class TestUrls(TestCase):

    def test_some_model_list_url_resolve(self):
        url = reverse('api:some_model_list')
        self.assertEqual(resolve(url).func.view_class, SomeModelListApi)

    def test_some_model_delete_url_resolve(self):
        url = reverse('api:some_model_delete', args=[0])
        self.assertEqual(resolve(url).func.view_class, SomeModelDeleteApi)

    def test_some_model_add_url_resolve(self):
        url = reverse('api:some_model_create')
        self.assertEqual(resolve(url).func.view_class, SomeModelCreateApi)

    def test_some_model_put_url_resolve(self):
        url = reverse('api:some_model_update', args=[0])
        self.assertEqual(resolve(url).func.view_class, SomeModelUpdateApi)
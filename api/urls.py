from django.urls import path
from api.views import (
    SomeModelCreateApi,
    SomeModelListApi,
    SomeModelUpdateApi,
    SomeModelDeleteApi,
)

app_name = 'api'

urlpatterns = [
    path('some-model/create/', SomeModelCreateApi.as_view(), name='some_model_create'),
    path('some-model/', SomeModelListApi.as_view(), name='some_model_list'),
    path('some-model/update/<int:pk>', SomeModelUpdateApi.as_view(), name='some_model_update'),
    path('some-model/delete/<int:pk>', SomeModelDeleteApi.as_view(), name='some_model_delete'),

]
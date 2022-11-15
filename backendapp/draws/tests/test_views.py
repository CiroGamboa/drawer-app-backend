from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class DrawViewsTests(APITestCase):

    def setUp(self):
        with open("draws/tests/test_data/test_draw_payload.json") as p:
            payload = json.load(p)
        
        self.sample_valid_draw = {'title':'Sample Valid Title','payload': payload}
        self.sample_invalid_draw = {'title':'Sample Invalid Title','payload': {'foo':'d','bar':'d'}}


    def test_get_all_draw(self):
        pass

    def test_create_draw(self):
        '''
        '''

        response = self.client.post(reverse('draw_list'), self.sample_valid_draw, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('draw_list'), self.sample_invalid_draw, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_draw(self):
        pass

    def test_delete_draw(self):
        pass
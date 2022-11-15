from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

from ..models import Draw

#TODO: Make the repeated post request a general function

class DrawViewsTests(APITestCase):

    def setUp(self):
        with open("draws/tests/data/test_draw_payload.json") as p:
            payload = json.load(p)
        
        self.sample_valid_draw = {'title':'Sample Valid Title','payload': payload}
        self.sample_invalid_draw = {'title':'Sample Invalid Title','payload': {'foo':'d','bar':'d'}}


    def test_get_all_draws_success(self):
        '''
        Successfully retrieve a list with all the draws
        '''
        response = self.client.get(reverse('draw_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_create_draw_success(self):
        '''
        Successfully created a new draw on the database through the API
        '''
        previous_draws_count = Draw.objects.all().count()
        response = self.client.post(reverse('draw_list'), self.sample_valid_draw, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(previous_draws_count+1, Draw.objects.all().count())

    def test_create_draw_failed(self):
        '''
        The creation of a new draw on the database failed due to an invalid draw payload
        '''
        response = self.client.post(reverse('draw_list'), self.sample_invalid_draw, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_draw_success(self):
        '''
        Successfully updated a draw on the database through the API
        '''
        response = self.client.post(reverse('draw_list'), self.sample_valid_draw, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        draw_id = response.data['id']
        response2 = self.client.put(reverse('draw_detail', kwargs={'draw_id': str(draw_id)}), self.sample_valid_draw, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_delete_draw_success(self):
        '''
        Successfully deleted a draw on the database through the API
        '''
        response = self.client.post(reverse('draw_list'), self.sample_valid_draw, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        draw_id = response.data['id']
        response2 = self.client.delete(reverse('draw_detail', kwargs={'draw_id': str(draw_id)}))
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
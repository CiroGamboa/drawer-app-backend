from django.test import TestCase
from ..models import Draw
from ..validators import ValidationErrorTestMixin
import json

class DrawModelTests(ValidationErrorTestMixin, TestCase):

    def create_test_draw(self):
        '''
        Create a test object in the database
        '''
        with open("draws/tests/data/test_draw_payload.json") as p:
            payload = json.load(p)
        
        test_draw = Draw.objects.create(title='test', payload=payload)
        return test_draw

    def test_draw_creation_sucess(self):
        '''
        If the input data has the correct json schema and is inserted correctly
        in the database, the test object will be created
        '''
        test_draw = self.create_test_draw()
        self.assertTrue(isinstance(test_draw, Draw))
        self.assertEqual(test_draw.__str__(), test_draw.title)

    def test_payload_validation_failed(self):
        '''
        Test the draw payload input must have a certain data scheme, so when tested
        with other data scheme, it must raise a ValidationError. 
        '''

        payload = {'foo':'d','bar':'d'}
        test_draw = Draw(title='test', payload=payload)

        with self.assertValidationErrors(['payload']):
            test_draw.full_clean()





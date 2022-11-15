from django.test import TestCase
from .models import Draw
from .validators import ValidationErrorTestMixin
import json

class DrawModelTests(ValidationErrorTestMixin,TestCase):

    def create_test_draw(self):
        '''
        Create
        '''
        with open("draws/test_data/test_draw_payload.json") as p:
            payload = json.load(p)
        
        test_draw = Draw.objects.create(title='test', payload=payload)
        return test_draw

    def test_draw_creation(self):
        '''
        The validation worked
        '''
        test_draw = self.create_test_draw()
        self.assertTrue(isinstance(test_draw, Draw))
        self.assertEqual(test_draw.__str__(), test_draw.title)

    def test_payload_validation(self):
        '''
        Test the draw payload input, which must have a certain data layout (True), 
        otherwise the validator must raise a ValidationError. If the validator returns True,
        the draw must be saved to the database.
        '''

        payload = {'foo':'d','bar':'d'}
        test_draw = Draw(title='test', payload=payload)

        with self.assertValidationErrors(['payload']):
            test_draw.full_clean()





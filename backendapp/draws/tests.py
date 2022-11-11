from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Draw
from .validators import ValidationErrorTestMixin

class DrawModelTests(ValidationErrorTestMixin,TestCase):

    # Probar si el draw_payload trae bien el formato
    def test_draw_payload_validation(self):
        '''
        Test the draw payload input, which must have a certain data layout (True), 
        otherwise the validator must raise a ValidationError. If the validator returns True,
        the draw must be saved to the database.
        '''

        payload = {'foo':'d','bar':'d'}
        test_draw = Draw(draw_title='test', draw_payload=payload)

        with self.assertValidationErrors(['draw_payload']):
            test_draw.full_clean()


from django.core.exceptions import ValidationError
from contextlib import contextmanager

class ValidationErrorTestMixin(object):

    @contextmanager
    def assertValidationErrors(self, fields):
        """
        Assert that a validation error is raised, containing all the specified
        fields, and only the specified fields.
        """
        try:
            yield
            raise AssertionError("ValidationError not raised")
        except ValidationError as e:
            self.assertEqual(set(fields), set(e.message_dict.keys()))


def validate_draw_payload(draw_payload):
    '''
    Validate if the draw payload has the proper data layout.
    An example of the data layout is in test_data/drawExample.json
    '''
    print("Executiiinnnggg")
    print(draw_payload)
    if len(draw_payload) > 5:
        print("Inside")
        raise ValidationError("Invalid draw_payload")
    else:
        return draw_payload
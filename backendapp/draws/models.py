from django.db import models
from django_json_field_schema_validator.validators import JSONFieldSchemaValidator
import json

# Upload the draw payload schema for further validation
# This schema can be relocated to some general init logic
with open("draws/schemas/draw_payload_schema.json") as schema:
    draw_payload_schema = json.load(schema)

class Draw(models.Model):

    draw_title = models.CharField(
        max_length=200, 
        null=False, 
        blank=False)

    draw_payload = models.JSONField(
        null=False, 
        blank=False, 
        validators=[JSONFieldSchemaValidator(draw_payload_schema)])

    def __str__(self):
        return self.draw_title


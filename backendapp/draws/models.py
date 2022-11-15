from django.db import models
from django_json_field_schema_validator.validators import JSONFieldSchemaValidator
import json

# Upload the draw payload schema for validation
# This schema should be relocated to some general init logic
with open("draws/schemas/draw_payload_schema.json") as schema:
    payload_schema = json.load(schema)

class Draw(models.Model):

    title = models.CharField(
        max_length=200, 
        null=False, 
        blank=False)

    payload = models.JSONField(
        null=False, 
        blank=False, 
        validators=[JSONFieldSchemaValidator(payload_schema)])

    def __str__(self):
        return self.title


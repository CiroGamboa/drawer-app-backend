import json

with open("schemas/draw_payload_schema.json") as schema:
    draw_payload_schema = json.load(schema)

print(draw_payload_schema)
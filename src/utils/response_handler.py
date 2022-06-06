import jsonschema


def status_code(response):
    return str(response.status_code)


def validate_json(response, schema):
    jsonschema.validate(instance=response.json(), schema=schema)
    return True

import os.path
import sys
import jsonschema
import yaml

with open(os.path.join(os.path.dirname(__file__),
                       'manifest-schema.yaml'), 'r') as f:
    SCHEMA = yaml.load(f)


def validate(manifest):
    return jsonschema.validate(manifest, SCHEMA)

if __name__ == '__main__':
    manifest = yaml.load(sys.stdin.read())
    validate(manifest)

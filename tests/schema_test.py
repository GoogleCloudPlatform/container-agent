#!/usr/bin/python

"""Tests for schema validattion."""

import unittest
import jsonschema
import yaml
from container_agent import schema


class SchemaTest(unittest.TestCase):
    def test_validateGood(self):
        with open('manifests/example.yaml') as f:
            manifest = yaml.load(f.read())
        schema.validate(manifest)

    def test_validateBad(self):
        manifest = {}
        self.assertRaises(jsonschema.ValidationError,
                          schema.validate, manifest)
        manifest = {
            'version': 1
            }
        self.assertRaises(jsonschema.ValidationError,
                          schema.validate, manifest)
        manifest = {
            'version': 'v1beta2'
            }
        self.assertRaises(jsonschema.ValidationError,
                          schema.validate, manifest)
        manifest = {
            'version': '1',
            'containers': [{
                'image': 'foo'
                }]
            }
        self.assertRaises(jsonschema.ValidationError,
                          schema.validate, manifest)

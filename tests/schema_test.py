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

    def test_ignoreUnknownAttributes(self):
        manifest = {
            'version': 'v1beta1',
            'unknown': 'attribute',
            'containers': [{
                'name': 'foo1',
                'image': 'foo',
                'unknown': 'attribute'
                }]
            }
        schema.validate(manifest)

    def test_validateBadVersion(self):
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

    def test_validateBadContainer(self):
        manifest = {
            'version': 'v1beta1',
            'containers': [{
                'image': 'foo'
                }]
            }
        self.assertRaises(jsonschema.ValidationError,
                          schema.validate, manifest)

    def test_validateBadVolume(self):
        manifest = {
            'version': 'v1beta1',
            'volumes': [{}]
            }
        self.assertRaises(jsonschema.ValidationError,
                          schema.validate, manifest)
        manifest = {
            'version': 'v1beta1',
            'volumes': [{'name': '1-bad-volume-name'}]
            }
        self.assertRaises(jsonschema.ValidationError,
                          schema.validate, manifest)
        manifest = {
            'version': 'v1beta1',
            'volumes': [
                {'name': 'duplicate-volume-name'},
                {'name': 'duplicate-volume-name'}
            ]}
        self.assertRaises(jsonschema.ValidationError,
                          schema.validate, manifest)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-06-22.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import documentreference
from fhirdate import FHIRDate


class DocumentReferenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DocumentReference", js["resourceType"])
        return documentreference.DocumentReference(js)
    
    def testDocumentReference1(self):
        inst = self.instantiate_from("documentreference-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentReference instance")
        self.implDocumentReference1(inst)
        
        js = inst.as_json()
        self.assertEqual("DocumentReference", js["resourceType"])
        inst2 = documentreference.DocumentReference(js)
        self.implDocumentReference1(inst2)
    
    def implDocumentReference1(self, inst):
        self.assertEqual(inst.confidentiality[0].coding[0].code, "1.3.6.1.4.1.21367.2006.7.101")
        self.assertEqual(inst.confidentiality[0].coding[0].display, "Clinical-Staff")
        self.assertEqual(inst.confidentiality[0].coding[0].system, "http://ihe.net/xds/connectathon/confidentialityCodes")
        self.assertEqual(inst.content[0].contentType, "application/hl7-v3+xml")
        self.assertEqual(inst.content[0].hash, "2jmj7l5rSw0yVb/vlWAYkK/YBwk=")
        self.assertEqual(inst.content[0].language, "en-US")
        self.assertEqual(inst.content[0].size, 3654)
        self.assertEqual(inst.content[0].url, "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510")
        self.assertEqual(inst.context.event[0].coding[0].code, "T-D8200")
        self.assertEqual(inst.context.event[0].coding[0].display, "Arm")
        self.assertEqual(inst.context.event[0].coding[0].system, "http://ihe.net/xds/connectathon/eventCodes")
        self.assertEqual(inst.context.facilityType.coding[0].code, "Outpatient")
        self.assertEqual(inst.context.facilityType.coding[0].display, "Outpatient")
        self.assertEqual(inst.context.facilityType.coding[0].system, "http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes")
        self.assertEqual(inst.context.period.end.date, FHIRDate("2004-12-23T08:01:00+11:00").date)
        self.assertEqual(inst.context.period.end.as_json(), "2004-12-23T08:01:00+11:00")
        self.assertEqual(inst.context.period.start.date, FHIRDate("2004-12-23T08:00:00+11:00").date)
        self.assertEqual(inst.context.period.start.as_json(), "2004-12-23T08:00:00+11:00")
        self.assertEqual(inst.created.date, FHIRDate("2005-12-24T09:35:00+11:00").date)
        self.assertEqual(inst.created.as_json(), "2005-12-24T09:35:00+11:00")
        self.assertEqual(inst.description, "Physical")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.indexed.date, FHIRDate("2005-12-24T09:43:41+11:00").date)
        self.assertEqual(inst.indexed.as_json(), "2005-12-24T09:43:41+11:00")
        self.assertEqual(inst.klass.coding[0].code, "History and Physical")
        self.assertEqual(inst.klass.coding[0].display, "History and Physical")
        self.assertEqual(inst.klass.coding[0].system, "http://ihe.net/xds/connectathon/classCodes")
        self.assertEqual(inst.masterIdentifier.system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.masterIdentifier.value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "34108-1")
        self.assertEqual(inst.type.coding[0].display, "Outpatient Note")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")


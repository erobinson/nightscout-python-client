# coding: utf-8

"""
    Nightscout API

    Own your DData with the Nightscout API  # noqa: E501

    OpenAPI spec version: 14.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import nightscout_python_client
from nightscout_python_client.api.treatments_api import TreatmentsApi  # noqa: E501
from nightscout_python_client.rest import ApiException


class TestTreatmentsApi(unittest.TestCase):
    """TreatmentsApi unit test stubs"""

    def setUp(self):
        self.api = TreatmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_treatments(self):
        """Test case for add_treatments

        Add new treatments.  # noqa: E501
        """
        pass

    def test_remove(self):
        """Test case for remove

        Delete treatments matching query.  # noqa: E501
        """
        pass

    def test_treatments_get(self):
        """Test case for treatments_get

        Treatments  # noqa: E501
        """
        pass

    def test_treatments_spec_delete(self):
        """Test case for treatments_spec_delete

        Delete treatments record with id provided in spec  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
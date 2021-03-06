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
from nightscout_python_client.api.devicestatus_api import DevicestatusApi  # noqa: E501
from nightscout_python_client.rest import ApiException


class TestDevicestatusApi(unittest.TestCase):
    """DevicestatusApi unit test stubs"""

    def setUp(self):
        self.api = DevicestatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_devicestatuses(self):
        """Test case for add_devicestatuses

        Add new devicestatus records.  # noqa: E501
        """
        pass

    def test_devicestatus_delete(self):
        """Test case for devicestatus_delete

        Delete all Devicestatus records matching query  # noqa: E501
        """
        pass

    def test_devicestatus_get(self):
        """Test case for devicestatus_get

        All Devicestatuses matching query  # noqa: E501
        """
        pass

    def test_devicestatus_spec_delete(self):
        """Test case for devicestatus_spec_delete

        Delete devicestatus record with id provided in spec  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

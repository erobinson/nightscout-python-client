# coding: utf-8

"""
    Nightscout API

    Own your DData with the Nightscout API  # noqa: E501

    OpenAPI spec version: 14.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Devicestatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'device': 'str',
        'created_at': 'str',
        'openaps': 'str',
        'loop': 'str',
        'pump': 'Pump',
        'uploader': 'Uploader',
        'xdripjs': 'Xdripjs'
    }

    attribute_map = {
        'device': 'device',
        'created_at': 'created_at',
        'openaps': 'openaps',
        'loop': 'loop',
        'pump': 'pump',
        'uploader': 'uploader',
        'xdripjs': 'xdripjs'
    }

    def __init__(self, device=None, created_at=None, openaps=None, loop=None, pump=None, uploader=None, xdripjs=None):  # noqa: E501
        """Devicestatus - a model defined in Swagger"""  # noqa: E501
        self._device = None
        self._created_at = None
        self._openaps = None
        self._loop = None
        self._pump = None
        self._uploader = None
        self._xdripjs = None
        self.discriminator = None
        self.device = device
        self.created_at = created_at
        if openaps is not None:
            self.openaps = openaps
        if loop is not None:
            self.loop = loop
        if pump is not None:
            self.pump = pump
        if uploader is not None:
            self.uploader = uploader
        if xdripjs is not None:
            self.xdripjs = xdripjs

    @property
    def device(self):
        """Gets the device of this Devicestatus.  # noqa: E501

        Device type and hostname for example openaps://hostname  # noqa: E501

        :return: The device of this Devicestatus.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this Devicestatus.

        Device type and hostname for example openaps://hostname  # noqa: E501

        :param device: The device of this Devicestatus.  # noqa: E501
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def created_at(self):
        """Gets the created_at of this Devicestatus.  # noqa: E501

        dateString, prefer ISO `8601`  # noqa: E501

        :return: The created_at of this Devicestatus.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Devicestatus.

        dateString, prefer ISO `8601`  # noqa: E501

        :param created_at: The created_at of this Devicestatus.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def openaps(self):
        """Gets the openaps of this Devicestatus.  # noqa: E501

        OpenAPS devicestatus record - TODO: Fill Out Details  # noqa: E501

        :return: The openaps of this Devicestatus.  # noqa: E501
        :rtype: str
        """
        return self._openaps

    @openaps.setter
    def openaps(self, openaps):
        """Sets the openaps of this Devicestatus.

        OpenAPS devicestatus record - TODO: Fill Out Details  # noqa: E501

        :param openaps: The openaps of this Devicestatus.  # noqa: E501
        :type: str
        """

        self._openaps = openaps

    @property
    def loop(self):
        """Gets the loop of this Devicestatus.  # noqa: E501

        Loop devicestatus record - TODO: Fill Out Details  # noqa: E501

        :return: The loop of this Devicestatus.  # noqa: E501
        :rtype: str
        """
        return self._loop

    @loop.setter
    def loop(self, loop):
        """Sets the loop of this Devicestatus.

        Loop devicestatus record - TODO: Fill Out Details  # noqa: E501

        :param loop: The loop of this Devicestatus.  # noqa: E501
        :type: str
        """

        self._loop = loop

    @property
    def pump(self):
        """Gets the pump of this Devicestatus.  # noqa: E501


        :return: The pump of this Devicestatus.  # noqa: E501
        :rtype: Pump
        """
        return self._pump

    @pump.setter
    def pump(self, pump):
        """Sets the pump of this Devicestatus.


        :param pump: The pump of this Devicestatus.  # noqa: E501
        :type: Pump
        """

        self._pump = pump

    @property
    def uploader(self):
        """Gets the uploader of this Devicestatus.  # noqa: E501


        :return: The uploader of this Devicestatus.  # noqa: E501
        :rtype: Uploader
        """
        return self._uploader

    @uploader.setter
    def uploader(self, uploader):
        """Sets the uploader of this Devicestatus.


        :param uploader: The uploader of this Devicestatus.  # noqa: E501
        :type: Uploader
        """

        self._uploader = uploader

    @property
    def xdripjs(self):
        """Gets the xdripjs of this Devicestatus.  # noqa: E501


        :return: The xdripjs of this Devicestatus.  # noqa: E501
        :rtype: Xdripjs
        """
        return self._xdripjs

    @xdripjs.setter
    def xdripjs(self, xdripjs):
        """Sets the xdripjs of this Devicestatus.


        :param xdripjs: The xdripjs of this Devicestatus.  # noqa: E501
        :type: Xdripjs
        """

        self._xdripjs = xdripjs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Devicestatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Devicestatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

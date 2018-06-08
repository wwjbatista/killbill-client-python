# coding: utf-8

#
# Copyright 2014-2017 Groupon, Inc.
# Copyright 2014-2017 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.19.17-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class PluginProperty(object):
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
        'key': 'Str',
        'value': 'Str',
        'is_updatable': 'Bool'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'is_updatable': 'isUpdatable'
    }

    def __init__(self, key=None, value=None, is_updatable=False):  # noqa: E501
        """PluginProperty - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._value = None
        self._is_updatable = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if is_updatable is not None:
            self.is_updatable = is_updatable

    @property
    def key(self):
        """Gets the key of this PluginProperty.  # noqa: E501


        :return: The key of this PluginProperty.  # noqa: E501
        :rtype: Str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PluginProperty.


        :param key: The key of this PluginProperty.  # noqa: E501
        :type: Str
        """


        self._key = key

    @property
    def value(self):
        """Gets the value of this PluginProperty.  # noqa: E501


        :return: The value of this PluginProperty.  # noqa: E501
        :rtype: Str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PluginProperty.


        :param value: The value of this PluginProperty.  # noqa: E501
        :type: Str
        """


        self._value = value

    @property
    def is_updatable(self):
        """Gets the is_updatable of this PluginProperty.  # noqa: E501


        :return: The is_updatable of this PluginProperty.  # noqa: E501
        :rtype: Bool
        """
        return self._is_updatable

    @is_updatable.setter
    def is_updatable(self, is_updatable):
        """Sets the is_updatable of this PluginProperty.


        :param is_updatable: The is_updatable of this PluginProperty.  # noqa: E501
        :type: Bool
        """


        self._is_updatable = is_updatable

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PluginProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

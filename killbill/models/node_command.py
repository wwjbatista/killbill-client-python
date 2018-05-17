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

    OpenAPI spec version: 0.19.15-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class NodeCommand(object):
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
        'is_system_command_type': 'Bool',
        'node_command_type': 'Str',
        'node_command_properties': 'List[NodeCommandProperty]'
    }

    attribute_map = {
        'is_system_command_type': 'isSystemCommandType',
        'node_command_type': 'nodeCommandType',
        'node_command_properties': 'nodeCommandProperties'
    }

    def __init__(self, is_system_command_type=False, node_command_type=None, node_command_properties=None):  # noqa: E501
        """NodeCommand - a model defined in Swagger"""  # noqa: E501

        self._is_system_command_type = None
        self._node_command_type = None
        self._node_command_properties = None
        self.discriminator = None

        if is_system_command_type is not None:
            self.is_system_command_type = is_system_command_type
        if node_command_type is not None:
            self.node_command_type = node_command_type
        if node_command_properties is not None:
            self.node_command_properties = node_command_properties

    @property
    def is_system_command_type(self):
        """Gets the is_system_command_type of this NodeCommand.  # noqa: E501


        :return: The is_system_command_type of this NodeCommand.  # noqa: E501
        :rtype: Bool
        """
        return self._is_system_command_type

    @is_system_command_type.setter
    def is_system_command_type(self, is_system_command_type):
        """Sets the is_system_command_type of this NodeCommand.


        :param is_system_command_type: The is_system_command_type of this NodeCommand.  # noqa: E501
        :type: Bool
        """


        self._is_system_command_type = is_system_command_type

    @property
    def node_command_type(self):
        """Gets the node_command_type of this NodeCommand.  # noqa: E501


        :return: The node_command_type of this NodeCommand.  # noqa: E501
        :rtype: Str
        """
        return self._node_command_type

    @node_command_type.setter
    def node_command_type(self, node_command_type):
        """Sets the node_command_type of this NodeCommand.


        :param node_command_type: The node_command_type of this NodeCommand.  # noqa: E501
        :type: Str
        """


        self._node_command_type = node_command_type

    @property
    def node_command_properties(self):
        """Gets the node_command_properties of this NodeCommand.  # noqa: E501


        :return: The node_command_properties of this NodeCommand.  # noqa: E501
        :rtype: List[NodeCommandProperty]
        """
        return self._node_command_properties

    @node_command_properties.setter
    def node_command_properties(self, node_command_properties):
        """Sets the node_command_properties of this NodeCommand.


        :param node_command_properties: The node_command_properties of this NodeCommand.  # noqa: E501
        :type: List[NodeCommandProperty]
        """


        self._node_command_properties = node_command_properties

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
        if not isinstance(other, NodeCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

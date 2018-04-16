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

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import killbill
from api.nodes_info_api import NodesInfoApi  # noqa: E501
from killbill.rest import ApiException


class TestNodesInfoApi(unittest.TestCase):
    """NodesInfoApi unit test stubs"""

    def setUp(self):
        self.api = api.nodes_info_api.NodesInfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_nodes_info(self):
        """Test case for get_nodes_info

        Retrieve all the nodes infos  # noqa: E501
        """
        pass

    def test_trigger_node_command(self):
        """Test case for trigger_node_command

        Trigger a node command  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

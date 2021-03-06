# coding: utf-8

"""
    Social Graph API

    Pho Networks REST API

    OpenAPI spec version: 1.1.1
    Contact: emre@phonetworks.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import pho_client
from pho_client.rest import ApiException
from pho_client.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = pho_client.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_add_attribute(self):
        """
        Test case for add_attribute

        updates (or creates) an attribute
        """
        pass

    def test_del_attribute(self):
        """
        Test case for del_attribute

        deletes an attribute
        """
        pass

    def test_del_entity(self):
        """
        Test case for del_entity

        deletes an entity
        """
        pass

    def test_get_all_edges(self):
        """
        Test case for get_all_edges

        retrieves the edges of a node
        """
        pass

    def test_get_attribute(self):
        """
        Test case for get_attribute

        retrieves the value of an entity attribute
        """
        pass

    def test_get_attributes(self):
        """
        Test case for get_attributes

        retrieves the existing attribute keys of an entity (edge or node)
        """
        pass

    def test_get_edge(self):
        """
        Test case for get_edge

        retrieves an edge
        """
        pass

    def test_get_edge_getters(self):
        """
        Test case for get_edge_getters

        retrieves the edge getter methods of a node
        """
        pass

    def test_get_edge_setters(self):
        """
        Test case for get_edge_setters

        retrieves the edge setter methods of a node
        """
        pass

    def test_get_founder(self):
        """
        Test case for get_founder

        retrieves the Graph Founder
        """
        pass

    def test_get_graph(self):
        """
        Test case for get_graph

        retrieves the main Graph
        """
        pass

    def test_get_incoming_edges(self):
        """
        Test case for get_incoming_edges

        retrieves the incoming edges of a node
        """
        pass

    def test_get_node(self):
        """
        Test case for get_node

        retrieves a node
        """
        pass

    def test_get_node_edge(self):
        """
        Test case for get_node_edge

        edge getter
        """
        pass

    def test_get_outgoing_edges(self):
        """
        Test case for get_outgoing_edges

        retrieves the outgoing edges of a node
        """
        pass

    def test_get_space(self):
        """
        Test case for get_space

        retrieves the Space
        """
        pass

    def test_get_type(self):
        """
        Test case for get_type

        fetches entity type
        """
        pass

    def test_make_actor(self):
        """
        Test case for make_actor

        creates an Actor object
        """
        pass

    def test_make_edge(self):
        """
        Test case for make_edge

        creates an edge
        """
        pass

    def test_set_attribute(self):
        """
        Test case for set_attribute

        updates (or creates) an attribute
        """
        pass


if __name__ == '__main__':
    unittest.main()

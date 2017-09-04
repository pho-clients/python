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

from pprint import pformat
from six import iteritems
import re


class Edge(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, head=None, tail=None, _class=None):
        """
        Edge - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'head': 'str',
            'tail': 'str',
            '_class': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'head': 'head',
            'tail': 'tail',
            '_class': 'class'
        }

        self._id = id
        self._head = head
        self._tail = tail
        self.__class = _class


    @property
    def id(self):
        """
        Gets the id of this Edge.


        :return: The id of this Edge.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Edge.


        :param id: The id of this Edge.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def head(self):
        """
        Gets the head of this Edge.


        :return: The head of this Edge.
        :rtype: str
        """
        return self._head

    @head.setter
    def head(self, head):
        """
        Sets the head of this Edge.


        :param head: The head of this Edge.
        :type: str
        """
        if head is None:
            raise ValueError("Invalid value for `head`, must not be `None`")

        self._head = head

    @property
    def tail(self):
        """
        Gets the tail of this Edge.


        :return: The tail of this Edge.
        :rtype: str
        """
        return self._tail

    @tail.setter
    def tail(self, tail):
        """
        Sets the tail of this Edge.


        :param tail: The tail of this Edge.
        :type: str
        """
        if tail is None:
            raise ValueError("Invalid value for `tail`, must not be `None`")

        self._tail = tail

    @property
    def _class(self):
        """
        Gets the _class of this Edge.


        :return: The _class of this Edge.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """
        Sets the _class of this Edge.


        :param _class: The _class of this Edge.
        :type: str
        """

        self.__class = _class

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

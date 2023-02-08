# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.18.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class CreatePullReviewComment(object):
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
        "body": "str",
        "new_position": "int",
        "old_position": "int",
        "path": "str",
    }

    attribute_map = {
        "body": "body",
        "new_position": "new_position",
        "old_position": "old_position",
        "path": "path",
    }

    def __init__(
        self,
        body=None,
        new_position=None,
        old_position=None,
        path=None,
        _configuration=None,
    ):  # noqa: E501
        """CreatePullReviewComment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._new_position = None
        self._old_position = None
        self._path = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if new_position is not None:
            self.new_position = new_position
        if old_position is not None:
            self.old_position = old_position
        if path is not None:
            self.path = path

    @property
    def body(self):
        """Gets the body of this CreatePullReviewComment.  # noqa: E501


        :return: The body of this CreatePullReviewComment.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreatePullReviewComment.


        :param body: The body of this CreatePullReviewComment.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def new_position(self):
        """Gets the new_position of this CreatePullReviewComment.  # noqa: E501

        if comment to new file line or 0  # noqa: E501

        :return: The new_position of this CreatePullReviewComment.  # noqa: E501
        :rtype: int
        """
        return self._new_position

    @new_position.setter
    def new_position(self, new_position):
        """Sets the new_position of this CreatePullReviewComment.

        if comment to new file line or 0  # noqa: E501

        :param new_position: The new_position of this CreatePullReviewComment.  # noqa: E501
        :type: int
        """

        self._new_position = new_position

    @property
    def old_position(self):
        """Gets the old_position of this CreatePullReviewComment.  # noqa: E501

        if comment to old file line or 0  # noqa: E501

        :return: The old_position of this CreatePullReviewComment.  # noqa: E501
        :rtype: int
        """
        return self._old_position

    @old_position.setter
    def old_position(self, old_position):
        """Sets the old_position of this CreatePullReviewComment.

        if comment to old file line or 0  # noqa: E501

        :param old_position: The old_position of this CreatePullReviewComment.  # noqa: E501
        :type: int
        """

        self._old_position = old_position

    @property
    def path(self):
        """Gets the path of this CreatePullReviewComment.  # noqa: E501

        the tree path  # noqa: E501

        :return: The path of this CreatePullReviewComment.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CreatePullReviewComment.

        the tree path  # noqa: E501

        :param path: The path of this CreatePullReviewComment.  # noqa: E501
        :type: str
        """

        self._path = path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CreatePullReviewComment, dict):
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
        if not isinstance(other, CreatePullReviewComment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreatePullReviewComment):
            return True

        return self.to_dict() != other.to_dict()

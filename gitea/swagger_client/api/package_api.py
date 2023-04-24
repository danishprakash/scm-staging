# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated
from typing import overload, Optional, Union, Awaitable

from pydantic import Field, StrictInt, StrictStr

from typing import List, Optional

from swagger_client.models.package import Package
from swagger_client.models.package_file import PackageFile

from swagger_client.api_client import ApiClient
from swagger_client.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class PackageApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def delete_package(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @overload
    def delete_package(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        async_req: Optional[bool] = True,
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @validate_arguments
    def delete_package(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[None, Awaitable[None]]:  # noqa: E501
        """Delete a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_package(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param owner: owner of the package (required)
        :type owner: str
        :param type: type of the package (required)
        :type type: str
        :param name: name of the package (required)
        :type name: str
        :param version: version of the package (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.delete_package_with_http_info(
            owner, type, name, version, **kwargs
        )  # noqa: E501

    @validate_arguments
    def delete_package_with_http_info(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        **kwargs
    ):  # noqa: E501
        """Delete a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_package_with_http_info(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param owner: owner of the package (required)
        :type owner: str
        :param type: type of the package (required)
        :type type: str
        :param name: name of the package (required)
        :type name: str
        :param version: version of the package (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = ["owner", "type", "name", "version"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_package" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["owner"]:
            _path_params["owner"] = _params["owner"]

        if _params["type"]:
            _path_params["type"] = _params["type"]

        if _params["name"]:
            _path_params["name"] = _params["name"]

        if _params["version"]:
            _path_params["version"] = _params["version"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = [
            "TOTPHeader",
            "AuthorizationHeaderToken",
            "SudoHeader",
            "BasicAuth",
            "AccessToken",
            "SudoParam",
            "Token",
        ]  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/packages/{owner}/{type}/{name}/{version}",
            "DELETE",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @overload
    async def get_package(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        **kwargs
    ) -> Package:  # noqa: E501
        ...

    @overload
    def get_package(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        async_req: Optional[bool] = True,
        **kwargs
    ) -> Package:  # noqa: E501
        ...

    @validate_arguments
    def get_package(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[Package, Awaitable[Package]]:  # noqa: E501
        """Gets a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_package(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param owner: owner of the package (required)
        :type owner: str
        :param type: type of the package (required)
        :type type: str
        :param name: name of the package (required)
        :type name: str
        :param version: version of the package (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Package
        """
        kwargs["_return_http_data_only"] = True
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.get_package_with_http_info(
            owner, type, name, version, **kwargs
        )  # noqa: E501

    @validate_arguments
    def get_package_with_http_info(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        **kwargs
    ):  # noqa: E501
        """Gets a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_package_with_http_info(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param owner: owner of the package (required)
        :type owner: str
        :param type: type of the package (required)
        :type type: str
        :param name: name of the package (required)
        :type name: str
        :param version: version of the package (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Package, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["owner", "type", "name", "version"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_package" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["owner"]:
            _path_params["owner"] = _params["owner"]

        if _params["type"]:
            _path_params["type"] = _params["type"]

        if _params["name"]:
            _path_params["name"] = _params["name"]

        if _params["version"]:
            _path_params["version"] = _params["version"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = [
            "TOTPHeader",
            "AuthorizationHeaderToken",
            "SudoHeader",
            "BasicAuth",
            "AccessToken",
            "SudoParam",
            "Token",
        ]  # noqa: E501

        _response_types_map = {
            "200": "Package",
            "404": None,
        }

        return self.api_client.call_api(
            "/packages/{owner}/{type}/{name}/{version}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @overload
    async def list_package_files(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        **kwargs
    ) -> List[PackageFile]:  # noqa: E501
        ...

    @overload
    def list_package_files(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        async_req: Optional[bool] = True,
        **kwargs
    ) -> List[PackageFile]:  # noqa: E501
        ...

    @validate_arguments
    def list_package_files(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[List[PackageFile], Awaitable[List[PackageFile]]]:  # noqa: E501
        """Gets all files of a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_package_files(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param owner: owner of the package (required)
        :type owner: str
        :param type: type of the package (required)
        :type type: str
        :param name: name of the package (required)
        :type name: str
        :param version: version of the package (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PackageFile]
        """
        kwargs["_return_http_data_only"] = True
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.list_package_files_with_http_info(
            owner, type, name, version, **kwargs
        )  # noqa: E501

    @validate_arguments
    def list_package_files_with_http_info(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the package")],
        type: Annotated[StrictStr, Field(..., description="type of the package")],
        name: Annotated[StrictStr, Field(..., description="name of the package")],
        version: Annotated[StrictStr, Field(..., description="version of the package")],
        **kwargs
    ):  # noqa: E501
        """Gets all files of a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_package_files_with_http_info(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param owner: owner of the package (required)
        :type owner: str
        :param type: type of the package (required)
        :type type: str
        :param name: name of the package (required)
        :type name: str
        :param version: version of the package (required)
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[PackageFile], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["owner", "type", "name", "version"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_package_files" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["owner"]:
            _path_params["owner"] = _params["owner"]

        if _params["type"]:
            _path_params["type"] = _params["type"]

        if _params["name"]:
            _path_params["name"] = _params["name"]

        if _params["version"]:
            _path_params["version"] = _params["version"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = [
            "TOTPHeader",
            "AuthorizationHeaderToken",
            "SudoHeader",
            "BasicAuth",
            "AccessToken",
            "SudoParam",
            "Token",
        ]  # noqa: E501

        _response_types_map = {
            "200": "List[PackageFile]",
            "404": None,
        }

        return self.api_client.call_api(
            "/packages/{owner}/{type}/{name}/{version}/files",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @overload
    async def list_packages(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the packages")],
        page: Annotated[
            Optional[StrictInt],
            Field(description="page number of results to return (1-based)"),
        ] = None,
        limit: Annotated[
            Optional[StrictInt], Field(description="page size of results")
        ] = None,
        type: Annotated[
            Optional[StrictStr], Field(description="package type filter")
        ] = None,
        q: Annotated[Optional[StrictStr], Field(description="name filter")] = None,
        **kwargs
    ) -> List[Package]:  # noqa: E501
        ...

    @overload
    def list_packages(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the packages")],
        page: Annotated[
            Optional[StrictInt],
            Field(description="page number of results to return (1-based)"),
        ] = None,
        limit: Annotated[
            Optional[StrictInt], Field(description="page size of results")
        ] = None,
        type: Annotated[
            Optional[StrictStr], Field(description="package type filter")
        ] = None,
        q: Annotated[Optional[StrictStr], Field(description="name filter")] = None,
        async_req: Optional[bool] = True,
        **kwargs
    ) -> List[Package]:  # noqa: E501
        ...

    @validate_arguments
    def list_packages(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the packages")],
        page: Annotated[
            Optional[StrictInt],
            Field(description="page number of results to return (1-based)"),
        ] = None,
        limit: Annotated[
            Optional[StrictInt], Field(description="page size of results")
        ] = None,
        type: Annotated[
            Optional[StrictStr], Field(description="package type filter")
        ] = None,
        q: Annotated[Optional[StrictStr], Field(description="name filter")] = None,
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[List[Package], Awaitable[List[Package]]]:  # noqa: E501
        """Gets all packages of an owner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_packages(owner, page, limit, type, q, async_req=True)
        >>> result = thread.get()

        :param owner: owner of the packages (required)
        :type owner: str
        :param page: page number of results to return (1-based)
        :type page: int
        :param limit: page size of results
        :type limit: int
        :param type: package type filter
        :type type: str
        :param q: name filter
        :type q: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[Package]
        """
        kwargs["_return_http_data_only"] = True
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.list_packages_with_http_info(
            owner, page, limit, type, q, **kwargs
        )  # noqa: E501

    @validate_arguments
    def list_packages_with_http_info(
        self,
        owner: Annotated[StrictStr, Field(..., description="owner of the packages")],
        page: Annotated[
            Optional[StrictInt],
            Field(description="page number of results to return (1-based)"),
        ] = None,
        limit: Annotated[
            Optional[StrictInt], Field(description="page size of results")
        ] = None,
        type: Annotated[
            Optional[StrictStr], Field(description="package type filter")
        ] = None,
        q: Annotated[Optional[StrictStr], Field(description="name filter")] = None,
        **kwargs
    ):  # noqa: E501
        """Gets all packages of an owner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_packages_with_http_info(owner, page, limit, type, q, async_req=True)
        >>> result = thread.get()

        :param owner: owner of the packages (required)
        :type owner: str
        :param page: page number of results to return (1-based)
        :type page: int
        :param limit: page size of results
        :type limit: int
        :param type: package type filter
        :type type: str
        :param q: name filter
        :type q: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[Package], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["owner", "page", "limit", "type", "q"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_packages" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["owner"]:
            _path_params["owner"] = _params["owner"]

        # process the query parameters
        _query_params = []
        if _params.get("page") is not None:  # noqa: E501
            _query_params.append(("page", _params["page"]))

        if _params.get("limit") is not None:  # noqa: E501
            _query_params.append(("limit", _params["limit"]))

        if _params.get("type") is not None:  # noqa: E501
            _query_params.append(("type", _params["type"].value))

        if _params.get("q") is not None:  # noqa: E501
            _query_params.append(("q", _params["q"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = [
            "TOTPHeader",
            "AuthorizationHeaderToken",
            "SudoHeader",
            "BasicAuth",
            "AccessToken",
            "SudoParam",
            "Token",
        ]  # noqa: E501

        _response_types_map = {
            "200": "List[Package]",
        }

        return self.api_client.call_api(
            "/packages/{owner}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

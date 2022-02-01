# coding: utf-8

"""
    Nightscout API

    Own your DData with the Nightscout API  # noqa: E501

    OpenAPI spec version: 14.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nightscout_python_client.api_client import ApiClient


class TreatmentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_treatments(self, body, **kwargs):  # noqa: E501
        """Add new treatments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_treatments(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[Treatment] body: Treatments to be uploaded. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_treatments_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_treatments_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_treatments_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add new treatments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_treatments_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[Treatment] body: Treatments to be uploaded. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_treatments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_treatments`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_secret', 'jwtoken', 'token_in_url']  # noqa: E501

        return self.api_client.call_api(
            '/treatments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove(self, **kwargs):  # noqa: E501
        """Delete treatments matching query.  # noqa: E501

        Remove treatments, same search syntax as GET.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str find: The query used to find treatments to delete, support nested query syntax, for example `find[insulin][$gte]=3`. All find parameters are interpreted as strings.
        :param float count: Number of entries to return.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.remove_with_http_info(**kwargs)  # noqa: E501
            return data

    def remove_with_http_info(self, **kwargs):  # noqa: E501
        """Delete treatments matching query.  # noqa: E501

        Remove treatments, same search syntax as GET.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str find: The query used to find treatments to delete, support nested query syntax, for example `find[insulin][$gte]=3`. All find parameters are interpreted as strings.
        :param float count: Number of entries to return.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['find', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'find' in params:
            query_params.append(('find', params['find']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_secret', 'jwtoken', 'token_in_url']  # noqa: E501

        return self.api_client.call_api(
            '/treatments', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def treatments_get(self, **kwargs):  # noqa: E501
        """Treatments  # noqa: E501

        The Treatments endpoint returns information about the Nightscout treatments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.treatments_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str find: The query used to find entries, supports nested query syntax.  Examples `find[insulin][$gte]=3` `find[carb][$gte]=100` `find[eventType]=Correction+Bolus` All find parameters are interpreted as strings.
        :param float count: Number of entries to return.
        :return: Treatments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.treatments_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.treatments_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def treatments_get_with_http_info(self, **kwargs):  # noqa: E501
        """Treatments  # noqa: E501

        The Treatments endpoint returns information about the Nightscout treatments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.treatments_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str find: The query used to find entries, supports nested query syntax.  Examples `find[insulin][$gte]=3` `find[carb][$gte]=100` `find[eventType]=Correction+Bolus` All find parameters are interpreted as strings.
        :param float count: Number of entries to return.
        :return: Treatments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['find', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method treatments_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'find' in params:
            query_params.append(('find', params['find']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_secret', 'jwtoken', 'token_in_url']  # noqa: E501

        return self.api_client.call_api(
            '/treatments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Treatments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def treatments_spec_delete(self, spec, **kwargs):  # noqa: E501
        """Delete treatments record with id provided in spec  # noqa: E501

        The Treatments endpoint returns information about the Nightscout devicestatus records.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.treatments_spec_delete(spec, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spec: treatment id, such as `55cf81bc436037528ec75fa5`  (required)
        :return: DeleteStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.treatments_spec_delete_with_http_info(spec, **kwargs)  # noqa: E501
        else:
            (data) = self.treatments_spec_delete_with_http_info(spec, **kwargs)  # noqa: E501
            return data

    def treatments_spec_delete_with_http_info(self, spec, **kwargs):  # noqa: E501
        """Delete treatments record with id provided in spec  # noqa: E501

        The Treatments endpoint returns information about the Nightscout devicestatus records.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.treatments_spec_delete_with_http_info(spec, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str spec: treatment id, such as `55cf81bc436037528ec75fa5`  (required)
        :return: DeleteStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['spec']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method treatments_spec_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'spec' is set
        if ('spec' not in params or
                params['spec'] is None):
            raise ValueError("Missing the required parameter `spec` when calling `treatments_spec_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'spec' in params:
            path_params['spec'] = params['spec']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_secret', 'jwtoken', 'token_in_url']  # noqa: E501

        return self.api_client.call_api(
            '/treatments/{spec}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
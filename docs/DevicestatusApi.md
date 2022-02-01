# nightscout_python_client.DevicestatusApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_devicestatuses**](DevicestatusApi.md#add_devicestatuses) | **POST** /devicestatus/ | Add new devicestatus records.
[**devicestatus_delete**](DevicestatusApi.md#devicestatus_delete) | **DELETE** /devicestatus/ | Delete all Devicestatus records matching query
[**devicestatus_get**](DevicestatusApi.md#devicestatus_get) | **GET** /devicestatus/ | All Devicestatuses matching query
[**devicestatus_spec_delete**](DevicestatusApi.md#devicestatus_spec_delete) | **DELETE** /devicestatus/{spec} | Delete devicestatus record with id provided in spec

# **add_devicestatuses**
> add_devicestatuses(body)

Add new devicestatus records.

### Example
```python
from __future__ import print_function
import time
import nightscout_python_client
from nightscout_python_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_secret
configuration = nightscout_python_client.Configuration()
configuration.api_key['api_secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_secret'] = 'Bearer'
# Configure API key authorization: token_in_url
configuration = nightscout_python_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = nightscout_python_client.DevicestatusApi(nightscout_python_client.ApiClient(configuration))
body = [nightscout_python_client.Devicestatus()] # list[Devicestatus] | Device statuses to be uploaded.

try:
    # Add new devicestatus records.
    api_instance.add_devicestatuses(body)
except ApiException as e:
    print("Exception when calling DevicestatusApi->add_devicestatuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Devicestatus]**](Devicestatus.md)| Device statuses to be uploaded. | 

### Return type

void (empty response body)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicestatus_delete**
> DeleteStatus devicestatus_delete(find=find)

Delete all Devicestatus records matching query

The Devicestatus endpoint returns information about the Nightscout devicestatus records. 

### Example
```python
from __future__ import print_function
import time
import nightscout_python_client
from nightscout_python_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_secret
configuration = nightscout_python_client.Configuration()
configuration.api_key['api_secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_secret'] = 'Bearer'
# Configure API key authorization: token_in_url
configuration = nightscout_python_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = nightscout_python_client.DevicestatusApi(nightscout_python_client.ApiClient(configuration))
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[created_at][$gte]=2015-08-27`.  All find parameters are interpreted as strings.  (optional)

try:
    # Delete all Devicestatus records matching query
    api_response = api_instance.devicestatus_delete(find=find)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicestatusApi->devicestatus_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find** | **str**| The query used to find entries, support nested query syntax, for example &#x60;find[created_at][$gte]&#x3D;2015-08-27&#x60;.  All find parameters are interpreted as strings.  | [optional] 

### Return type

[**DeleteStatus**](DeleteStatus.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicestatus_get**
> Devicestatuses devicestatus_get(find=find, count=count)

All Devicestatuses matching query

The Devicestatus endpoint returns information about the Nightscout devicestatus records.

### Example
```python
from __future__ import print_function
import time
import nightscout_python_client
from nightscout_python_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_secret
configuration = nightscout_python_client.Configuration()
configuration.api_key['api_secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_secret'] = 'Bearer'
# Configure API key authorization: token_in_url
configuration = nightscout_python_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = nightscout_python_client.DevicestatusApi(nightscout_python_client.ApiClient(configuration))
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings. (optional)
count = 1.2 # float | Number of devicestatus records to return. (optional)

try:
    # All Devicestatuses matching query
    api_response = api_instance.devicestatus_get(find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicestatusApi->devicestatus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find** | **str**| The query used to find entries, support nested query syntax, for example &#x60;find[dateString][$gte]&#x3D;2015-08-27&#x60;.  All find parameters are interpreted as strings. | [optional] 
 **count** | **float**| Number of devicestatus records to return. | [optional] 

### Return type

[**Devicestatuses**](Devicestatuses.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devicestatus_spec_delete**
> DeleteStatus devicestatus_spec_delete(spec)

Delete devicestatus record with id provided in spec

The Devicestatus endpoint returns information about the Nightscout devicestatus records. 

### Example
```python
from __future__ import print_function
import time
import nightscout_python_client
from nightscout_python_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_secret
configuration = nightscout_python_client.Configuration()
configuration.api_key['api_secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_secret'] = 'Bearer'
# Configure API key authorization: token_in_url
configuration = nightscout_python_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = nightscout_python_client.DevicestatusApi(nightscout_python_client.ApiClient(configuration))
spec = 'spec_example' # str | entry id, such as `55cf81bc436037528ec75fa5` 

try:
    # Delete devicestatus record with id provided in spec
    api_response = api_instance.devicestatus_spec_delete(spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicestatusApi->devicestatus_spec_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec** | **str**| entry id, such as &#x60;55cf81bc436037528ec75fa5&#x60;  | 

### Return type

[**DeleteStatus**](DeleteStatus.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


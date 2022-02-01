# nightscout_python_client.ProfileApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_get**](ProfileApi.md#profile_get) | **GET** /profile | Profile

# **profile_get**
> Profile profile_get()

Profile

The Profile endpoint returns information about the Nightscout Treatment Profiles.

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
api_instance = nightscout_python_client.ProfileApi(nightscout_python_client.ApiClient(configuration))

try:
    # Profile
    api_response = api_instance.profile_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->profile_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


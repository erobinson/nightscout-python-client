# nightscout_python_client.TreatmentsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_treatments**](TreatmentsApi.md#add_treatments) | **POST** /treatments | Add new treatments.
[**remove**](TreatmentsApi.md#remove) | **DELETE** /treatments | Delete treatments matching query.
[**treatments_get**](TreatmentsApi.md#treatments_get) | **GET** /treatments | Treatments
[**treatments_spec_delete**](TreatmentsApi.md#treatments_spec_delete) | **DELETE** /treatments/{spec} | Delete treatments record with id provided in spec

# **add_treatments**
> add_treatments(body)

Add new treatments.

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
api_instance = nightscout_python_client.TreatmentsApi(nightscout_python_client.ApiClient(configuration))
body = [nightscout_python_client.Treatment()] # list[Treatment] | Treatments to be uploaded.

try:
    # Add new treatments.
    api_instance.add_treatments(body)
except ApiException as e:
    print("Exception when calling TreatmentsApi->add_treatments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Treatment]**](Treatment.md)| Treatments to be uploaded. | 

### Return type

void (empty response body)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove**
> remove(find=find, count=count)

Delete treatments matching query.

Remove treatments, same search syntax as GET.

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
api_instance = nightscout_python_client.TreatmentsApi(nightscout_python_client.ApiClient(configuration))
find = 'find_example' # str | The query used to find treatments to delete, support nested query syntax, for example `find[insulin][$gte]=3`. All find parameters are interpreted as strings. (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # Delete treatments matching query.
    api_instance.remove(find=find, count=count)
except ApiException as e:
    print("Exception when calling TreatmentsApi->remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find** | **str**| The query used to find treatments to delete, support nested query syntax, for example &#x60;find[insulin][$gte]&#x3D;3&#x60;. All find parameters are interpreted as strings. | [optional] 
 **count** | **float**| Number of entries to return. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **treatments_get**
> Treatments treatments_get(find=find, count=count)

Treatments

The Treatments endpoint returns information about the Nightscout treatments.

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
api_instance = nightscout_python_client.TreatmentsApi(nightscout_python_client.ApiClient(configuration))
find = 'find_example' # str | The query used to find entries, supports nested query syntax.  Examples `find[insulin][$gte]=3` `find[carb][$gte]=100` `find[eventType]=Correction+Bolus` All find parameters are interpreted as strings. (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # Treatments
    api_response = api_instance.treatments_get(find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreatmentsApi->treatments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find** | **str**| The query used to find entries, supports nested query syntax.  Examples &#x60;find[insulin][$gte]&#x3D;3&#x60; &#x60;find[carb][$gte]&#x3D;100&#x60; &#x60;find[eventType]&#x3D;Correction+Bolus&#x60; All find parameters are interpreted as strings. | [optional] 
 **count** | **float**| Number of entries to return. | [optional] 

### Return type

[**Treatments**](Treatments.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **treatments_spec_delete**
> DeleteStatus treatments_spec_delete(spec)

Delete treatments record with id provided in spec

The Treatments endpoint returns information about the Nightscout devicestatus records. 

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
api_instance = nightscout_python_client.TreatmentsApi(nightscout_python_client.ApiClient(configuration))
spec = 'spec_example' # str | treatment id, such as `55cf81bc436037528ec75fa5` 

try:
    # Delete treatments record with id provided in spec
    api_response = api_instance.treatments_spec_delete(spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TreatmentsApi->treatments_spec_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec** | **str**| treatment id, such as &#x60;55cf81bc436037528ec75fa5&#x60;  | 

### Return type

[**DeleteStatus**](DeleteStatus.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


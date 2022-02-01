# nightscout_python_client.EntriesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entries**](EntriesApi.md#add_entries) | **POST** /entries | Add new entries.
[**echo_storage_spec_get**](EntriesApi.md#echo_storage_spec_get) | **GET** /echo/{storage}/{spec} | View generated Mongo Query object
[**entries_get**](EntriesApi.md#entries_get) | **GET** /entries | All Entries matching query
[**entries_spec_get**](EntriesApi.md#entries_spec_get) | **GET** /entries/{spec} | All Entries matching query
[**remove**](EntriesApi.md#remove) | **DELETE** /entries | Delete entries matching query.
[**slice_storage_field_type_prefix_regex_get**](EntriesApi.md#slice_storage_field_type_prefix_regex_get) | **GET** /slice/{storage}/{field}/{type}/{prefix}/{regex} | All Entries matching query
[**times_echo_prefix_regex_get**](EntriesApi.md#times_echo_prefix_regex_get) | **GET** /times/echo/{prefix}/{regex} | Echo the query object to be used.
[**times_prefix_regex_get**](EntriesApi.md#times_prefix_regex_get) | **GET** /times/{prefix}/{regex} | All Entries matching query

# **add_entries**
> add_entries(body)

Add new entries.

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
api_instance = nightscout_python_client.EntriesApi(nightscout_python_client.ApiClient(configuration))
body = [nightscout_python_client.Entry()] # list[Entry] | Entries to be uploaded.

try:
    # Add new entries.
    api_instance.add_entries(body)
except ApiException as e:
    print("Exception when calling EntriesApi->add_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Entry]**](Entry.md)| Entries to be uploaded. | 

### Return type

void (empty response body)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **echo_storage_spec_get**
> MongoQuery echo_storage_spec_get(storage, spec, find=find, count=count)

View generated Mongo Query object

Information about the mongo query object created by the query. 

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
api_instance = nightscout_python_client.EntriesApi(nightscout_python_client.ApiClient(configuration))
storage = 'storage_example' # str | `entries`, or `treatments` to select the storage layer. 
spec = 'spec_example' # str | entry id, such as `55cf81bc436037528ec75fa5` or a type filter such as `sgv`, `mbg`, etc. This parameter is optional. 
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings.  (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # View generated Mongo Query object
    api_response = api_instance.echo_storage_spec_get(storage, spec, find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->echo_storage_spec_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage** | **str**| &#x60;entries&#x60;, or &#x60;treatments&#x60; to select the storage layer.  | 
 **spec** | **str**| entry id, such as &#x60;55cf81bc436037528ec75fa5&#x60; or a type filter such as &#x60;sgv&#x60;, &#x60;mbg&#x60;, etc. This parameter is optional.  | 
 **find** | **str**| The query used to find entries, support nested query syntax, for example &#x60;find[dateString][$gte]&#x3D;2015-08-27&#x60;.  All find parameters are interpreted as strings.  | [optional] 
 **count** | **float**| Number of entries to return. | [optional] 

### Return type

[**MongoQuery**](MongoQuery.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entries_get**
> Entries entries_get(find=find, count=count)

All Entries matching query

The Entries endpoint returns information about the Nightscout entries.

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
api_instance = nightscout_python_client.EntriesApi(nightscout_python_client.ApiClient(configuration))
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings. (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # All Entries matching query
    api_response = api_instance.entries_get(find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->entries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find** | **str**| The query used to find entries, support nested query syntax, for example &#x60;find[dateString][$gte]&#x3D;2015-08-27&#x60;.  All find parameters are interpreted as strings. | [optional] 
 **count** | **float**| Number of entries to return. | [optional] 

### Return type

[**Entries**](Entries.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entries_spec_get**
> Entries entries_spec_get(spec, find=find, count=count)

All Entries matching query

The Entries endpoint returns information about the Nightscout entries. 

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
api_instance = nightscout_python_client.EntriesApi(nightscout_python_client.ApiClient(configuration))
spec = 'spec_example' # str | entry id, such as `55cf81bc436037528ec75fa5` or a type filter such as `sgv`, `mbg`, etc. 
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings.  (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # All Entries matching query
    api_response = api_instance.entries_spec_get(spec, find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->entries_spec_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec** | **str**| entry id, such as &#x60;55cf81bc436037528ec75fa5&#x60; or a type filter such as &#x60;sgv&#x60;, &#x60;mbg&#x60;, etc.  | 
 **find** | **str**| The query used to find entries, support nested query syntax, for example &#x60;find[dateString][$gte]&#x3D;2015-08-27&#x60;.  All find parameters are interpreted as strings.  | [optional] 
 **count** | **float**| Number of entries to return. | [optional] 

### Return type

[**Entries**](Entries.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove**
> remove(find=find, count=count)

Delete entries matching query.

Remove entries, same search syntax as GET.

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
api_instance = nightscout_python_client.EntriesApi(nightscout_python_client.ApiClient(configuration))
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings. (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # Delete entries matching query.
    api_instance.remove(find=find, count=count)
except ApiException as e:
    print("Exception when calling EntriesApi->remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find** | **str**| The query used to find entries, support nested query syntax, for example &#x60;find[dateString][$gte]&#x3D;2015-08-27&#x60;.  All find parameters are interpreted as strings. | [optional] 
 **count** | **float**| Number of entries to return. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slice_storage_field_type_prefix_regex_get**
> Entries slice_storage_field_type_prefix_regex_get(storage, field, type, prefix, regex, find=find, count=count)

All Entries matching query

The Entries endpoint returns information about the Nightscout entries.

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
api_instance = nightscout_python_client.EntriesApi(nightscout_python_client.ApiClient(configuration))
storage = 'storage_example' # str | Prefix to use in constructing a prefix-based regex, default is `entries`.
field = 'field_example' # str | Name of the field to use Regex against in query object, default is `dateString`.
type = 'type_example' # str | The type field to search against, default is sgv.
prefix = 'prefix_example' # str | Prefix to use in constructing a prefix-based regex.
regex = 'regex_example' # str | Tail part of regexp to use in expanding/construccting a query object. Regexp also has bash-style brace and glob expansion applied to it, creating ways to search for modal times of day, perhaps using something like this syntax: `T{15..17}:.*`, this would search for all records from 3pm to 5pm. 
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings.  (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # All Entries matching query
    api_response = api_instance.slice_storage_field_type_prefix_regex_get(storage, field, type, prefix, regex, find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->slice_storage_field_type_prefix_regex_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage** | **str**| Prefix to use in constructing a prefix-based regex, default is &#x60;entries&#x60;. | 
 **field** | **str**| Name of the field to use Regex against in query object, default is &#x60;dateString&#x60;. | 
 **type** | **str**| The type field to search against, default is sgv. | 
 **prefix** | **str**| Prefix to use in constructing a prefix-based regex. | 
 **regex** | **str**| Tail part of regexp to use in expanding/construccting a query object. Regexp also has bash-style brace and glob expansion applied to it, creating ways to search for modal times of day, perhaps using something like this syntax: &#x60;T{15..17}:.*&#x60;, this would search for all records from 3pm to 5pm.  | 
 **find** | **str**| The query used to find entries, support nested query syntax, for example &#x60;find[dateString][$gte]&#x3D;2015-08-27&#x60;.  All find parameters are interpreted as strings.  | [optional] 
 **count** | **float**| Number of entries to return. | [optional] 

### Return type

[**Entries**](Entries.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **times_echo_prefix_regex_get**
> MongoQuery times_echo_prefix_regex_get(prefix, regex, find=find, count=count)

Echo the query object to be used.

Echo debug information about the query object constructed.

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
api_instance = nightscout_python_client.EntriesApi(nightscout_python_client.ApiClient(configuration))
prefix = 'prefix_example' # str | Prefix to use in constructing a prefix-based regex.
regex = 'regex_example' # str | Tail part of regexp to use in expanding/construccting a query object. Regexp also has bash-style brace and glob expansion applied to it, creating ways to search for modal times of day, perhaps using something like this syntax: `T{15..17}:.*`, this would search for all records from 3pm to 5pm. 
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings. (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # Echo the query object to be used.
    api_response = api_instance.times_echo_prefix_regex_get(prefix, regex, find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->times_echo_prefix_regex_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| Prefix to use in constructing a prefix-based regex. | 
 **regex** | **str**| Tail part of regexp to use in expanding/construccting a query object. Regexp also has bash-style brace and glob expansion applied to it, creating ways to search for modal times of day, perhaps using something like this syntax: &#x60;T{15..17}:.*&#x60;, this would search for all records from 3pm to 5pm.  | 
 **find** | **str**| The query used to find entries, support nested query syntax, for example &#x60;find[dateString][$gte]&#x3D;2015-08-27&#x60;.  All find parameters are interpreted as strings. | [optional] 
 **count** | **float**| Number of entries to return. | [optional] 

### Return type

[**MongoQuery**](MongoQuery.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **times_prefix_regex_get**
> Entries times_prefix_regex_get(prefix, regex, find=find, count=count)

All Entries matching query

The Entries endpoint returns information about the Nightscout entries.

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
api_instance = nightscout_python_client.EntriesApi(nightscout_python_client.ApiClient(configuration))
prefix = 'prefix_example' # str | Prefix to use in constructing a prefix-based regex.
regex = 'regex_example' # str | Tail part of regexp to use in expanding/construccting a query object. Regexp also has bash-style brace and glob expansion applied to it, creating ways to search for modal times of day, perhaps using something like this syntax: `T{15..17}:.*`, this would search for all records from 3pm to 5pm. 
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings. (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # All Entries matching query
    api_response = api_instance.times_prefix_regex_get(prefix, regex, find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->times_prefix_regex_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| Prefix to use in constructing a prefix-based regex. | 
 **regex** | **str**| Tail part of regexp to use in expanding/construccting a query object. Regexp also has bash-style brace and glob expansion applied to it, creating ways to search for modal times of day, perhaps using something like this syntax: &#x60;T{15..17}:.*&#x60;, this would search for all records from 3pm to 5pm.  | 
 **find** | **str**| The query used to find entries, support nested query syntax, for example &#x60;find[dateString][$gte]&#x3D;2015-08-27&#x60;.  All find parameters are interpreted as strings. | [optional] 
 **count** | **float**| Number of entries to return. | [optional] 

### Return type

[**Entries**](Entries.md)

### Authorization

[api_secret](../README.md#api_secret), [jwtoken](../README.md#jwtoken), [token_in_url](../README.md#token_in_url)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


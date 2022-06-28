# start by checking out the API docs

https://<your-site>.herokuapp.com/api-docs/
https://<your-site>.herokuapp.com/api3-docs/

# nightscout-python-client
Own your Data with the Nightscout API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 14.2.2
- Package version: 0.0.1
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## INITIAL VERSION

This is a very initial version, only tested getting entries so far.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import nightscout_python_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import nightscout_python_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import nightscout_python_client
from nightscout_python_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_secret
configuration = nightscout_python_client.Configuration()
configuration.host = "<YOUR_SITE_HERE.herokuapp.com>/api/v1"
configuration.api_key['api_secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_secret'] = 'Bearer'
# Configure API key authorization: token_in_url
configuration = nightscout_python_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = nightscout_python_client.DebugApi(nightscout_python_client.ApiClient(configuration))
storage = 'storage_example' # str | `entries`, or `treatments` to select the storage layer. 
spec = 'spec_example' # str | entry id, such as `55cf81bc436037528ec75fa5` or a type filter such as `sgv`, `mbg`, etc. This parameter is optional. 
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings.  (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # View generated Mongo Query object
    api_response = api_instance.echo_storage_spec_get(storage, spec, find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->echo_storage_spec_get: %s\n" % e)

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
api_instance = nightscout_python_client.DebugApi(nightscout_python_client.ApiClient(configuration))
prefix = 'prefix_example' # str | Prefix to use in constructing a prefix-based regex.
regex = 'regex_example' # str | Tail part of regexp to use in expanding/construccting a query object. Regexp also has bash-style brace and glob expansion applied to it, creating ways to search for modal times of day, perhaps using something like this syntax: `T{15..17}:.*`, this would search for all records from 3pm to 5pm. 
find = 'find_example' # str | The query used to find entries, support nested query syntax, for example `find[dateString][$gte]=2015-08-27`.  All find parameters are interpreted as strings. (optional)
count = 1.2 # float | Number of entries to return. (optional)

try:
    # Echo the query object to be used.
    api_response = api_instance.times_echo_prefix_regex_get(prefix, regex, find=find, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->times_echo_prefix_regex_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DebugApi* | [**echo_storage_spec_get**](docs/DebugApi.md#echo_storage_spec_get) | **GET** /echo/{storage}/{spec} | View generated Mongo Query object
*DebugApi* | [**times_echo_prefix_regex_get**](docs/DebugApi.md#times_echo_prefix_regex_get) | **GET** /times/echo/{prefix}/{regex} | Echo the query object to be used.
*DevicestatusApi* | [**add_devicestatuses**](docs/DevicestatusApi.md#add_devicestatuses) | **POST** /devicestatus/ | Add new devicestatus records.
*DevicestatusApi* | [**devicestatus_delete**](docs/DevicestatusApi.md#devicestatus_delete) | **DELETE** /devicestatus/ | Delete all Devicestatus records matching query
*DevicestatusApi* | [**devicestatus_get**](docs/DevicestatusApi.md#devicestatus_get) | **GET** /devicestatus/ | All Devicestatuses matching query
*DevicestatusApi* | [**devicestatus_spec_delete**](docs/DevicestatusApi.md#devicestatus_spec_delete) | **DELETE** /devicestatus/{spec} | Delete devicestatus record with id provided in spec
*EntriesApi* | [**add_entries**](docs/EntriesApi.md#add_entries) | **POST** /entries | Add new entries.
*EntriesApi* | [**echo_storage_spec_get**](docs/EntriesApi.md#echo_storage_spec_get) | **GET** /echo/{storage}/{spec} | View generated Mongo Query object
*EntriesApi* | [**entries_get**](docs/EntriesApi.md#entries_get) | **GET** /entries | All Entries matching query
*EntriesApi* | [**entries_spec_get**](docs/EntriesApi.md#entries_spec_get) | **GET** /entries/{spec} | All Entries matching query
*EntriesApi* | [**remove**](docs/EntriesApi.md#remove) | **DELETE** /entries | Delete entries matching query.
*EntriesApi* | [**slice_storage_field_type_prefix_regex_get**](docs/EntriesApi.md#slice_storage_field_type_prefix_regex_get) | **GET** /slice/{storage}/{field}/{type}/{prefix}/{regex} | All Entries matching query
*EntriesApi* | [**times_echo_prefix_regex_get**](docs/EntriesApi.md#times_echo_prefix_regex_get) | **GET** /times/echo/{prefix}/{regex} | Echo the query object to be used.
*EntriesApi* | [**times_prefix_regex_get**](docs/EntriesApi.md#times_prefix_regex_get) | **GET** /times/{prefix}/{regex} | All Entries matching query
*ProfileApi* | [**profile_get**](docs/ProfileApi.md#profile_get) | **GET** /profile | Profile
*StatusApi* | [**status_get**](docs/StatusApi.md#status_get) | **GET** /status | Status
*TreatmentsApi* | [**add_treatments**](docs/TreatmentsApi.md#add_treatments) | **POST** /treatments | Add new treatments.
*TreatmentsApi* | [**remove**](docs/TreatmentsApi.md#remove) | **DELETE** /treatments | Delete treatments matching query.
*TreatmentsApi* | [**treatments_get**](docs/TreatmentsApi.md#treatments_get) | **GET** /treatments | Treatments
*TreatmentsApi* | [**treatments_spec_delete**](docs/TreatmentsApi.md#treatments_spec_delete) | **DELETE** /treatments/{spec} | Delete treatments record with id provided in spec

## Documentation For Models

 - [DeleteStatus](docs/DeleteStatus.md)
 - [Devicestatus](docs/Devicestatus.md)
 - [Devicestatuses](docs/Devicestatuses.md)
 - [Entries](docs/Entries.md)
 - [Entry](docs/Entry.md)
 - [Error](docs/Error.md)
 - [ExtendedSettings](docs/ExtendedSettings.md)
 - [MongoQuery](docs/MongoQuery.md)
 - [Optime](docs/Optime.md)
 - [Profile](docs/Profile.md)
 - [Pump](docs/Pump.md)
 - [Pumpbattery](docs/Pumpbattery.md)
 - [Pumpstatus](docs/Pumpstatus.md)
 - [Settings](docs/Settings.md)
 - [Status](docs/Status.md)
 - [Threshold](docs/Threshold.md)
 - [Treatment](docs/Treatment.md)
 - [Treatments](docs/Treatments.md)
 - [Uploader](docs/Uploader.md)
 - [Xdripjs](docs/Xdripjs.md)

## Documentation For Authorization


## api_secret

- **Type**: API key
- **API key parameter name**: api_secret
- **Location**: HTTP header

## jwtoken


## token_in_url

- **Type**: API key
- **API key parameter name**: token
- **Location**: URL query string


## Author



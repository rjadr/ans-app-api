# ans_app_api.LocationsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_locations_id_delete**](LocationsApi.md#api_v2_locations_id_delete) | **DELETE** /api/v2/locations/{id} | Delete location
[**api_v2_locations_id_get**](LocationsApi.md#api_v2_locations_id_get) | **GET** /api/v2/locations/{id} | Show Location
[**api_v2_locations_id_patch**](LocationsApi.md#api_v2_locations_id_patch) | **PATCH** /api/v2/locations/{id} | Update location
[**api_v2_schools_school_id_locations_get**](LocationsApi.md#api_v2_schools_school_id_locations_get) | **GET** /api/v2/schools/{school_id}/locations | List locations
[**api_v2_schools_school_id_locations_post**](LocationsApi.md#api_v2_schools_school_id_locations_post) | **POST** /api/v2/schools/{school_id}/locations | Create location

# **api_v2_locations_id_delete**
> InlineResponse20012 api_v2_locations_id_delete(id)

Delete location

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LocationsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete location
    api_response = api_instance.api_v2_locations_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->api_v2_locations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_locations_id_get**
> InlineResponse20012 api_v2_locations_id_get(id)

Show Location

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LocationsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show Location
    api_response = api_instance.api_v2_locations_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->api_v2_locations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_locations_id_patch**
> InlineResponse20012 api_v2_locations_id_patch(id, body=body)

Update location

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LocationsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.LocationsIdBody() # LocationsIdBody |  (optional)

try:
    # Update location
    api_response = api_instance.api_v2_locations_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->api_v2_locations_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**LocationsIdBody**](LocationsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_locations_get**
> list[InlineResponse20012] api_v2_schools_school_id_locations_get(school_id, items=items, page=page)

List locations

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LocationsApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List locations
    api_response = api_instance.api_v2_schools_school_id_locations_get(school_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->api_v2_schools_school_id_locations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20012]**](InlineResponse20012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_locations_post**
> InlineResponse20012 api_v2_schools_school_id_locations_post(school_id, body=body)

Create location

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LocationsApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
body = ans_app_api.SchoolIdLocationsBody() # SchoolIdLocationsBody |  (optional)

try:
    # Create location
    api_response = api_instance.api_v2_schools_school_id_locations_post(school_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->api_v2_schools_school_id_locations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **body** | [**SchoolIdLocationsBody**](SchoolIdLocationsBody.md)|  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


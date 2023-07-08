# ans_app_api.PeriodsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_periods_id_delete**](PeriodsApi.md#api_v2_periods_id_delete) | **DELETE** /api/v2/periods/{id} | Delete period
[**api_v2_periods_id_get**](PeriodsApi.md#api_v2_periods_id_get) | **GET** /api/v2/periods/{id} | Show period
[**api_v2_periods_id_patch**](PeriodsApi.md#api_v2_periods_id_patch) | **PATCH** /api/v2/periods/{id} | Update period
[**api_v2_schools_school_id_periods_get**](PeriodsApi.md#api_v2_schools_school_id_periods_get) | **GET** /api/v2/schools/{school_id}/periods | List periods
[**api_v2_schools_school_id_periods_post**](PeriodsApi.md#api_v2_schools_school_id_periods_post) | **POST** /api/v2/schools/{school_id}/periods | Create period

# **api_v2_periods_id_delete**
> api_v2_periods_id_delete(id)

Delete period

Hard delete a period

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PeriodsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete period
    api_instance.api_v2_periods_id_delete(id)
except ApiException as e:
    print("Exception when calling PeriodsApi->api_v2_periods_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_periods_id_get**
> api_v2_periods_id_get(id)

Show period

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PeriodsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show period
    api_instance.api_v2_periods_id_get(id)
except ApiException as e:
    print("Exception when calling PeriodsApi->api_v2_periods_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_periods_id_patch**
> api_v2_periods_id_patch(id, body=body)

Update period

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PeriodsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.PeriodsIdBody() # PeriodsIdBody |  (optional)

try:
    # Update period
    api_instance.api_v2_periods_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling PeriodsApi->api_v2_periods_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**PeriodsIdBody**](PeriodsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_periods_get**
> api_v2_schools_school_id_periods_get(school_id, items=items, page=page)

List periods

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PeriodsApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List periods
    api_instance.api_v2_schools_school_id_periods_get(school_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling PeriodsApi->api_v2_schools_school_id_periods_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_periods_post**
> api_v2_schools_school_id_periods_post(school_id, body=body)

Create period

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PeriodsApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
body = ans_app_api.SchoolIdPeriodsBody() # SchoolIdPeriodsBody |  (optional)

try:
    # Create period
    api_instance.api_v2_schools_school_id_periods_post(school_id, body=body)
except ApiException as e:
    print("Exception when calling PeriodsApi->api_v2_schools_school_id_periods_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **body** | [**SchoolIdPeriodsBody**](SchoolIdPeriodsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


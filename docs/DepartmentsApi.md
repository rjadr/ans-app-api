# ans_app_api.DepartmentsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_departments_id_delete**](DepartmentsApi.md#api_v2_departments_id_delete) | **DELETE** /api/v2/departments/{id} | Delete department
[**api_v2_departments_id_get**](DepartmentsApi.md#api_v2_departments_id_get) | **GET** /api/v2/departments/{id} | Show department
[**api_v2_departments_id_patch**](DepartmentsApi.md#api_v2_departments_id_patch) | **PATCH** /api/v2/departments/{id} | Update department
[**api_v2_schools_school_id_departments_get**](DepartmentsApi.md#api_v2_schools_school_id_departments_get) | **GET** /api/v2/schools/{school_id}/departments | List departments
[**api_v2_schools_school_id_departments_post**](DepartmentsApi.md#api_v2_schools_school_id_departments_post) | **POST** /api/v2/schools/{school_id}/departments | Create department

# **api_v2_departments_id_delete**
> api_v2_departments_id_delete(id)

Delete department

Hard delete a department

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DepartmentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete department
    api_instance.api_v2_departments_id_delete(id)
except ApiException as e:
    print("Exception when calling DepartmentsApi->api_v2_departments_id_delete: %s\n" % e)
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

# **api_v2_departments_id_get**
> api_v2_departments_id_get(id)

Show department

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DepartmentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show department
    api_instance.api_v2_departments_id_get(id)
except ApiException as e:
    print("Exception when calling DepartmentsApi->api_v2_departments_id_get: %s\n" % e)
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

# **api_v2_departments_id_patch**
> api_v2_departments_id_patch(id, body=body)

Update department

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DepartmentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.DepartmentsIdBody() # DepartmentsIdBody |  (optional)

try:
    # Update department
    api_instance.api_v2_departments_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling DepartmentsApi->api_v2_departments_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**DepartmentsIdBody**](DepartmentsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_departments_get**
> list[InlineResponse2005] api_v2_schools_school_id_departments_get(school_id, items=items, page=page)

List departments

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DepartmentsApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List departments
    api_response = api_instance.api_v2_schools_school_id_departments_get(school_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->api_v2_schools_school_id_departments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2005]**](InlineResponse2005.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_departments_post**
> api_v2_schools_school_id_departments_post(school_id, body=body)

Create department

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DepartmentsApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
body = ans_app_api.SchoolIdDepartmentsBody() # SchoolIdDepartmentsBody |  (optional)

try:
    # Create department
    api_instance.api_v2_schools_school_id_departments_post(school_id, body=body)
except ApiException as e:
    print("Exception when calling DepartmentsApi->api_v2_schools_school_id_departments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **body** | [**SchoolIdDepartmentsBody**](SchoolIdDepartmentsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


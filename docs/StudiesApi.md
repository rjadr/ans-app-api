# ans_app_api.StudiesApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_departments_department_id_studies_get**](StudiesApi.md#api_v2_departments_department_id_studies_get) | **GET** /api/v2/departments/{department_id}/studies | List studies
[**api_v2_departments_department_id_studies_post**](StudiesApi.md#api_v2_departments_department_id_studies_post) | **POST** /api/v2/departments/{department_id}/studies | Create study
[**api_v2_studies_id_delete**](StudiesApi.md#api_v2_studies_id_delete) | **DELETE** /api/v2/studies/{id} | Delete study
[**api_v2_studies_id_get**](StudiesApi.md#api_v2_studies_id_get) | **GET** /api/v2/studies/{id} | Show study
[**api_v2_studies_id_patch**](StudiesApi.md#api_v2_studies_id_patch) | **PATCH** /api/v2/studies/{id} | Update study

# **api_v2_departments_department_id_studies_get**
> api_v2_departments_department_id_studies_get(department_id, items=items, page=page)

List studies

List all studies of the department

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.StudiesApi(ans_app_api.ApiClient(configuration))
department_id = 'department_id_example' # str | department_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List studies
    api_instance.api_v2_departments_department_id_studies_get(department_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling StudiesApi->api_v2_departments_department_id_studies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **str**| department_id | 
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

# **api_v2_departments_department_id_studies_post**
> api_v2_departments_department_id_studies_post(department_id, body=body)

Create study

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.StudiesApi(ans_app_api.ApiClient(configuration))
department_id = 'department_id_example' # str | department_id
body = ans_app_api.DepartmentIdStudiesBody() # DepartmentIdStudiesBody |  (optional)

try:
    # Create study
    api_instance.api_v2_departments_department_id_studies_post(department_id, body=body)
except ApiException as e:
    print("Exception when calling StudiesApi->api_v2_departments_department_id_studies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **str**| department_id | 
 **body** | [**DepartmentIdStudiesBody**](DepartmentIdStudiesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_studies_id_delete**
> api_v2_studies_id_delete(id)

Delete study

Hard delete a study

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.StudiesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete study
    api_instance.api_v2_studies_id_delete(id)
except ApiException as e:
    print("Exception when calling StudiesApi->api_v2_studies_id_delete: %s\n" % e)
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

# **api_v2_studies_id_get**
> api_v2_studies_id_get(id)

Show study

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.StudiesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show study
    api_instance.api_v2_studies_id_get(id)
except ApiException as e:
    print("Exception when calling StudiesApi->api_v2_studies_id_get: %s\n" % e)
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

# **api_v2_studies_id_patch**
> api_v2_studies_id_patch(id, body=body)

Update study

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.StudiesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.StudiesIdBody() # StudiesIdBody |  (optional)

try:
    # Update study
    api_instance.api_v2_studies_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling StudiesApi->api_v2_studies_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**StudiesIdBody**](StudiesIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


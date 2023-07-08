# ans_app_api.RequirementsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_requirements_get**](RequirementsApi.md#api_v2_assignments_assignment_id_requirements_get) | **GET** /api/v2/assignments/{assignment_id}/requirements | List requirements
[**api_v2_assignments_assignment_id_requirements_post**](RequirementsApi.md#api_v2_assignments_assignment_id_requirements_post) | **POST** /api/v2/assignments/{assignment_id}/requirements | Create requirement
[**api_v2_requirements_id_delete**](RequirementsApi.md#api_v2_requirements_id_delete) | **DELETE** /api/v2/requirements/{id}/ | Delete requirement
[**api_v2_requirements_id_get**](RequirementsApi.md#api_v2_requirements_id_get) | **GET** /api/v2/requirements/{id}/ | Show requirement
[**api_v2_requirements_id_patch**](RequirementsApi.md#api_v2_requirements_id_patch) | **PATCH** /api/v2/requirements/{id}/ | Update requirement

# **api_v2_assignments_assignment_id_requirements_get**
> api_v2_assignments_assignment_id_requirements_get(assignment_id, items=items, page=page)

List requirements

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.RequirementsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List requirements
    api_instance.api_v2_assignments_assignment_id_requirements_get(assignment_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling RequirementsApi->api_v2_assignments_assignment_id_requirements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
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

# **api_v2_assignments_assignment_id_requirements_post**
> api_v2_assignments_assignment_id_requirements_post(assignment_id, body=body)

Create requirement

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.RequirementsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
body = ans_app_api.AssignmentIdRequirementsBody() # AssignmentIdRequirementsBody |  (optional)

try:
    # Create requirement
    api_instance.api_v2_assignments_assignment_id_requirements_post(assignment_id, body=body)
except ApiException as e:
    print("Exception when calling RequirementsApi->api_v2_assignments_assignment_id_requirements_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **body** | [**AssignmentIdRequirementsBody**](AssignmentIdRequirementsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_requirements_id_delete**
> api_v2_requirements_id_delete(id)

Delete requirement

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.RequirementsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete requirement
    api_instance.api_v2_requirements_id_delete(id)
except ApiException as e:
    print("Exception when calling RequirementsApi->api_v2_requirements_id_delete: %s\n" % e)
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

# **api_v2_requirements_id_get**
> api_v2_requirements_id_get(id)

Show requirement

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.RequirementsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show requirement
    api_instance.api_v2_requirements_id_get(id)
except ApiException as e:
    print("Exception when calling RequirementsApi->api_v2_requirements_id_get: %s\n" % e)
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

# **api_v2_requirements_id_patch**
> api_v2_requirements_id_patch(id, body=body)

Update requirement

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.RequirementsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.RequirementsIdBody() # RequirementsIdBody |  (optional)

try:
    # Update requirement
    api_instance.api_v2_requirements_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling RequirementsApi->api_v2_requirements_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**RequirementsIdBody**](RequirementsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


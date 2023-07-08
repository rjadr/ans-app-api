# ans_app_api.FormsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_forms_delete**](FormsApi.md#api_v2_assignments_assignment_id_forms_delete) | **DELETE** /api/v2/assignments/{assignment_id}/forms | Delete forms
[**api_v2_assignments_assignment_id_forms_get**](FormsApi.md#api_v2_assignments_assignment_id_forms_get) | **GET** /api/v2/assignments/{assignment_id}/forms | List forms

# **api_v2_assignments_assignment_id_forms_delete**
> api_v2_assignments_assignment_id_forms_delete(assignment_id)

Delete forms

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.FormsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id

try:
    # Delete forms
    api_instance.api_v2_assignments_assignment_id_forms_delete(assignment_id)
except ApiException as e:
    print("Exception when calling FormsApi->api_v2_assignments_assignment_id_forms_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_assignment_id_forms_get**
> list[InlineResponse2007] api_v2_assignments_assignment_id_forms_get(assignment_id, items=items, page=page)

List forms

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.FormsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List forms
    api_response = api_instance.api_v2_assignments_assignment_id_forms_get(assignment_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormsApi->api_v2_assignments_assignment_id_forms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2007]**](InlineResponse2007.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


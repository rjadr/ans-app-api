# ans_app_api.SchoolsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_schools_id_get**](SchoolsApi.md#api_v2_schools_id_get) | **GET** /api/v2/schools/{id} | Show school
[**api_v2_schools_id_patch**](SchoolsApi.md#api_v2_schools_id_patch) | **PATCH** /api/v2/schools/{id} | Update school

# **api_v2_schools_id_get**
> api_v2_schools_id_get(id)

Show school

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SchoolsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show school
    api_instance.api_v2_schools_id_get(id)
except ApiException as e:
    print("Exception when calling SchoolsApi->api_v2_schools_id_get: %s\n" % e)
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

# **api_v2_schools_id_patch**
> api_v2_schools_id_patch(id, body=body)

Update school

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SchoolsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.SchoolsIdBody() # SchoolsIdBody |  (optional)

try:
    # Update school
    api_instance.api_v2_schools_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling SchoolsApi->api_v2_schools_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**SchoolsIdBody**](SchoolsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


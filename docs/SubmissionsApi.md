# ans_app_api.SubmissionsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_submissions_id_get**](SubmissionsApi.md#api_v2_submissions_id_get) | **GET** /api/v2/submissions/{id} | Show submission
[**api_v2_submissions_id_patch**](SubmissionsApi.md#api_v2_submissions_id_patch) | **PATCH** /api/v2/submissions/{id} | Update submission

# **api_v2_submissions_id_get**
> InlineResponse20025 api_v2_submissions_id_get(id)

Show submission

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SubmissionsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show submission
    api_response = api_instance.api_v2_submissions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmissionsApi->api_v2_submissions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_submissions_id_patch**
> InlineResponse20025 api_v2_submissions_id_patch(id, body=body)

Update submission

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SubmissionsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.SubmissionsIdBody() # SubmissionsIdBody |  (optional)

try:
    # Update submission
    api_response = api_instance.api_v2_submissions_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmissionsApi->api_v2_submissions_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**SubmissionsIdBody**](SubmissionsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


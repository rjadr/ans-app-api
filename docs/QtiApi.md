# ans_app_api.QtiApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_qti_results_id_get**](QtiApi.md#api_v2_qti_results_id_get) | **GET** /api/v2/qti/results/{id} | QTI export

# **api_v2_qti_results_id_get**
> api_v2_qti_results_id_get(id)

QTI export

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QtiApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # QTI export
    api_instance.api_v2_qti_results_id_get(id)
except ApiException as e:
    print("Exception when calling QtiApi->api_v2_qti_results_id_get: %s\n" % e)
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
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


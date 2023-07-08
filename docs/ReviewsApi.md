# ans_app_api.ReviewsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_reviews_id_get**](ReviewsApi.md#api_v2_reviews_id_get) | **GET** /api/v2/reviews/{id} | Show review

# **api_v2_reviews_id_get**
> InlineResponse20023 api_v2_reviews_id_get(id)

Show review

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ReviewsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show review
    api_response = api_instance.api_v2_reviews_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReviewsApi->api_v2_reviews_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


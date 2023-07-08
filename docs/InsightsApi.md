# ans_app_api.InsightsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_insights_assignments_id_get**](InsightsApi.md#api_v2_insights_assignments_id_get) | **GET** /api/v2/insights/assignments/{id} | Show insights
[**api_v2_insights_questions_id_get**](InsightsApi.md#api_v2_insights_questions_id_get) | **GET** /api/v2/insights/questions/{id} | Show insights

# **api_v2_insights_assignments_id_get**
> InlineResponse20010 api_v2_insights_assignments_id_get(id)

Show insights

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.InsightsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | assignment_id

try:
    # Show insights
    api_response = api_instance.api_v2_insights_assignments_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightsApi->api_v2_insights_assignments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| assignment_id | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_insights_questions_id_get**
> InlineResponse20011 api_v2_insights_questions_id_get(id)

Show insights

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.InsightsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | question_id

try:
    # Show insights
    api_response = api_instance.api_v2_insights_questions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightsApi->api_v2_insights_questions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| question_id | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


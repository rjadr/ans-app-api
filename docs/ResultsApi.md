# ans_app_api.ResultsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_results_get**](ResultsApi.md#api_v2_assignments_assignment_id_results_get) | **GET** /api/v2/assignments/{assignment_id}/results | List results
[**api_v2_assignments_assignment_id_results_post**](ResultsApi.md#api_v2_assignments_assignment_id_results_post) | **POST** /api/v2/assignments/{assignment_id}/results | Create result
[**api_v2_results_id_delete**](ResultsApi.md#api_v2_results_id_delete) | **DELETE** /api/v2/results/{id} | Delete result
[**api_v2_results_id_get**](ResultsApi.md#api_v2_results_id_get) | **GET** /api/v2/results/{id} | Show result
[**api_v2_results_id_patch**](ResultsApi.md#api_v2_results_id_patch) | **PATCH** /api/v2/results/{id} | Update result

# **api_v2_assignments_assignment_id_results_get**
> list[InlineResponse20022] api_v2_assignments_assignment_id_results_get(assignment_id, items=items, page=page)

List results

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ResultsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List results
    api_response = api_instance.api_v2_assignments_assignment_id_results_get(assignment_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->api_v2_assignments_assignment_id_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20022]**](InlineResponse20022.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_assignment_id_results_post**
> InlineResponse2017 api_v2_assignments_assignment_id_results_post(assignment_id, body=body)

Create result

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ResultsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
body = ans_app_api.AssignmentIdResultsBody() # AssignmentIdResultsBody |  (optional)

try:
    # Create result
    api_response = api_instance.api_v2_assignments_assignment_id_results_post(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->api_v2_assignments_assignment_id_results_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **body** | [**AssignmentIdResultsBody**](AssignmentIdResultsBody.md)|  | [optional] 

### Return type

[**InlineResponse2017**](InlineResponse2017.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_id_delete**
> InlineResponse2017 api_v2_results_id_delete(id)

Delete result

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ResultsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete result
    api_response = api_instance.api_v2_results_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->api_v2_results_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2017**](InlineResponse2017.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_id_get**
> InlineResponse2017 api_v2_results_id_get(id)

Show result

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ResultsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show result
    api_response = api_instance.api_v2_results_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->api_v2_results_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2017**](InlineResponse2017.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_id_patch**
> api_v2_results_id_patch(id, body=body)

Update result

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ResultsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.ResultsIdBody() # ResultsIdBody |  (optional)

try:
    # Update result
    api_instance.api_v2_results_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling ResultsApi->api_v2_results_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**ResultsIdBody**](ResultsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


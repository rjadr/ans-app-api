# ans_app_api.TimeslotsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_timeslots_get**](TimeslotsApi.md#api_v2_assignments_assignment_id_timeslots_get) | **GET** /api/v2/assignments/{assignment_id}/timeslots | List timeslots
[**api_v2_assignments_assignment_id_timeslots_post**](TimeslotsApi.md#api_v2_assignments_assignment_id_timeslots_post) | **POST** /api/v2/assignments/{assignment_id}/timeslots | Create timeslot
[**api_v2_timeslots_id_delete**](TimeslotsApi.md#api_v2_timeslots_id_delete) | **DELETE** /api/v2/timeslots/{id} | Delete timeslot
[**api_v2_timeslots_id_get**](TimeslotsApi.md#api_v2_timeslots_id_get) | **GET** /api/v2/timeslots/{id} | Show timeslot
[**api_v2_timeslots_id_patch**](TimeslotsApi.md#api_v2_timeslots_id_patch) | **PATCH** /api/v2/timeslots/{id} | Update timeslot

# **api_v2_assignments_assignment_id_timeslots_get**
> list[InlineResponse20027] api_v2_assignments_assignment_id_timeslots_get(assignment_id, items=items, page=page)

List timeslots

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TimeslotsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List timeslots
    api_response = api_instance.api_v2_assignments_assignment_id_timeslots_get(assignment_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeslotsApi->api_v2_assignments_assignment_id_timeslots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20027]**](InlineResponse20027.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_assignment_id_timeslots_post**
> InlineResponse20027 api_v2_assignments_assignment_id_timeslots_post(assignment_id, body=body)

Create timeslot

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TimeslotsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
body = ans_app_api.AssignmentIdTimeslotsBody() # AssignmentIdTimeslotsBody |  (optional)

try:
    # Create timeslot
    api_response = api_instance.api_v2_assignments_assignment_id_timeslots_post(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeslotsApi->api_v2_assignments_assignment_id_timeslots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **body** | [**AssignmentIdTimeslotsBody**](AssignmentIdTimeslotsBody.md)|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_timeslots_id_delete**
> api_v2_timeslots_id_delete(id)

Delete timeslot

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TimeslotsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete timeslot
    api_instance.api_v2_timeslots_id_delete(id)
except ApiException as e:
    print("Exception when calling TimeslotsApi->api_v2_timeslots_id_delete: %s\n" % e)
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

# **api_v2_timeslots_id_get**
> InlineResponse20027 api_v2_timeslots_id_get(id)

Show timeslot

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TimeslotsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show timeslot
    api_response = api_instance.api_v2_timeslots_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeslotsApi->api_v2_timeslots_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_timeslots_id_patch**
> InlineResponse20027 api_v2_timeslots_id_patch(id, body=body)

Update timeslot

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TimeslotsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.TimeslotsIdBody() # TimeslotsIdBody |  (optional)

try:
    # Update timeslot
    api_response = api_instance.api_v2_timeslots_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeslotsApi->api_v2_timeslots_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**TimeslotsIdBody**](TimeslotsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


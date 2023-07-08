# ans_app_api.ExercisesApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_exercises_get**](ExercisesApi.md#api_v2_assignments_assignment_id_exercises_get) | **GET** /api/v2/assignments/{assignment_id}/exercises | List exercises
[**api_v2_assignments_assignment_id_exercises_post**](ExercisesApi.md#api_v2_assignments_assignment_id_exercises_post) | **POST** /api/v2/assignments/{assignment_id}/exercises | Create exercise
[**api_v2_exercises_id_delete**](ExercisesApi.md#api_v2_exercises_id_delete) | **DELETE** /api/v2/exercises/{id} | Delete exercise
[**api_v2_exercises_id_get**](ExercisesApi.md#api_v2_exercises_id_get) | **GET** /api/v2/exercises/{id} | Show exercise
[**api_v2_exercises_id_patch**](ExercisesApi.md#api_v2_exercises_id_patch) | **PATCH** /api/v2/exercises/{id} | Update exercise

# **api_v2_assignments_assignment_id_exercises_get**
> list[InlineResponse2006] api_v2_assignments_assignment_id_exercises_get(assignment_id, items=items, page=page)

List exercises

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ExercisesApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List exercises
    api_response = api_instance.api_v2_assignments_assignment_id_exercises_get(assignment_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExercisesApi->api_v2_assignments_assignment_id_exercises_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_assignment_id_exercises_post**
> InlineResponse2006 api_v2_assignments_assignment_id_exercises_post(assignment_id, body=body)

Create exercise

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ExercisesApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
body = ans_app_api.AssignmentIdExercisesBody() # AssignmentIdExercisesBody |  (optional)

try:
    # Create exercise
    api_response = api_instance.api_v2_assignments_assignment_id_exercises_post(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExercisesApi->api_v2_assignments_assignment_id_exercises_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **body** | [**AssignmentIdExercisesBody**](AssignmentIdExercisesBody.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_exercises_id_delete**
> InlineResponse2006 api_v2_exercises_id_delete(id)

Delete exercise

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ExercisesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete exercise
    api_response = api_instance.api_v2_exercises_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExercisesApi->api_v2_exercises_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_exercises_id_get**
> InlineResponse2006 api_v2_exercises_id_get(id)

Show exercise

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ExercisesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show exercise
    api_response = api_instance.api_v2_exercises_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExercisesApi->api_v2_exercises_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_exercises_id_patch**
> InlineResponse2006 api_v2_exercises_id_patch(id, body=body)

Update exercise

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ExercisesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.ExercisesIdBody() # ExercisesIdBody |  (optional)

try:
    # Update exercise
    api_response = api_instance.api_v2_exercises_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExercisesApi->api_v2_exercises_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**ExercisesIdBody**](ExercisesIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


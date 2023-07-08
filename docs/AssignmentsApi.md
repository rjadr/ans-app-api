# ans_app_api.AssignmentsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_id_delete**](AssignmentsApi.md#api_v2_assignments_id_delete) | **DELETE** /api/v2/assignments/{id} | Delete assignment
[**api_v2_assignments_id_get**](AssignmentsApi.md#api_v2_assignments_id_get) | **GET** /api/v2/assignments/{id} | Show assignment
[**api_v2_assignments_id_patch**](AssignmentsApi.md#api_v2_assignments_id_patch) | **PATCH** /api/v2/assignments/{id} | Update assignment
[**api_v2_courses_course_id_assignments_get**](AssignmentsApi.md#api_v2_courses_course_id_assignments_get) | **GET** /api/v2/courses/{course_id}/assignments | List assignments
[**api_v2_courses_course_id_assignments_post**](AssignmentsApi.md#api_v2_courses_course_id_assignments_post) | **POST** /api/v2/courses/{course_id}/assignments | Create assignment

# **api_v2_assignments_id_delete**
> api_v2_assignments_id_delete(id)

Delete assignment

Soft delete an assignment by moving it to removed assignments

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete assignment
    api_instance.api_v2_assignments_id_delete(id)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v2_assignments_id_delete: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_id_get**
> InlineResponse201 api_v2_assignments_id_get(id)

Show assignment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show assignment
    api_response = api_instance.api_v2_assignments_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v2_assignments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_id_patch**
> InlineResponse201 api_v2_assignments_id_patch(id, body=body)

Update assignment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.AssignmentsIdBody() # AssignmentsIdBody |  (optional)

try:
    # Update assignment
    api_response = api_instance.api_v2_assignments_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v2_assignments_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**AssignmentsIdBody**](AssignmentsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_courses_course_id_assignments_get**
> list[InlineResponse200] api_v2_courses_course_id_assignments_get(course_id)

List assignments

List all assignments in a course

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentsApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id

try:
    # List assignments
    api_response = api_instance.api_v2_courses_course_id_assignments_get(course_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v2_courses_course_id_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_courses_course_id_assignments_post**
> InlineResponse201 api_v2_courses_course_id_assignments_post(course_id, body=body)

Create assignment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentsApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id
body = ans_app_api.CourseIdAssignmentsBody() # CourseIdAssignmentsBody |  (optional)

try:
    # Create assignment
    api_response = api_instance.api_v2_courses_course_id_assignments_post(course_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v2_courses_course_id_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 
 **body** | [**CourseIdAssignmentsBody**](CourseIdAssignmentsBody.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


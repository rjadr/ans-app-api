# ans_app_api.CoursesApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_courses_id_delete**](CoursesApi.md#api_v2_courses_id_delete) | **DELETE** /api/v2/courses/{id} | Delete course
[**api_v2_courses_id_get**](CoursesApi.md#api_v2_courses_id_get) | **GET** /api/v2/courses/{id} | Show course
[**api_v2_courses_id_patch**](CoursesApi.md#api_v2_courses_id_patch) | **PATCH** /api/v2/courses/{id} | Update course
[**api_v2_schools_school_id_courses_get**](CoursesApi.md#api_v2_schools_school_id_courses_get) | **GET** /api/v2/schools/{school_id}/courses | List courses
[**api_v2_schools_school_id_courses_post**](CoursesApi.md#api_v2_schools_school_id_courses_post) | **POST** /api/v2/schools/{school_id}/courses | Create course

# **api_v2_courses_id_delete**
> api_v2_courses_id_delete(id)

Delete course

Soft delete a course by moving it to removed courses

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete course
    api_instance.api_v2_courses_id_delete(id)
except ApiException as e:
    print("Exception when calling CoursesApi->api_v2_courses_id_delete: %s\n" % e)
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

# **api_v2_courses_id_get**
> InlineResponse2012 api_v2_courses_id_get(id)

Show course

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show course
    api_response = api_instance.api_v2_courses_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->api_v2_courses_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_courses_id_patch**
> InlineResponse2012 api_v2_courses_id_patch(id, body=body)

Update course

To update from one role to another,         the user must first be removed from the current role list and with a new request added to the chosen role list

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.CoursesIdBody() # CoursesIdBody |  (optional)

try:
    # Update course
    api_response = api_instance.api_v2_courses_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->api_v2_courses_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**CoursesIdBody**](CoursesIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_courses_get**
> list[InlineResponse2003] api_v2_schools_school_id_courses_get(school_id, items=items, page=page)

List courses

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List courses
    api_response = api_instance.api_v2_schools_school_id_courses_get(school_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->api_v2_schools_school_id_courses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_courses_post**
> InlineResponse2012 api_v2_schools_school_id_courses_post(school_id, body=body)

Create course

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
body = ans_app_api.SchoolIdCoursesBody() # SchoolIdCoursesBody |  (optional)

try:
    # Create course
    api_response = api_instance.api_v2_schools_school_id_courses_post(school_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->api_v2_schools_school_id_courses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **body** | [**SchoolIdCoursesBody**](SchoolIdCoursesBody.md)|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ans_app_api.CoursesClassesApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_classes_class_id_courses_classes_get**](CoursesClassesApi.md#api_v2_classes_class_id_courses_classes_get) | **GET** /api/v2/classes/{class_id}/courses_classes | List courses in class
[**api_v2_classes_class_id_courses_classes_post**](CoursesClassesApi.md#api_v2_classes_class_id_courses_classes_post) | **POST** /api/v2/classes/{class_id}/courses_classes | Add course to class
[**api_v2_courses_classes_id_delete**](CoursesClassesApi.md#api_v2_courses_classes_id_delete) | **DELETE** /api/v2/courses_classes/{id} | Delete courses class
[**api_v2_courses_course_id_courses_classes_get**](CoursesClassesApi.md#api_v2_courses_course_id_courses_classes_get) | **GET** /api/v2/courses/{course_id}/courses_classes | List classes in course
[**api_v2_courses_course_id_courses_classes_post**](CoursesClassesApi.md#api_v2_courses_course_id_courses_classes_post) | **POST** /api/v2/courses/{course_id}/courses_classes | Add class to course

# **api_v2_classes_class_id_courses_classes_get**
> list[InlineResponse2002] api_v2_classes_class_id_courses_classes_get(class_id, items=items, page=page)

List courses in class

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesClassesApi(ans_app_api.ApiClient(configuration))
class_id = 'class_id_example' # str | class_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List courses in class
    api_response = api_instance.api_v2_classes_class_id_courses_classes_get(class_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesClassesApi->api_v2_classes_class_id_courses_classes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_id** | **str**| class_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_classes_class_id_courses_classes_post**
> InlineResponse2002 api_v2_classes_class_id_courses_classes_post(class_id, body=body)

Add course to class

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesClassesApi(ans_app_api.ApiClient(configuration))
class_id = 'class_id_example' # str | class_id
body = ans_app_api.ClassIdCoursesClassesBody() # ClassIdCoursesClassesBody |  (optional)

try:
    # Add course to class
    api_response = api_instance.api_v2_classes_class_id_courses_classes_post(class_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesClassesApi->api_v2_classes_class_id_courses_classes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_id** | **str**| class_id | 
 **body** | [**ClassIdCoursesClassesBody**](ClassIdCoursesClassesBody.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_courses_classes_id_delete**
> api_v2_courses_classes_id_delete(id)

Delete courses class

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesClassesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete courses class
    api_instance.api_v2_courses_classes_id_delete(id)
except ApiException as e:
    print("Exception when calling CoursesClassesApi->api_v2_courses_classes_id_delete: %s\n" % e)
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

# **api_v2_courses_course_id_courses_classes_get**
> list[InlineResponse2002] api_v2_courses_course_id_courses_classes_get(course_id, items=items, page=page)

List classes in course

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesClassesApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List classes in course
    api_response = api_instance.api_v2_courses_course_id_courses_classes_get(course_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesClassesApi->api_v2_courses_course_id_courses_classes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_courses_course_id_courses_classes_post**
> InlineResponse2002 api_v2_courses_course_id_courses_classes_post(course_id, body=body)

Add class to course

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesClassesApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id
body = ans_app_api.CourseIdCoursesClassesBody() # CourseIdCoursesClassesBody |  (optional)

try:
    # Add class to course
    api_response = api_instance.api_v2_courses_course_id_courses_classes_post(course_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesClassesApi->api_v2_courses_course_id_courses_classes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 
 **body** | [**CourseIdCoursesClassesBody**](CourseIdCoursesClassesBody.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


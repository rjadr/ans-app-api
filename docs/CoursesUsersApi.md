# ans_app_api.CoursesUsersApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_courses_course_id_courses_users_get**](CoursesUsersApi.md#api_v2_courses_course_id_courses_users_get) | **GET** /api/v2/courses/{course_id}/courses_users | List course users
[**api_v2_courses_course_id_courses_users_post**](CoursesUsersApi.md#api_v2_courses_course_id_courses_users_post) | **POST** /api/v2/courses/{course_id}/courses_users | Add user to course
[**api_v2_courses_users_id_delete**](CoursesUsersApi.md#api_v2_courses_users_id_delete) | **DELETE** /api/v2/courses_users/{id} | Delete courses user
[**api_v2_courses_users_id_get**](CoursesUsersApi.md#api_v2_courses_users_id_get) | **GET** /api/v2/courses_users/{id} | Show courses user
[**api_v2_courses_users_id_patch**](CoursesUsersApi.md#api_v2_courses_users_id_patch) | **PATCH** /api/v2/courses_users/{id} | Update courses user
[**api_v2_users_user_id_courses_users_get**](CoursesUsersApi.md#api_v2_users_user_id_courses_users_get) | **GET** /api/v2/users/{user_id}/courses_users | List user courses
[**api_v2_users_user_id_courses_users_post**](CoursesUsersApi.md#api_v2_users_user_id_courses_users_post) | **POST** /api/v2/users/{user_id}/courses_users | Add user to course

# **api_v2_courses_course_id_courses_users_get**
> api_v2_courses_course_id_courses_users_get(course_id, items=items, page=page)

List course users

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesUsersApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List course users
    api_instance.api_v2_courses_course_id_courses_users_get(course_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling CoursesUsersApi->api_v2_courses_course_id_courses_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_courses_course_id_courses_users_post**
> InlineResponse2013 api_v2_courses_course_id_courses_users_post(course_id, body=body)

Add user to course

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesUsersApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id
body = ans_app_api.CourseIdCoursesUsersBody() # CourseIdCoursesUsersBody |  (optional)

try:
    # Add user to course
    api_response = api_instance.api_v2_courses_course_id_courses_users_post(course_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesUsersApi->api_v2_courses_course_id_courses_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 
 **body** | [**CourseIdCoursesUsersBody**](CourseIdCoursesUsersBody.md)|  | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_courses_users_id_delete**
> api_v2_courses_users_id_delete(id)

Delete courses user

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesUsersApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete courses user
    api_instance.api_v2_courses_users_id_delete(id)
except ApiException as e:
    print("Exception when calling CoursesUsersApi->api_v2_courses_users_id_delete: %s\n" % e)
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

# **api_v2_courses_users_id_get**
> InlineResponse2013 api_v2_courses_users_id_get(id)

Show courses user

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesUsersApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show courses user
    api_response = api_instance.api_v2_courses_users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesUsersApi->api_v2_courses_users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_courses_users_id_patch**
> InlineResponse2013 api_v2_courses_users_id_patch(id, body=body)

Update courses user

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesUsersApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.CoursesUsersIdBody() # CoursesUsersIdBody |  (optional)

try:
    # Update courses user
    api_response = api_instance.api_v2_courses_users_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesUsersApi->api_v2_courses_users_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**CoursesUsersIdBody**](CoursesUsersIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_users_user_id_courses_users_get**
> api_v2_users_user_id_courses_users_get(user_id, items=items, page=page)

List user courses

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesUsersApi(ans_app_api.ApiClient(configuration))
user_id = 'user_id_example' # str | user_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List user courses
    api_instance.api_v2_users_user_id_courses_users_get(user_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling CoursesUsersApi->api_v2_users_user_id_courses_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_users_user_id_courses_users_post**
> InlineResponse2013 api_v2_users_user_id_courses_users_post(user_id, body=body)

Add user to course

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoursesUsersApi(ans_app_api.ApiClient(configuration))
user_id = 'user_id_example' # str | user_id
body = ans_app_api.UserIdCoursesUsersBody() # UserIdCoursesUsersBody |  (optional)

try:
    # Add user to course
    api_response = api_instance.api_v2_users_user_id_courses_users_post(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesUsersApi->api_v2_users_user_id_courses_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user_id | 
 **body** | [**UserIdCoursesUsersBody**](UserIdCoursesUsersBody.md)|  | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


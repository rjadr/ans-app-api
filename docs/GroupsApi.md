# ans_app_api.GroupsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_courses_course_id_groups_get**](GroupsApi.md#api_v2_courses_course_id_groups_get) | **GET** /api/v2/courses/{course_id}/groups | List groups
[**api_v2_courses_course_id_groups_post**](GroupsApi.md#api_v2_courses_course_id_groups_post) | **POST** /api/v2/courses/{course_id}/groups | Create group
[**api_v2_groups_id_delete**](GroupsApi.md#api_v2_groups_id_delete) | **DELETE** /api/v2/groups/{id} | Delete group
[**api_v2_groups_id_get**](GroupsApi.md#api_v2_groups_id_get) | **GET** /api/v2/groups/{id} | Show group
[**api_v2_groups_id_patch**](GroupsApi.md#api_v2_groups_id_patch) | **PATCH** /api/v2/groups/{id} | Update group

# **api_v2_courses_course_id_groups_get**
> list[InlineResponse2008] api_v2_courses_course_id_groups_get(course_id, items=items, page=page)

List groups

List all groups in a course

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List groups
    api_response = api_instance.api_v2_courses_course_id_groups_get(course_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->api_v2_courses_course_id_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2008]**](InlineResponse2008.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_courses_course_id_groups_post**
> InlineResponse2015 api_v2_courses_course_id_groups_post(course_id, body=body)

Create group

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id
body = ans_app_api.CourseIdGroupsBody() # CourseIdGroupsBody |  (optional)

try:
    # Create group
    api_response = api_instance.api_v2_courses_course_id_groups_post(course_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->api_v2_courses_course_id_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 
 **body** | [**CourseIdGroupsBody**](CourseIdGroupsBody.md)|  | [optional] 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_groups_id_delete**
> api_v2_groups_id_delete(id)

Delete group

Delete a group. You can not delete a group that has a result.

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete group
    api_instance.api_v2_groups_id_delete(id)
except ApiException as e:
    print("Exception when calling GroupsApi->api_v2_groups_id_delete: %s\n" % e)
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

# **api_v2_groups_id_get**
> InlineResponse2015 api_v2_groups_id_get(id)

Show group

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show group
    api_response = api_instance.api_v2_groups_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->api_v2_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_groups_id_patch**
> InlineResponse2015 api_v2_groups_id_patch(id, body=body)

Update group

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.GroupsIdBody() # GroupsIdBody |  (optional)

try:
    # Update group
    api_response = api_instance.api_v2_groups_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->api_v2_groups_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**GroupsIdBody**](GroupsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


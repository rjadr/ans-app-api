# ans_app_api.GroupsUsersApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_groups_group_id_groups_users_get**](GroupsUsersApi.md#api_v2_groups_group_id_groups_users_get) | **GET** /api/v2/groups/{group_id}/groups_users | List users in group
[**api_v2_groups_group_id_groups_users_post**](GroupsUsersApi.md#api_v2_groups_group_id_groups_users_post) | **POST** /api/v2/groups/{group_id}/groups_users | Add user to group
[**api_v2_groups_users_id_delete**](GroupsUsersApi.md#api_v2_groups_users_id_delete) | **DELETE** /api/v2/groups_users/{id} | Remove user from group
[**api_v2_users_user_id_groups_users_get**](GroupsUsersApi.md#api_v2_users_user_id_groups_users_get) | **GET** /api/v2/users/{user_id}/groups_users | List groups of user
[**api_v2_users_user_id_groups_users_post**](GroupsUsersApi.md#api_v2_users_user_id_groups_users_post) | **POST** /api/v2/users/{user_id}/groups_users | Add user to group

# **api_v2_groups_group_id_groups_users_get**
> list[InlineResponse2009] api_v2_groups_group_id_groups_users_get(group_id, items=items, page=page)

List users in group

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsUsersApi(ans_app_api.ApiClient(configuration))
group_id = 'group_id_example' # str | group_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List users in group
    api_response = api_instance.api_v2_groups_group_id_groups_users_get(group_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsUsersApi->api_v2_groups_group_id_groups_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| group_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2009]**](InlineResponse2009.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_groups_group_id_groups_users_post**
> InlineResponse2009 api_v2_groups_group_id_groups_users_post(group_id, body=body)

Add user to group

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsUsersApi(ans_app_api.ApiClient(configuration))
group_id = 'group_id_example' # str | group_id
body = ans_app_api.GroupIdGroupsUsersBody() # GroupIdGroupsUsersBody |  (optional)

try:
    # Add user to group
    api_response = api_instance.api_v2_groups_group_id_groups_users_post(group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsUsersApi->api_v2_groups_group_id_groups_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| group_id | 
 **body** | [**GroupIdGroupsUsersBody**](GroupIdGroupsUsersBody.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_groups_users_id_delete**
> api_v2_groups_users_id_delete(id)

Remove user from group

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsUsersApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Remove user from group
    api_instance.api_v2_groups_users_id_delete(id)
except ApiException as e:
    print("Exception when calling GroupsUsersApi->api_v2_groups_users_id_delete: %s\n" % e)
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

# **api_v2_users_user_id_groups_users_get**
> list[InlineResponse2009] api_v2_users_user_id_groups_users_get(user_id, items=items, page=page)

List groups of user

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsUsersApi(ans_app_api.ApiClient(configuration))
user_id = 'user_id_example' # str | user_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List groups of user
    api_response = api_instance.api_v2_users_user_id_groups_users_get(user_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsUsersApi->api_v2_users_user_id_groups_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2009]**](InlineResponse2009.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_users_user_id_groups_users_post**
> InlineResponse2009 api_v2_users_user_id_groups_users_post(user_id, body=body)

Add user to group

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.GroupsUsersApi(ans_app_api.ApiClient(configuration))
user_id = 'user_id_example' # str | user_id
body = ans_app_api.UserIdGroupsUsersBody() # UserIdGroupsUsersBody |  (optional)

try:
    # Add user to group
    api_response = api_instance.api_v2_users_user_id_groups_users_post(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsUsersApi->api_v2_users_user_id_groups_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user_id | 
 **body** | [**UserIdGroupsUsersBody**](UserIdGroupsUsersBody.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


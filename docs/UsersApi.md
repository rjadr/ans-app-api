# ans_app_api.UsersApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_schools_school_id_users_get**](UsersApi.md#api_v2_schools_school_id_users_get) | **GET** /api/v2/schools/{school_id}/users | List users
[**api_v2_schools_school_id_users_post**](UsersApi.md#api_v2_schools_school_id_users_post) | **POST** /api/v2/schools/{school_id}/users | Create user
[**api_v2_users_id_delete**](UsersApi.md#api_v2_users_id_delete) | **DELETE** /api/v2/users/{id} | Delete user
[**api_v2_users_id_get**](UsersApi.md#api_v2_users_id_get) | **GET** /api/v2/users/{id} | Show user
[**api_v2_users_id_patch**](UsersApi.md#api_v2_users_id_patch) | **PATCH** /api/v2/users/{id} | Update user

# **api_v2_schools_school_id_users_get**
> list[InlineResponse20028] api_v2_schools_school_id_users_get(school_id, items=items, page=page)

List users

List all users of the school

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.UsersApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List users
    api_response = api_instance.api_v2_schools_school_id_users_get(school_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v2_schools_school_id_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20028]**](InlineResponse20028.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_users_post**
> InlineResponse20029 api_v2_schools_school_id_users_post(school_id, body=body)

Create user

Create a new user. If an existing user is found based on the email or student number, the existing user is returned with status 200. Empty attributes are filled with the provided information, but existing attributes are not overwritten.

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.UsersApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
body = ans_app_api.SchoolIdUsersBody() # SchoolIdUsersBody |  (optional)

try:
    # Create user
    api_response = api_instance.api_v2_schools_school_id_users_post(school_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v2_schools_school_id_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **body** | [**SchoolIdUsersBody**](SchoolIdUsersBody.md)|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_users_id_delete**
> api_v2_users_id_delete(id)

Delete user

Soft delete a user by clearing all attributes except student number

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.UsersApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete user
    api_instance.api_v2_users_id_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->api_v2_users_id_delete: %s\n" % e)
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

# **api_v2_users_id_get**
> InlineResponse20029 api_v2_users_id_get(id)

Show user

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.UsersApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show user
    api_response = api_instance.api_v2_users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v2_users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_users_id_patch**
> InlineResponse20029 api_v2_users_id_patch(id, body=body)

Update user

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.UsersApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.UsersIdBody() # UsersIdBody |  (optional)

try:
    # Update user
    api_response = api_instance.api_v2_users_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v2_users_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**UsersIdBody**](UsersIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


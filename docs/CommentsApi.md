# ans_app_api.CommentsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_comments_get**](CommentsApi.md#api_v2_comments_get) | **GET** /api/v2/comments | List comments
[**api_v2_comments_id_delete**](CommentsApi.md#api_v2_comments_id_delete) | **DELETE** /api/v2/comments/{id} | Destroy comment
[**api_v2_comments_id_get**](CommentsApi.md#api_v2_comments_id_get) | **GET** /api/v2/comments/{id} | Show comment
[**api_v2_comments_id_patch**](CommentsApi.md#api_v2_comments_id_patch) | **PATCH** /api/v2/comments/{id} | Update comment
[**api_v2_comments_post**](CommentsApi.md#api_v2_comments_post) | **POST** /api/v2/comments | Create comment

# **api_v2_comments_get**
> api_v2_comments_get(items=items, page=page)

List comments

List all your comments

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CommentsApi(ans_app_api.ApiClient(configuration))
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List comments
    api_instance.api_v2_comments_get(items=items, page=page)
except ApiException as e:
    print("Exception when calling CommentsApi->api_v2_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **api_v2_comments_id_delete**
> api_v2_comments_id_delete(id)

Destroy comment

Destroy a comment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CommentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Destroy comment
    api_instance.api_v2_comments_id_delete(id)
except ApiException as e:
    print("Exception when calling CommentsApi->api_v2_comments_id_delete: %s\n" % e)
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

# **api_v2_comments_id_get**
> api_v2_comments_id_get(id)

Show comment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CommentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show comment
    api_instance.api_v2_comments_id_get(id)
except ApiException as e:
    print("Exception when calling CommentsApi->api_v2_comments_id_get: %s\n" % e)
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

# **api_v2_comments_id_patch**
> api_v2_comments_id_patch(id, body=body)

Update comment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CommentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.CommentsIdBody() # CommentsIdBody |  (optional)

try:
    # Update comment
    api_instance.api_v2_comments_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling CommentsApi->api_v2_comments_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**CommentsIdBody**](CommentsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_comments_post**
> api_v2_comments_post(body=body)

Create comment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CommentsApi(ans_app_api.ApiClient(configuration))
body = ans_app_api.V2CommentsBody() # V2CommentsBody |  (optional)

try:
    # Create comment
    api_instance.api_v2_comments_post(body=body)
except ApiException as e:
    print("Exception when calling CommentsApi->api_v2_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2CommentsBody**](V2CommentsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ans_app_api.ClassesApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_classes_id_delete**](ClassesApi.md#api_v2_classes_id_delete) | **DELETE** /api/v2/classes/{id} | Delete class
[**api_v2_classes_id_get**](ClassesApi.md#api_v2_classes_id_get) | **GET** /api/v2/classes/{id} | Show class
[**api_v2_classes_id_patch**](ClassesApi.md#api_v2_classes_id_patch) | **PATCH** /api/v2/classes/{id} | Update class
[**api_v2_schools_school_id_classes_get**](ClassesApi.md#api_v2_schools_school_id_classes_get) | **GET** /api/v2/schools/{school_id}/classes | List Classes
[**api_v2_schools_school_id_classes_post**](ClassesApi.md#api_v2_schools_school_id_classes_post) | **POST** /api/v2/schools/{school_id}/classes | Create classes

# **api_v2_classes_id_delete**
> InlineResponse2011 api_v2_classes_id_delete(id)

Delete class

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ClassesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete class
    api_response = api_instance.api_v2_classes_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->api_v2_classes_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_classes_id_get**
> InlineResponse2011 api_v2_classes_id_get(id)

Show class

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ClassesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show class
    api_response = api_instance.api_v2_classes_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->api_v2_classes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_classes_id_patch**
> InlineResponse2011 api_v2_classes_id_patch(id, body=body)

Update class

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ClassesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.ClassesIdBody() # ClassesIdBody |  (optional)

try:
    # Update class
    api_response = api_instance.api_v2_classes_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->api_v2_classes_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**ClassesIdBody**](ClassesIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_classes_get**
> list[InlineResponse2001] api_v2_schools_school_id_classes_get(school_id, items=items, page=page)

List Classes

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ClassesApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List Classes
    api_response = api_instance.api_v2_schools_school_id_classes_get(school_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->api_v2_schools_school_id_classes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_classes_post**
> InlineResponse2011 api_v2_schools_school_id_classes_post(school_id, body=body)

Create classes

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ClassesApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
body = ans_app_api.SchoolIdClassesBody() # SchoolIdClassesBody |  (optional)

try:
    # Create classes
    api_response = api_instance.api_v2_schools_school_id_classes_post(school_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->api_v2_schools_school_id_classes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **body** | [**SchoolIdClassesBody**](SchoolIdClassesBody.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


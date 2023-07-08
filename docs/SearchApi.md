# ans_app_api.SearchApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_search_assignments_get**](SearchApi.md#api_v2_search_assignments_get) | **GET** /api/v2/search/assignments | Search assignments
[**api_v2_search_courses_get**](SearchApi.md#api_v2_search_courses_get) | **GET** /api/v2/search/courses | Search courses
[**api_v2_search_groups_get**](SearchApi.md#api_v2_search_groups_get) | **GET** /api/v2/search/groups | Search groups
[**api_v2_search_question_bank_assignments_get**](SearchApi.md#api_v2_search_question_bank_assignments_get) | **GET** /api/v2/search/question_bank_assignments | Search question bank assignments
[**api_v2_search_question_banks_get**](SearchApi.md#api_v2_search_question_banks_get) | **GET** /api/v2/search/question_banks | Search question banks
[**api_v2_search_results_get**](SearchApi.md#api_v2_search_results_get) | **GET** /api/v2/search/results | Search results
[**api_v2_search_timeslots_get**](SearchApi.md#api_v2_search_timeslots_get) | **GET** /api/v2/search/timeslots | Search timeslots
[**api_v2_search_users_get**](SearchApi.md#api_v2_search_users_get) | **GET** /api/v2/search/users | Search users

# **api_v2_search_assignments_get**
> api_v2_search_assignments_get(query=query, items=items, page=page)

Search assignments

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SearchApi(ans_app_api.ApiClient(configuration))
query = 'query_example' # str | Search query (optional)
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Search assignments
    api_instance.api_v2_search_assignments_get(query=query, items=items, page=page)
except ApiException as e:
    print("Exception when calling SearchApi->api_v2_search_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | [optional] 
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

# **api_v2_search_courses_get**
> api_v2_search_courses_get(query=query, items=items, page=page)

Search courses

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SearchApi(ans_app_api.ApiClient(configuration))
query = 'query_example' # str | Search query (optional)
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Search courses
    api_instance.api_v2_search_courses_get(query=query, items=items, page=page)
except ApiException as e:
    print("Exception when calling SearchApi->api_v2_search_courses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | [optional] 
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

# **api_v2_search_groups_get**
> api_v2_search_groups_get(query=query, items=items, page=page)

Search groups

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SearchApi(ans_app_api.ApiClient(configuration))
query = 'query_example' # str | Search query (optional)
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Search groups
    api_instance.api_v2_search_groups_get(query=query, items=items, page=page)
except ApiException as e:
    print("Exception when calling SearchApi->api_v2_search_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | [optional] 
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

# **api_v2_search_question_bank_assignments_get**
> api_v2_search_question_bank_assignments_get(query=query, items=items, page=page)

Search question bank assignments

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SearchApi(ans_app_api.ApiClient(configuration))
query = 'query_example' # str | Search query (optional)
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Search question bank assignments
    api_instance.api_v2_search_question_bank_assignments_get(query=query, items=items, page=page)
except ApiException as e:
    print("Exception when calling SearchApi->api_v2_search_question_bank_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | [optional] 
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

# **api_v2_search_question_banks_get**
> api_v2_search_question_banks_get(query=query, items=items, page=page)

Search question banks

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SearchApi(ans_app_api.ApiClient(configuration))
query = 'query_example' # str | Search query (optional)
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Search question banks
    api_instance.api_v2_search_question_banks_get(query=query, items=items, page=page)
except ApiException as e:
    print("Exception when calling SearchApi->api_v2_search_question_banks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | [optional] 
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

# **api_v2_search_results_get**
> api_v2_search_results_get(query=query, items=items, page=page)

Search results

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SearchApi(ans_app_api.ApiClient(configuration))
query = 'query_example' # str | Search query (optional)
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Search results
    api_instance.api_v2_search_results_get(query=query, items=items, page=page)
except ApiException as e:
    print("Exception when calling SearchApi->api_v2_search_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | [optional] 
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

# **api_v2_search_timeslots_get**
> api_v2_search_timeslots_get(query=query, items=items, page=page)

Search timeslots

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SearchApi(ans_app_api.ApiClient(configuration))
query = 'query_example' # str | Search query (optional)
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Search timeslots
    api_instance.api_v2_search_timeslots_get(query=query, items=items, page=page)
except ApiException as e:
    print("Exception when calling SearchApi->api_v2_search_timeslots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | [optional] 
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

# **api_v2_search_users_get**
> api_v2_search_users_get(query=query, items=items, page=page)

Search users

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SearchApi(ans_app_api.ApiClient(configuration))
query = 'query_example' # str | Search query (optional)
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Search users
    api_instance.api_v2_search_users_get(query=query, items=items, page=page)
except ApiException as e:
    print("Exception when calling SearchApi->api_v2_search_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | [optional] 
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


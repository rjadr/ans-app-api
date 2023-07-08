# ans_app_api.LogsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_logs_assignments_id_get**](LogsApi.md#api_v2_logs_assignments_id_get) | **GET** /api/v2/logs/assignments/{id} | Show assignment log
[**api_v2_logs_courses_id_get**](LogsApi.md#api_v2_logs_courses_id_get) | **GET** /api/v2/logs/courses/{id} | Show course log
[**api_v2_logs_courses_users_id_get**](LogsApi.md#api_v2_logs_courses_users_id_get) | **GET** /api/v2/logs/courses_users/{id} | Show courses users log
[**api_v2_logs_responses_id_get**](LogsApi.md#api_v2_logs_responses_id_get) | **GET** /api/v2/logs/responses/{id} | Show response log
[**api_v2_logs_results_id_get**](LogsApi.md#api_v2_logs_results_id_get) | **GET** /api/v2/logs/results/{id} | Show result log
[**api_v2_logs_schools_id_get**](LogsApi.md#api_v2_logs_schools_id_get) | **GET** /api/v2/logs/schools/{id} | Show school log
[**api_v2_logs_submissions_id_get**](LogsApi.md#api_v2_logs_submissions_id_get) | **GET** /api/v2/logs/submissions/{id} | Show submission log
[**api_v2_logs_subsets_id_get**](LogsApi.md#api_v2_logs_subsets_id_get) | **GET** /api/v2/logs/subsets/{id} | Show subset log
[**api_v2_logs_users_id_get**](LogsApi.md#api_v2_logs_users_id_get) | **GET** /api/v2/logs/users/{id} | Show user log

# **api_v2_logs_assignments_id_get**
> list[InlineResponse20013] api_v2_logs_assignments_id_get(id, items=items, page=page)

Show assignment log

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LogsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Show assignment log
    api_response = api_instance.api_v2_logs_assignments_id_get(id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->api_v2_logs_assignments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_logs_courses_id_get**
> list[InlineResponse20013] api_v2_logs_courses_id_get(id, items=items, page=page)

Show course log

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LogsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Show course log
    api_response = api_instance.api_v2_logs_courses_id_get(id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->api_v2_logs_courses_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_logs_courses_users_id_get**
> list[InlineResponse20013] api_v2_logs_courses_users_id_get(id, items=items, page=page)

Show courses users log

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LogsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Show courses users log
    api_response = api_instance.api_v2_logs_courses_users_id_get(id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->api_v2_logs_courses_users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_logs_responses_id_get**
> list[InlineResponse20013] api_v2_logs_responses_id_get(id, items=items, page=page)

Show response log

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LogsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Show response log
    api_response = api_instance.api_v2_logs_responses_id_get(id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->api_v2_logs_responses_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_logs_results_id_get**
> list[InlineResponse20013] api_v2_logs_results_id_get(id, items=items, page=page)

Show result log

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LogsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Show result log
    api_response = api_instance.api_v2_logs_results_id_get(id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->api_v2_logs_results_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_logs_schools_id_get**
> list[InlineResponse20013] api_v2_logs_schools_id_get(id, items=items, page=page)

Show school log

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LogsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Show school log
    api_response = api_instance.api_v2_logs_schools_id_get(id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->api_v2_logs_schools_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_logs_submissions_id_get**
> list[InlineResponse20013] api_v2_logs_submissions_id_get(id, items=items, page=page)

Show submission log

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LogsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Show submission log
    api_response = api_instance.api_v2_logs_submissions_id_get(id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->api_v2_logs_submissions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_logs_subsets_id_get**
> list[InlineResponse20013] api_v2_logs_subsets_id_get(id, items=items, page=page)

Show subset log

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LogsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Show subset log
    api_response = api_instance.api_v2_logs_subsets_id_get(id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->api_v2_logs_subsets_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_logs_users_id_get**
> list[InlineResponse20013] api_v2_logs_users_id_get(id, items=items, page=page)

Show user log

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.LogsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # Show user log
    api_response = api_instance.api_v2_logs_users_id_get(id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->api_v2_logs_users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ans_app_api.BackgroundJobsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_background_jobs_get**](BackgroundJobsApi.md#api_v2_background_jobs_get) | **GET** /api/v2/background_jobs | List background jobs
[**api_v2_background_jobs_id_get**](BackgroundJobsApi.md#api_v2_background_jobs_id_get) | **GET** /api/v2/background_jobs/{id} | Show background job
[**api_v2_background_jobs_id_patch**](BackgroundJobsApi.md#api_v2_background_jobs_id_patch) | **PATCH** /api/v2/background_jobs/{id} | Update background job

# **api_v2_background_jobs_get**
> api_v2_background_jobs_get(items=items, page=page)

List background jobs

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.BackgroundJobsApi(ans_app_api.ApiClient(configuration))
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List background jobs
    api_instance.api_v2_background_jobs_get(items=items, page=page)
except ApiException as e:
    print("Exception when calling BackgroundJobsApi->api_v2_background_jobs_get: %s\n" % e)
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

# **api_v2_background_jobs_id_get**
> api_v2_background_jobs_id_get(id)

Show background job

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.BackgroundJobsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show background job
    api_instance.api_v2_background_jobs_id_get(id)
except ApiException as e:
    print("Exception when calling BackgroundJobsApi->api_v2_background_jobs_id_get: %s\n" % e)
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

# **api_v2_background_jobs_id_patch**
> api_v2_background_jobs_id_patch(id, body=body)

Update background job

To start the processing of an initialized background job after you uploaded the file, you must update the status to \"pending\". You can only update background jobs you created yourself and that currently have the \"initialized\" status.

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.BackgroundJobsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.BackgroundJobsIdBody() # BackgroundJobsIdBody |  (optional)

try:
    # Update background job
    api_instance.api_v2_background_jobs_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling BackgroundJobsApi->api_v2_background_jobs_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**BackgroundJobsIdBody**](BackgroundJobsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


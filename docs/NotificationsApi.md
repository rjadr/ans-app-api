# ans_app_api.NotificationsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_notifications_get**](NotificationsApi.md#api_v2_notifications_get) | **GET** /api/v2/notifications | List notifications
[**api_v2_notifications_id_get**](NotificationsApi.md#api_v2_notifications_id_get) | **GET** /api/v2/notifications/{id} | Show notification

# **api_v2_notifications_get**
> api_v2_notifications_get(items=items, page=page)

List notifications

List all your notifications

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.NotificationsApi(ans_app_api.ApiClient(configuration))
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List notifications
    api_instance.api_v2_notifications_get(items=items, page=page)
except ApiException as e:
    print("Exception when calling NotificationsApi->api_v2_notifications_get: %s\n" % e)
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

# **api_v2_notifications_id_get**
> api_v2_notifications_id_get(id)

Show notification

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.NotificationsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show notification
    api_instance.api_v2_notifications_id_get(id)
except ApiException as e:
    print("Exception when calling NotificationsApi->api_v2_notifications_id_get: %s\n" % e)
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


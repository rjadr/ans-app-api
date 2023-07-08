# ans_app_api.WebhooksApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_webhooks_get**](WebhooksApi.md#api_v2_webhooks_get) | **GET** /api/v2/webhooks/ | List webhooks
[**api_v2_webhooks_id_delete**](WebhooksApi.md#api_v2_webhooks_id_delete) | **DELETE** /api/v2/webhooks/{id} | Delete webhook
[**api_v2_webhooks_id_get**](WebhooksApi.md#api_v2_webhooks_id_get) | **GET** /api/v2/webhooks/{id} | Show webhook
[**api_v2_webhooks_id_patch**](WebhooksApi.md#api_v2_webhooks_id_patch) | **PATCH** /api/v2/webhooks/{id} | Update webhook
[**api_v2_webhooks_post**](WebhooksApi.md#api_v2_webhooks_post) | **POST** /api/v2/webhooks/ | Create webhook

# **api_v2_webhooks_get**
> list[InlineResponse20030] api_v2_webhooks_get(items=items, page=page)

List webhooks

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.WebhooksApi(ans_app_api.ApiClient(configuration))
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List webhooks
    api_response = api_instance.api_v2_webhooks_get(items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v2_webhooks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20030]**](InlineResponse20030.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_id_delete**
> InlineResponse2018 api_v2_webhooks_id_delete(id)

Delete webhook

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.WebhooksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete webhook
    api_response = api_instance.api_v2_webhooks_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v2_webhooks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2018**](InlineResponse2018.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_id_get**
> InlineResponse2018 api_v2_webhooks_id_get(id)

Show webhook

View webhook attributes and the last 5 events that occurent on the webhook

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.WebhooksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show webhook
    api_response = api_instance.api_v2_webhooks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v2_webhooks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2018**](InlineResponse2018.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_id_patch**
> InlineResponse2018 api_v2_webhooks_id_patch(id, body=body)

Update webhook

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.WebhooksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.WebhooksIdBody() # WebhooksIdBody |  (optional)

try:
    # Update webhook
    api_response = api_instance.api_v2_webhooks_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v2_webhooks_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**WebhooksIdBody**](WebhooksIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2018**](InlineResponse2018.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_post**
> InlineResponse2018 api_v2_webhooks_post(body=body)

Create webhook

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.WebhooksApi(ans_app_api.ApiClient(configuration))
body = ans_app_api.V2WebhooksBody() # V2WebhooksBody |  (optional)

try:
    # Create webhook
    api_response = api_instance.api_v2_webhooks_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v2_webhooks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2WebhooksBody**](V2WebhooksBody.md)|  | [optional] 

### Return type

[**InlineResponse2018**](InlineResponse2018.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


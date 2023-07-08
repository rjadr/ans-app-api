# ans_app_api.SubscriptionsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_plans_plan_id_subscriptions_get**](SubscriptionsApi.md#api_v2_plans_plan_id_subscriptions_get) | **GET** /api/v2/plans/{plan_id}/subscriptions | List subscriptions
[**api_v2_plans_plan_id_subscriptions_post**](SubscriptionsApi.md#api_v2_plans_plan_id_subscriptions_post) | **POST** /api/v2/plans/{plan_id}/subscriptions | Create subscription
[**api_v2_subscriptions_id_delete**](SubscriptionsApi.md#api_v2_subscriptions_id_delete) | **DELETE** /api/v2/subscriptions/{id} | Delete subscription
[**api_v2_subscriptions_id_get**](SubscriptionsApi.md#api_v2_subscriptions_id_get) | **GET** /api/v2/subscriptions/{id} | Show subscription
[**api_v2_subscriptions_id_patch**](SubscriptionsApi.md#api_v2_subscriptions_id_patch) | **PATCH** /api/v2/subscriptions/{id} | Update subscription

# **api_v2_plans_plan_id_subscriptions_get**
> list[InlineResponse20026] api_v2_plans_plan_id_subscriptions_get(plan_id, items=items, page=page)

List subscriptions

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SubscriptionsApi(ans_app_api.ApiClient(configuration))
plan_id = 'plan_id_example' # str | plan_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List subscriptions
    api_response = api_instance.api_v2_plans_plan_id_subscriptions_get(plan_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->api_v2_plans_plan_id_subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| plan_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20026]**](InlineResponse20026.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_plans_plan_id_subscriptions_post**
> InlineResponse20026 api_v2_plans_plan_id_subscriptions_post(plan_id, body=body, brin6=brin6)

Create subscription

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SubscriptionsApi(ans_app_api.ApiClient(configuration))
plan_id = 'plan_id_example' # str | plan_id
body = ans_app_api.PlanIdSubscriptionsBody() # PlanIdSubscriptionsBody |  (optional)
brin6 = 'brin6_example' # str | The brin6 of the school (optional)

try:
    # Create subscription
    api_response = api_instance.api_v2_plans_plan_id_subscriptions_post(plan_id, body=body, brin6=brin6)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->api_v2_plans_plan_id_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| plan_id | 
 **body** | [**PlanIdSubscriptionsBody**](PlanIdSubscriptionsBody.md)|  | [optional] 
 **brin6** | **str**| The brin6 of the school | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_subscriptions_id_delete**
> InlineResponse20026 api_v2_subscriptions_id_delete(id)

Delete subscription

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SubscriptionsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete subscription
    api_response = api_instance.api_v2_subscriptions_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->api_v2_subscriptions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_subscriptions_id_get**
> InlineResponse20026 api_v2_subscriptions_id_get(id)

Show subscription

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SubscriptionsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show subscription
    api_response = api_instance.api_v2_subscriptions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->api_v2_subscriptions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_subscriptions_id_patch**
> InlineResponse20026 api_v2_subscriptions_id_patch(id, body=body)

Update subscription

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.SubscriptionsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.SubscriptionsIdBody() # SubscriptionsIdBody |  (optional)

try:
    # Update subscription
    api_response = api_instance.api_v2_subscriptions_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->api_v2_subscriptions_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**SubscriptionsIdBody**](SubscriptionsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


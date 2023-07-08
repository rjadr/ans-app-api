# ans_app_api.PlansApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_plans_id_delete**](PlansApi.md#api_v2_plans_id_delete) | **DELETE** /api/v2/plans/{id} | Delete plan
[**api_v2_plans_id_get**](PlansApi.md#api_v2_plans_id_get) | **GET** /api/v2/plans/{id} | Show plan
[**api_v2_plans_id_patch**](PlansApi.md#api_v2_plans_id_patch) | **PATCH** /api/v2/plans/{id} | Update plan
[**api_v2_publishers_publisher_id_plans_get**](PlansApi.md#api_v2_publishers_publisher_id_plans_get) | **GET** /api/v2/publishers/{publisher_id}/plans | List plans
[**api_v2_publishers_publisher_id_plans_post**](PlansApi.md#api_v2_publishers_publisher_id_plans_post) | **POST** /api/v2/publishers/{publisher_id}/plans | Create plan

# **api_v2_plans_id_delete**
> InlineResponse20014 api_v2_plans_id_delete(id)

Delete plan

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PlansApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete plan
    api_response = api_instance.api_v2_plans_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->api_v2_plans_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_plans_id_get**
> InlineResponse20014 api_v2_plans_id_get(id)

Show plan

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PlansApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show plan
    api_response = api_instance.api_v2_plans_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->api_v2_plans_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_plans_id_patch**
> InlineResponse20014 api_v2_plans_id_patch(id, body=body)

Update plan

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PlansApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.PlansIdBody() # PlansIdBody |  (optional)

try:
    # Update plan
    api_response = api_instance.api_v2_plans_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->api_v2_plans_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**PlansIdBody**](PlansIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_publishers_publisher_id_plans_get**
> list[InlineResponse20014] api_v2_publishers_publisher_id_plans_get(publisher_id, items=items, page=page)

List plans

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PlansApi(ans_app_api.ApiClient(configuration))
publisher_id = 'publisher_id_example' # str | publisher_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List plans
    api_response = api_instance.api_v2_publishers_publisher_id_plans_get(publisher_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->api_v2_publishers_publisher_id_plans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publisher_id** | **str**| publisher_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20014]**](InlineResponse20014.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_publishers_publisher_id_plans_post**
> InlineResponse20014 api_v2_publishers_publisher_id_plans_post(publisher_id, body=body)

Create plan

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PlansApi(ans_app_api.ApiClient(configuration))
publisher_id = 'publisher_id_example' # str | publisher_id
body = ans_app_api.PublisherIdPlansBody() # PublisherIdPlansBody |  (optional)

try:
    # Create plan
    api_response = api_instance.api_v2_publishers_publisher_id_plans_post(publisher_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->api_v2_publishers_publisher_id_plans_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publisher_id** | **str**| publisher_id | 
 **body** | [**PublisherIdPlansBody**](PublisherIdPlansBody.md)|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


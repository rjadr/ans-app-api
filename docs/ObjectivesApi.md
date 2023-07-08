# ans_app_api.ObjectivesApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_domains_domain_id_objectives_get**](ObjectivesApi.md#api_v2_domains_domain_id_objectives_get) | **GET** /api/v2/domains/{domain_id}/objectives | List objectives
[**api_v2_domains_domain_id_objectives_post**](ObjectivesApi.md#api_v2_domains_domain_id_objectives_post) | **POST** /api/v2/domains/{domain_id}/objectives | Create objective
[**api_v2_objectives_id_delete**](ObjectivesApi.md#api_v2_objectives_id_delete) | **DELETE** /api/v2/objectives/{id} | Delete objective
[**api_v2_objectives_id_get**](ObjectivesApi.md#api_v2_objectives_id_get) | **GET** /api/v2/objectives/{id} | Show objective
[**api_v2_objectives_id_patch**](ObjectivesApi.md#api_v2_objectives_id_patch) | **PATCH** /api/v2/objectives/{id} | Update objective

# **api_v2_domains_domain_id_objectives_get**
> api_v2_domains_domain_id_objectives_get(domain_id, items=items, page=page)

List objectives

List all objectives in a domain

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ObjectivesApi(ans_app_api.ApiClient(configuration))
domain_id = 'domain_id_example' # str | domain_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List objectives
    api_instance.api_v2_domains_domain_id_objectives_get(domain_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling ObjectivesApi->api_v2_domains_domain_id_objectives_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| domain_id | 
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

# **api_v2_domains_domain_id_objectives_post**
> api_v2_domains_domain_id_objectives_post(domain_id, body=body)

Create objective

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ObjectivesApi(ans_app_api.ApiClient(configuration))
domain_id = 'domain_id_example' # str | domain_id
body = ans_app_api.DomainIdObjectivesBody() # DomainIdObjectivesBody |  (optional)

try:
    # Create objective
    api_instance.api_v2_domains_domain_id_objectives_post(domain_id, body=body)
except ApiException as e:
    print("Exception when calling ObjectivesApi->api_v2_domains_domain_id_objectives_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| domain_id | 
 **body** | [**DomainIdObjectivesBody**](DomainIdObjectivesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_objectives_id_delete**
> api_v2_objectives_id_delete(id)

Delete objective

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ObjectivesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete objective
    api_instance.api_v2_objectives_id_delete(id)
except ApiException as e:
    print("Exception when calling ObjectivesApi->api_v2_objectives_id_delete: %s\n" % e)
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

# **api_v2_objectives_id_get**
> api_v2_objectives_id_get(id)

Show objective

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ObjectivesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show objective
    api_instance.api_v2_objectives_id_get(id)
except ApiException as e:
    print("Exception when calling ObjectivesApi->api_v2_objectives_id_get: %s\n" % e)
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

# **api_v2_objectives_id_patch**
> api_v2_objectives_id_patch(id, body=body)

Update objective

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ObjectivesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.ObjectivesIdBody() # ObjectivesIdBody |  (optional)

try:
    # Update objective
    api_instance.api_v2_objectives_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling ObjectivesApi->api_v2_objectives_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**ObjectivesIdBody**](ObjectivesIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


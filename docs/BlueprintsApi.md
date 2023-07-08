# ans_app_api.BlueprintsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_blueprints_id_get**](BlueprintsApi.md#api_v2_blueprints_id_get) | **GET** /api/v2/blueprints/{id} | Show blueprint
[**api_v2_question_banks_question_bank_id_blueprints_get**](BlueprintsApi.md#api_v2_question_banks_question_bank_id_blueprints_get) | **GET** /api/v2/question_banks/{question_bank_id}/blueprints | List blueprints

# **api_v2_blueprints_id_get**
> api_v2_blueprints_id_get(id)

Show blueprint

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.BlueprintsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show blueprint
    api_instance.api_v2_blueprints_id_get(id)
except ApiException as e:
    print("Exception when calling BlueprintsApi->api_v2_blueprints_id_get: %s\n" % e)
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

# **api_v2_question_banks_question_bank_id_blueprints_get**
> api_v2_question_banks_question_bank_id_blueprints_get(question_bank_id, items=items, page=page)

List blueprints

List all your blueprints

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.BlueprintsApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List blueprints
    api_instance.api_v2_question_banks_question_bank_id_blueprints_get(question_bank_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling BlueprintsApi->api_v2_question_banks_question_bank_id_blueprints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_id** | **str**| question_bank_id | 
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


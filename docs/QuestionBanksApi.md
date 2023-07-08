# ans_app_api.QuestionBanksApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_question_banks_get**](QuestionBanksApi.md#api_v2_question_banks_get) | **GET** /api/v2/question_banks | List question banks
[**api_v2_question_banks_id_delete**](QuestionBanksApi.md#api_v2_question_banks_id_delete) | **DELETE** /api/v2/question_banks/{id} | Delete question bank
[**api_v2_question_banks_id_get**](QuestionBanksApi.md#api_v2_question_banks_id_get) | **GET** /api/v2/question_banks/{id} | Show question bank
[**api_v2_question_banks_id_patch**](QuestionBanksApi.md#api_v2_question_banks_id_patch) | **PATCH** /api/v2/question_banks/{id} | Update question bank
[**api_v2_question_banks_post**](QuestionBanksApi.md#api_v2_question_banks_post) | **POST** /api/v2/question_banks | Create question bank

# **api_v2_question_banks_get**
> list[InlineResponse20020] api_v2_question_banks_get(items=items, page=page)

List question banks

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBanksApi(ans_app_api.ApiClient(configuration))
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List question banks
    api_response = api_instance.api_v2_question_banks_get(items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionBanksApi->api_v2_question_banks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20020]**](InlineResponse20020.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_banks_id_delete**
> api_v2_question_banks_id_delete(id)

Delete question bank

Soft delete a question bank by moving it to removed question banks

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBanksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete question bank
    api_instance.api_v2_question_banks_id_delete(id)
except ApiException as e:
    print("Exception when calling QuestionBanksApi->api_v2_question_banks_id_delete: %s\n" % e)
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

# **api_v2_question_banks_id_get**
> api_v2_question_banks_id_get(id)

Show question bank

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBanksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show question bank
    api_instance.api_v2_question_banks_id_get(id)
except ApiException as e:
    print("Exception when calling QuestionBanksApi->api_v2_question_banks_id_get: %s\n" % e)
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

# **api_v2_question_banks_id_patch**
> api_v2_question_banks_id_patch(id, body=body)

Update question bank

To update from one role to another,         the user must first be removed from the current role list and with a new request added to the chosen role list

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBanksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.QuestionBanksIdBody() # QuestionBanksIdBody |  (optional)

try:
    # Update question bank
    api_instance.api_v2_question_banks_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling QuestionBanksApi->api_v2_question_banks_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**QuestionBanksIdBody**](QuestionBanksIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_banks_post**
> api_v2_question_banks_post(body=body)

Create question bank

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBanksApi(ans_app_api.ApiClient(configuration))
body = ans_app_api.V2QuestionBanksBody() # V2QuestionBanksBody |  (optional)

try:
    # Create question bank
    api_instance.api_v2_question_banks_post(body=body)
except ApiException as e:
    print("Exception when calling QuestionBanksApi->api_v2_question_banks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2QuestionBanksBody**](V2QuestionBanksBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


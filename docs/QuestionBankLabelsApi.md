# ans_app_api.QuestionBankLabelsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_question_bank_labels_id_delete**](QuestionBankLabelsApi.md#api_v2_question_bank_labels_id_delete) | **DELETE** /api/v2/question_bank_labels/{id} | Delete question bank label
[**api_v2_question_bank_labels_id_get**](QuestionBankLabelsApi.md#api_v2_question_bank_labels_id_get) | **GET** /api/v2/question_bank_labels/{id} | Show question bank label
[**api_v2_question_bank_labels_id_patch**](QuestionBankLabelsApi.md#api_v2_question_bank_labels_id_patch) | **PATCH** /api/v2/question_bank_labels/{id} | Update question bank label
[**api_v2_question_banks_question_bank_id_question_bank_labels_get**](QuestionBankLabelsApi.md#api_v2_question_banks_question_bank_id_question_bank_labels_get) | **GET** /api/v2/question_banks/{question_bank_id}/question_bank_labels | List question bank labels
[**api_v2_question_banks_question_bank_id_question_bank_labels_post**](QuestionBankLabelsApi.md#api_v2_question_banks_question_bank_id_question_bank_labels_post) | **POST** /api/v2/question_banks/{question_bank_id}/question_bank_labels | Create question bank label

# **api_v2_question_bank_labels_id_delete**
> api_v2_question_bank_labels_id_delete(id)

Delete question bank label

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankLabelsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete question bank label
    api_instance.api_v2_question_bank_labels_id_delete(id)
except ApiException as e:
    print("Exception when calling QuestionBankLabelsApi->api_v2_question_bank_labels_id_delete: %s\n" % e)
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

# **api_v2_question_bank_labels_id_get**
> api_v2_question_bank_labels_id_get(id)

Show question bank label

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankLabelsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show question bank label
    api_instance.api_v2_question_bank_labels_id_get(id)
except ApiException as e:
    print("Exception when calling QuestionBankLabelsApi->api_v2_question_bank_labels_id_get: %s\n" % e)
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

# **api_v2_question_bank_labels_id_patch**
> api_v2_question_bank_labels_id_patch(id, body=body)

Update question bank label

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankLabelsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.QuestionBankLabelsIdBody() # QuestionBankLabelsIdBody |  (optional)

try:
    # Update question bank label
    api_instance.api_v2_question_bank_labels_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling QuestionBankLabelsApi->api_v2_question_bank_labels_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**QuestionBankLabelsIdBody**](QuestionBankLabelsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_banks_question_bank_id_question_bank_labels_get**
> api_v2_question_banks_question_bank_id_question_bank_labels_get(question_bank_id, items=items, page=page)

List question bank labels

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankLabelsApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List question bank labels
    api_instance.api_v2_question_banks_question_bank_id_question_bank_labels_get(question_bank_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling QuestionBankLabelsApi->api_v2_question_banks_question_bank_id_question_bank_labels_get: %s\n" % e)
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

# **api_v2_question_banks_question_bank_id_question_bank_labels_post**
> api_v2_question_banks_question_bank_id_question_bank_labels_post(question_bank_id, body=body)

Create question bank label

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankLabelsApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
body = ans_app_api.QuestionBankIdQuestionBankLabelsBody() # QuestionBankIdQuestionBankLabelsBody |  (optional)

try:
    # Create question bank label
    api_instance.api_v2_question_banks_question_bank_id_question_bank_labels_post(question_bank_id, body=body)
except ApiException as e:
    print("Exception when calling QuestionBankLabelsApi->api_v2_question_banks_question_bank_id_question_bank_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_id** | **str**| question_bank_id | 
 **body** | [**QuestionBankIdQuestionBankLabelsBody**](QuestionBankIdQuestionBankLabelsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


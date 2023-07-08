# ans_app_api.QuestionBankAssignmentsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_question_bank_assignments_id_delete**](QuestionBankAssignmentsApi.md#api_v2_question_bank_assignments_id_delete) | **DELETE** /api/v2/question_bank_assignments/{id} | Delete question bank assignment
[**api_v2_question_bank_assignments_id_get**](QuestionBankAssignmentsApi.md#api_v2_question_bank_assignments_id_get) | **GET** /api/v2/question_bank_assignments/{id} | Show question bank assignment
[**api_v2_question_bank_assignments_id_patch**](QuestionBankAssignmentsApi.md#api_v2_question_bank_assignments_id_patch) | **PATCH** /api/v2/question_bank_assignments/{id} | Update question bank assignment
[**api_v2_question_bank_assignments_question_bank_assignment_id_question_bank_assignment_results_get**](QuestionBankAssignmentsApi.md#api_v2_question_bank_assignments_question_bank_assignment_id_question_bank_assignment_results_get) | **GET** /api/v2/question_bank_assignments/{question_bank_assignment_id}/question_bank_assignment_results | List question bank assignment results
[**api_v2_question_banks_question_bank_id_question_bank_assignments_get**](QuestionBankAssignmentsApi.md#api_v2_question_banks_question_bank_id_question_bank_assignments_get) | **GET** /api/v2/question_banks/{question_bank_id}/question_bank_assignments | List question bank assignments
[**api_v2_question_banks_question_bank_id_question_bank_assignments_post**](QuestionBankAssignmentsApi.md#api_v2_question_banks_question_bank_id_question_bank_assignments_post) | **POST** /api/v2/question_banks/{question_bank_id}/question_bank_assignments | Create question bank assignment

# **api_v2_question_bank_assignments_id_delete**
> api_v2_question_bank_assignments_id_delete(id)

Delete question bank assignment

Soft delete a question bank assignment by moving it to removed assignments

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankAssignmentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete question bank assignment
    api_instance.api_v2_question_bank_assignments_id_delete(id)
except ApiException as e:
    print("Exception when calling QuestionBankAssignmentsApi->api_v2_question_bank_assignments_id_delete: %s\n" % e)
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

# **api_v2_question_bank_assignments_id_get**
> api_v2_question_bank_assignments_id_get(id)

Show question bank assignment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankAssignmentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show question bank assignment
    api_instance.api_v2_question_bank_assignments_id_get(id)
except ApiException as e:
    print("Exception when calling QuestionBankAssignmentsApi->api_v2_question_bank_assignments_id_get: %s\n" % e)
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

# **api_v2_question_bank_assignments_id_patch**
> api_v2_question_bank_assignments_id_patch(id, body=body)

Update question bank assignment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankAssignmentsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.QuestionBankAssignmentsIdBody() # QuestionBankAssignmentsIdBody |  (optional)

try:
    # Update question bank assignment
    api_instance.api_v2_question_bank_assignments_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling QuestionBankAssignmentsApi->api_v2_question_bank_assignments_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**QuestionBankAssignmentsIdBody**](QuestionBankAssignmentsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_bank_assignments_question_bank_assignment_id_question_bank_assignment_results_get**
> api_v2_question_bank_assignments_question_bank_assignment_id_question_bank_assignment_results_get(question_bank_assignment_id, items=items, page=page)

List question bank assignment results

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankAssignmentsApi(ans_app_api.ApiClient(configuration))
question_bank_assignment_id = 'question_bank_assignment_id_example' # str | question_bank_assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List question bank assignment results
    api_instance.api_v2_question_bank_assignments_question_bank_assignment_id_question_bank_assignment_results_get(question_bank_assignment_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling QuestionBankAssignmentsApi->api_v2_question_bank_assignments_question_bank_assignment_id_question_bank_assignment_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_assignment_id** | **str**| question_bank_assignment_id | 
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

# **api_v2_question_banks_question_bank_id_question_bank_assignments_get**
> list[InlineResponse20017] api_v2_question_banks_question_bank_id_question_bank_assignments_get(question_bank_id, items=items, page=page)

List question bank assignments

List all assignments in a question bank

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankAssignmentsApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List question bank assignments
    api_response = api_instance.api_v2_question_banks_question_bank_id_question_bank_assignments_get(question_bank_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionBankAssignmentsApi->api_v2_question_banks_question_bank_id_question_bank_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_id** | **str**| question_bank_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20017]**](InlineResponse20017.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_banks_question_bank_id_question_bank_assignments_post**
> api_v2_question_banks_question_bank_id_question_bank_assignments_post(question_bank_id, body=body)

Create question bank assignment

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankAssignmentsApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
body = ans_app_api.QuestionBankIdQuestionBankAssignmentsBody() # QuestionBankIdQuestionBankAssignmentsBody |  (optional)

try:
    # Create question bank assignment
    api_instance.api_v2_question_banks_question_bank_id_question_bank_assignments_post(question_bank_id, body=body)
except ApiException as e:
    print("Exception when calling QuestionBankAssignmentsApi->api_v2_question_banks_question_bank_id_question_bank_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_id** | **str**| question_bank_id | 
 **body** | [**QuestionBankIdQuestionBankAssignmentsBody**](QuestionBankIdQuestionBankAssignmentsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


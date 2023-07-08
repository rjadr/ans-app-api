# ans_app_api.TasksApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_tasks_get**](TasksApi.md#api_v2_assignments_assignment_id_tasks_get) | **GET** /api/v2/assignments/{assignment_id}/tasks | List assignment tasks
[**api_v2_assignments_assignment_id_tasks_post**](TasksApi.md#api_v2_assignments_assignment_id_tasks_post) | **POST** /api/v2/assignments/{assignment_id}/tasks | Create assignment task
[**api_v2_question_banks_question_bank_id_tasks_get**](TasksApi.md#api_v2_question_banks_question_bank_id_tasks_get) | **GET** /api/v2/question_banks/{question_bank_id}/tasks | List question bank tasks
[**api_v2_question_banks_question_bank_id_tasks_post**](TasksApi.md#api_v2_question_banks_question_bank_id_tasks_post) | **POST** /api/v2/question_banks/{question_bank_id}/tasks | Create question bank task
[**api_v2_tasks_id_delete**](TasksApi.md#api_v2_tasks_id_delete) | **DELETE** /api/v2/tasks/{id} | Delete task
[**api_v2_tasks_id_get**](TasksApi.md#api_v2_tasks_id_get) | **GET** /api/v2/tasks/{id} | Show task
[**api_v2_tasks_id_patch**](TasksApi.md#api_v2_tasks_id_patch) | **PATCH** /api/v2/tasks/{id} | Update task

# **api_v2_assignments_assignment_id_tasks_get**
> api_v2_assignments_assignment_id_tasks_get(assignment_id, items=items, page=page)

List assignment tasks

List all your assignment tasks

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TasksApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List assignment tasks
    api_instance.api_v2_assignments_assignment_id_tasks_get(assignment_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling TasksApi->api_v2_assignments_assignment_id_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
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

# **api_v2_assignments_assignment_id_tasks_post**
> api_v2_assignments_assignment_id_tasks_post(assignment_id, body=body)

Create assignment task

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TasksApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
body = ans_app_api.AssignmentIdTasksBody() # AssignmentIdTasksBody |  (optional)

try:
    # Create assignment task
    api_instance.api_v2_assignments_assignment_id_tasks_post(assignment_id, body=body)
except ApiException as e:
    print("Exception when calling TasksApi->api_v2_assignments_assignment_id_tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **body** | [**AssignmentIdTasksBody**](AssignmentIdTasksBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_banks_question_bank_id_tasks_get**
> api_v2_question_banks_question_bank_id_tasks_get(question_bank_id, items=items, page=page)

List question bank tasks

List all your question bank tasks

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TasksApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List question bank tasks
    api_instance.api_v2_question_banks_question_bank_id_tasks_get(question_bank_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling TasksApi->api_v2_question_banks_question_bank_id_tasks_get: %s\n" % e)
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

# **api_v2_question_banks_question_bank_id_tasks_post**
> api_v2_question_banks_question_bank_id_tasks_post(question_bank_id, body=body)

Create question bank task

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TasksApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
body = ans_app_api.QuestionBankIdTasksBody() # QuestionBankIdTasksBody |  (optional)

try:
    # Create question bank task
    api_instance.api_v2_question_banks_question_bank_id_tasks_post(question_bank_id, body=body)
except ApiException as e:
    print("Exception when calling TasksApi->api_v2_question_banks_question_bank_id_tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_id** | **str**| question_bank_id | 
 **body** | [**QuestionBankIdTasksBody**](QuestionBankIdTasksBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tasks_id_delete**
> api_v2_tasks_id_delete(id)

Delete task

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TasksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete task
    api_instance.api_v2_tasks_id_delete(id)
except ApiException as e:
    print("Exception when calling TasksApi->api_v2_tasks_id_delete: %s\n" % e)
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

# **api_v2_tasks_id_get**
> api_v2_tasks_id_get(id)

Show task

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TasksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show task
    api_instance.api_v2_tasks_id_get(id)
except ApiException as e:
    print("Exception when calling TasksApi->api_v2_tasks_id_get: %s\n" % e)
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

# **api_v2_tasks_id_patch**
> api_v2_tasks_id_patch(id, body=body)

Update task

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.TasksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.TasksIdBody() # TasksIdBody |  (optional)

try:
    # Update task
    api_instance.api_v2_tasks_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling TasksApi->api_v2_tasks_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**TasksIdBody**](TasksIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


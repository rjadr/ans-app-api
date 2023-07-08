# ans_app_api.QuestionBankExercisesApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_question_bank_exercises_id_delete**](QuestionBankExercisesApi.md#api_v2_question_bank_exercises_id_delete) | **DELETE** /api/v2/question_bank_exercises/{id} | Delete question bank exercise
[**api_v2_question_bank_exercises_id_get**](QuestionBankExercisesApi.md#api_v2_question_bank_exercises_id_get) | **GET** /api/v2/question_bank_exercises/{id} | Show question bank exercise
[**api_v2_question_bank_exercises_id_patch**](QuestionBankExercisesApi.md#api_v2_question_bank_exercises_id_patch) | **PATCH** /api/v2/question_bank_exercises/{id} | Update question bank exercise
[**api_v2_question_banks_question_bank_id_question_bank_exercises_get**](QuestionBankExercisesApi.md#api_v2_question_banks_question_bank_id_question_bank_exercises_get) | **GET** /api/v2/question_banks/{question_bank_id}/question_bank_exercises | List question bank exercises
[**api_v2_question_banks_question_bank_id_question_bank_exercises_import_get**](QuestionBankExercisesApi.md#api_v2_question_banks_question_bank_id_question_bank_exercises_import_get) | **GET** /api/v2/question_banks/{question_bank_id}/question_bank_exercises/import | Import question bank exercises
[**api_v2_question_banks_question_bank_id_question_bank_exercises_post**](QuestionBankExercisesApi.md#api_v2_question_banks_question_bank_id_question_bank_exercises_post) | **POST** /api/v2/question_banks/{question_bank_id}/question_bank_exercises | Create question bank exercise

# **api_v2_question_bank_exercises_id_delete**
> api_v2_question_bank_exercises_id_delete(id)

Delete question bank exercise

Soft delete a question bank exercise by moving it to removed exercises

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankExercisesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete question bank exercise
    api_instance.api_v2_question_bank_exercises_id_delete(id)
except ApiException as e:
    print("Exception when calling QuestionBankExercisesApi->api_v2_question_bank_exercises_id_delete: %s\n" % e)
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

# **api_v2_question_bank_exercises_id_get**
> InlineResponse20019 api_v2_question_bank_exercises_id_get(id)

Show question bank exercise

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankExercisesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show question bank exercise
    api_response = api_instance.api_v2_question_bank_exercises_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionBankExercisesApi->api_v2_question_bank_exercises_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_bank_exercises_id_patch**
> api_v2_question_bank_exercises_id_patch(id, body=body)

Update question bank exercise

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankExercisesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.QuestionBankExercisesIdBody() # QuestionBankExercisesIdBody |  (optional)

try:
    # Update question bank exercise
    api_instance.api_v2_question_bank_exercises_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling QuestionBankExercisesApi->api_v2_question_bank_exercises_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**QuestionBankExercisesIdBody**](QuestionBankExercisesIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_banks_question_bank_id_question_bank_exercises_get**
> list[InlineResponse20018] api_v2_question_banks_question_bank_id_question_bank_exercises_get(question_bank_id, items=items, page=page)

List question bank exercises

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankExercisesApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List question bank exercises
    api_response = api_instance.api_v2_question_banks_question_bank_id_question_bank_exercises_get(question_bank_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionBankExercisesApi->api_v2_question_banks_question_bank_id_question_bank_exercises_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_id** | **str**| question_bank_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20018]**](InlineResponse20018.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_banks_question_bank_id_question_bank_exercises_import_get**
> api_v2_question_banks_question_bank_id_question_bank_exercises_import_get(question_bank_id, file_name=file_name, file_size=file_size)

Import question bank exercises

Import a QTI zip file. You will receive a put_url to upload the QTI zip file to our object store. The put_url is valid for 1 hour. After uploading the file, you must change the status of the background job from \"initialized\" to \"pending\" to start the processing of the QTI file

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankExercisesApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
file_name = 'file_name_example' # str | The name of the QTI file (optional)
file_size = 56 # int | The size of the QTI zip file in bytes (optional)

try:
    # Import question bank exercises
    api_instance.api_v2_question_banks_question_bank_id_question_bank_exercises_import_get(question_bank_id, file_name=file_name, file_size=file_size)
except ApiException as e:
    print("Exception when calling QuestionBankExercisesApi->api_v2_question_banks_question_bank_id_question_bank_exercises_import_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_id** | **str**| question_bank_id | 
 **file_name** | **str**| The name of the QTI file | [optional] 
 **file_size** | **int**| The size of the QTI zip file in bytes | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_banks_question_bank_id_question_bank_exercises_post**
> api_v2_question_banks_question_bank_id_question_bank_exercises_post(question_bank_id, body=body)

Create question bank exercise

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionBankExercisesApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
body = ans_app_api.QuestionBankIdQuestionBankExercisesBody() # QuestionBankIdQuestionBankExercisesBody |  (optional)

try:
    # Create question bank exercise
    api_instance.api_v2_question_banks_question_bank_id_question_bank_exercises_post(question_bank_id, body=body)
except ApiException as e:
    print("Exception when calling QuestionBankExercisesApi->api_v2_question_banks_question_bank_id_question_bank_exercises_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_id** | **str**| question_bank_id | 
 **body** | [**QuestionBankIdQuestionBankExercisesBody**](QuestionBankIdQuestionBankExercisesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ans_app_api.QuestionsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_exercises_exercise_id_questions_get**](QuestionsApi.md#api_v2_exercises_exercise_id_questions_get) | **GET** /api/v2/exercises/{exercise_id}/questions | List questions
[**api_v2_exercises_exercise_id_questions_post**](QuestionsApi.md#api_v2_exercises_exercise_id_questions_post) | **POST** /api/v2/exercises/{exercise_id}/questions | Create question
[**api_v2_questions_id_delete**](QuestionsApi.md#api_v2_questions_id_delete) | **DELETE** /api/v2/questions/{id} | Delete question
[**api_v2_questions_id_get**](QuestionsApi.md#api_v2_questions_id_get) | **GET** /api/v2/questions/{id} | Show question
[**api_v2_questions_id_patch**](QuestionsApi.md#api_v2_questions_id_patch) | **PATCH** /api/v2/questions/{id} | Update question

# **api_v2_exercises_exercise_id_questions_get**
> list[InlineResponse20021] api_v2_exercises_exercise_id_questions_get(exercise_id, items=items, page=page)

List questions

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionsApi(ans_app_api.ApiClient(configuration))
exercise_id = 'exercise_id_example' # str | exercise_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List questions
    api_response = api_instance.api_v2_exercises_exercise_id_questions_get(exercise_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->api_v2_exercises_exercise_id_questions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exercise_id** | **str**| exercise_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20021]**](InlineResponse20021.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_exercises_exercise_id_questions_post**
> InlineResponse2016 api_v2_exercises_exercise_id_questions_post(exercise_id, body=body)

Create question

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionsApi(ans_app_api.ApiClient(configuration))
exercise_id = 'exercise_id_example' # str | exercise_id
body = ans_app_api.ExerciseIdQuestionsBody() # ExerciseIdQuestionsBody |  (optional)

try:
    # Create question
    api_response = api_instance.api_v2_exercises_exercise_id_questions_post(exercise_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->api_v2_exercises_exercise_id_questions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exercise_id** | **str**| exercise_id | 
 **body** | [**ExerciseIdQuestionsBody**](ExerciseIdQuestionsBody.md)|  | [optional] 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_questions_id_delete**
> InlineResponse2016 api_v2_questions_id_delete(id)

Delete question

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete question
    api_response = api_instance.api_v2_questions_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->api_v2_questions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_questions_id_get**
> InlineResponse2016 api_v2_questions_id_get(id)

Show question

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show question
    api_response = api_instance.api_v2_questions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->api_v2_questions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_questions_id_patch**
> InlineResponse2016 api_v2_questions_id_patch(id, body=body)

Update question

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.QuestionsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.QuestionsIdBody() # QuestionsIdBody |  (optional)

try:
    # Update question
    api_response = api_instance.api_v2_questions_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->api_v2_questions_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**QuestionsIdBody**](QuestionsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


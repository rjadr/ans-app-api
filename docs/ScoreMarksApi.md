# ans_app_api.ScoreMarksApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_score_marks_get**](ScoreMarksApi.md#api_v2_assignments_assignment_id_score_marks_get) | **GET** /api/v2/assignments/{assignment_id}/score_marks | List score marks
[**api_v2_assignments_assignment_id_score_marks_post**](ScoreMarksApi.md#api_v2_assignments_assignment_id_score_marks_post) | **POST** /api/v2/assignments/{assignment_id}/score_marks | Create score mark
[**api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get**](ScoreMarksApi.md#api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get) | **GET** /api/v2/question_bank_assignments/{question_bank_assignment_id}/score_marks | List question bank assignment score marks
[**api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post**](ScoreMarksApi.md#api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post) | **POST** /api/v2/question_bank_assignments/{question_bank_assignment_id}/score_marks | Create question bank assignment score mark
[**api_v2_score_marks_id_delete**](ScoreMarksApi.md#api_v2_score_marks_id_delete) | **DELETE** /api/v2/score_marks/{id} | Delete score mark
[**api_v2_score_marks_id_get**](ScoreMarksApi.md#api_v2_score_marks_id_get) | **GET** /api/v2/score_marks/{id} | Show score mark
[**api_v2_score_marks_id_patch**](ScoreMarksApi.md#api_v2_score_marks_id_patch) | **PATCH** /api/v2/score_marks/{id} | Update score mark

# **api_v2_assignments_assignment_id_score_marks_get**
> list[InlineResponse20024] api_v2_assignments_assignment_id_score_marks_get(assignment_id, items=items, page=page)

List score marks

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ScoreMarksApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List score marks
    api_response = api_instance.api_v2_assignments_assignment_id_score_marks_get(assignment_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreMarksApi->api_v2_assignments_assignment_id_score_marks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20024]**](InlineResponse20024.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_assignment_id_score_marks_post**
> InlineResponse20024 api_v2_assignments_assignment_id_score_marks_post(assignment_id, body=body)

Create score mark

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ScoreMarksApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
body = ans_app_api.AssignmentIdScoreMarksBody() # AssignmentIdScoreMarksBody |  (optional)

try:
    # Create score mark
    api_response = api_instance.api_v2_assignments_assignment_id_score_marks_post(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreMarksApi->api_v2_assignments_assignment_id_score_marks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **body** | [**AssignmentIdScoreMarksBody**](AssignmentIdScoreMarksBody.md)|  | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get**
> list[InlineResponse20024] api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get(question_bank_assignment_id, items=items, page=page)

List question bank assignment score marks

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ScoreMarksApi(ans_app_api.ApiClient(configuration))
question_bank_assignment_id = 'question_bank_assignment_id_example' # str | question_bank_assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List question bank assignment score marks
    api_response = api_instance.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get(question_bank_assignment_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreMarksApi->api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_assignment_id** | **str**| question_bank_assignment_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20024]**](InlineResponse20024.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post**
> InlineResponse20024 api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post(question_bank_assignment_id, body=body)

Create question bank assignment score mark

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ScoreMarksApi(ans_app_api.ApiClient(configuration))
question_bank_assignment_id = 'question_bank_assignment_id_example' # str | question_bank_assignment_id
body = ans_app_api.QuestionBankAssignmentIdScoreMarksBody() # QuestionBankAssignmentIdScoreMarksBody |  (optional)

try:
    # Create question bank assignment score mark
    api_response = api_instance.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post(question_bank_assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreMarksApi->api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_assignment_id** | **str**| question_bank_assignment_id | 
 **body** | [**QuestionBankAssignmentIdScoreMarksBody**](QuestionBankAssignmentIdScoreMarksBody.md)|  | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_score_marks_id_delete**
> api_v2_score_marks_id_delete(id)

Delete score mark

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ScoreMarksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete score mark
    api_instance.api_v2_score_marks_id_delete(id)
except ApiException as e:
    print("Exception when calling ScoreMarksApi->api_v2_score_marks_id_delete: %s\n" % e)
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

# **api_v2_score_marks_id_get**
> InlineResponse20024 api_v2_score_marks_id_get(id)

Show score mark

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ScoreMarksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show score mark
    api_response = api_instance.api_v2_score_marks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreMarksApi->api_v2_score_marks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_score_marks_id_patch**
> InlineResponse20024 api_v2_score_marks_id_patch(id, body=body)

Update score mark

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ScoreMarksApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.ScoreMarksIdBody() # ScoreMarksIdBody |  (optional)

try:
    # Update score mark
    api_response = api_instance.api_v2_score_marks_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreMarksApi->api_v2_score_marks_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**ScoreMarksIdBody**](ScoreMarksIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


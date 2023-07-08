# ans_app_api.CoversApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_cover_get**](CoversApi.md#api_v2_assignments_assignment_id_cover_get) | **GET** /api/v2/assignments/{assignment_id}/cover | Show cover
[**api_v2_assignments_assignment_id_cover_patch**](CoversApi.md#api_v2_assignments_assignment_id_cover_patch) | **PATCH** /api/v2/assignments/{assignment_id}/cover | Update cover
[**api_v2_question_bank_assignments_question_bank_assignment_id_cover_get**](CoversApi.md#api_v2_question_bank_assignments_question_bank_assignment_id_cover_get) | **GET** /api/v2/question_bank_assignments/{question_bank_assignment_id}/cover | Show cover
[**api_v2_question_bank_assignments_question_bank_assignment_id_cover_patch**](CoversApi.md#api_v2_question_bank_assignments_question_bank_assignment_id_cover_patch) | **PATCH** /api/v2/question_bank_assignments/{question_bank_assignment_id}/cover | Update cover

# **api_v2_assignments_assignment_id_cover_get**
> InlineResponse2004 api_v2_assignments_assignment_id_cover_get(assignment_id)

Show cover

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoversApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id

try:
    # Show cover
    api_response = api_instance.api_v2_assignments_assignment_id_cover_get(assignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoversApi->api_v2_assignments_assignment_id_cover_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_assignment_id_cover_patch**
> InlineResponse2004 api_v2_assignments_assignment_id_cover_patch(assignment_id, body=body)

Update cover

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoversApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
body = ans_app_api.AssignmentIdCoverBody() # AssignmentIdCoverBody |  (optional)

try:
    # Update cover
    api_response = api_instance.api_v2_assignments_assignment_id_cover_patch(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoversApi->api_v2_assignments_assignment_id_cover_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **body** | [**AssignmentIdCoverBody**](AssignmentIdCoverBody.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_bank_assignments_question_bank_assignment_id_cover_get**
> InlineResponse2004 api_v2_question_bank_assignments_question_bank_assignment_id_cover_get(question_bank_assignment_id)

Show cover

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoversApi(ans_app_api.ApiClient(configuration))
question_bank_assignment_id = 'question_bank_assignment_id_example' # str | question_bank_assignment_id

try:
    # Show cover
    api_response = api_instance.api_v2_question_bank_assignments_question_bank_assignment_id_cover_get(question_bank_assignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoversApi->api_v2_question_bank_assignments_question_bank_assignment_id_cover_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_assignment_id** | **str**| question_bank_assignment_id | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_bank_assignments_question_bank_assignment_id_cover_patch**
> api_v2_question_bank_assignments_question_bank_assignment_id_cover_patch(question_bank_assignment_id, body=body)

Update cover

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.CoversApi(ans_app_api.ApiClient(configuration))
question_bank_assignment_id = 'question_bank_assignment_id_example' # str | question_bank_assignment_id
body = ans_app_api.QuestionBankAssignmentIdCoverBody() # QuestionBankAssignmentIdCoverBody |  (optional)

try:
    # Update cover
    api_instance.api_v2_question_bank_assignments_question_bank_assignment_id_cover_patch(question_bank_assignment_id, body=body)
except ApiException as e:
    print("Exception when calling CoversApi->api_v2_question_bank_assignments_question_bank_assignment_id_cover_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_assignment_id** | **str**| question_bank_assignment_id | 
 **body** | [**QuestionBankAssignmentIdCoverBody**](QuestionBankAssignmentIdCoverBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


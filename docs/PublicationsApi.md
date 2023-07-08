# ans_app_api.PublicationsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_publication_get**](PublicationsApi.md#api_v2_assignments_assignment_id_publication_get) | **GET** /api/v2/assignments/{assignment_id}/publication | Show publication
[**api_v2_assignments_assignment_id_publication_patch**](PublicationsApi.md#api_v2_assignments_assignment_id_publication_patch) | **PATCH** /api/v2/assignments/{assignment_id}/publication | Update publication

# **api_v2_assignments_assignment_id_publication_get**
> InlineResponse20016 api_v2_assignments_assignment_id_publication_get(assignment_id)

Show publication

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PublicationsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id

try:
    # Show publication
    api_response = api_instance.api_v2_assignments_assignment_id_publication_get(assignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationsApi->api_v2_assignments_assignment_id_publication_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_assignment_id_publication_patch**
> api_v2_assignments_assignment_id_publication_patch(assignment_id, body=body)

Update publication

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PublicationsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
body = ans_app_api.AssignmentIdPublicationBody() # AssignmentIdPublicationBody |  (optional)

try:
    # Update publication
    api_instance.api_v2_assignments_assignment_id_publication_patch(assignment_id, body=body)
except ApiException as e:
    print("Exception when calling PublicationsApi->api_v2_assignments_assignment_id_publication_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **body** | [**AssignmentIdPublicationBody**](AssignmentIdPublicationBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


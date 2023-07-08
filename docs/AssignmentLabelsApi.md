# ans_app_api.AssignmentLabelsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_labels_id_delete**](AssignmentLabelsApi.md#api_v2_labels_id_delete) | **DELETE** /api/v2/labels/{id} | Delete assignment label
[**api_v2_labels_id_get**](AssignmentLabelsApi.md#api_v2_labels_id_get) | **GET** /api/v2/labels/{id} | Show assignment label
[**api_v2_labels_id_patch**](AssignmentLabelsApi.md#api_v2_labels_id_patch) | **PATCH** /api/v2/labels/{id} | Update assignment label
[**api_v2_schools_school_id_labels_get**](AssignmentLabelsApi.md#api_v2_schools_school_id_labels_get) | **GET** /api/v2/schools/{school_id}/labels | List assignment labels
[**api_v2_schools_school_id_labels_post**](AssignmentLabelsApi.md#api_v2_schools_school_id_labels_post) | **POST** /api/v2/schools/{school_id}/labels | Create assignment label

# **api_v2_labels_id_delete**
> api_v2_labels_id_delete(id)

Delete assignment label

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentLabelsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete assignment label
    api_instance.api_v2_labels_id_delete(id)
except ApiException as e:
    print("Exception when calling AssignmentLabelsApi->api_v2_labels_id_delete: %s\n" % e)
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

# **api_v2_labels_id_get**
> api_v2_labels_id_get(id)

Show assignment label

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentLabelsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show assignment label
    api_instance.api_v2_labels_id_get(id)
except ApiException as e:
    print("Exception when calling AssignmentLabelsApi->api_v2_labels_id_get: %s\n" % e)
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

# **api_v2_labels_id_patch**
> api_v2_labels_id_patch(id, body=body)

Update assignment label

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentLabelsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.LabelsIdBody() # LabelsIdBody |  (optional)

try:
    # Update assignment label
    api_instance.api_v2_labels_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling AssignmentLabelsApi->api_v2_labels_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**LabelsIdBody**](LabelsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_schools_school_id_labels_get**
> api_v2_schools_school_id_labels_get(school_id, items=items, page=page)

List assignment labels

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentLabelsApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List assignment labels
    api_instance.api_v2_schools_school_id_labels_get(school_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling AssignmentLabelsApi->api_v2_schools_school_id_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
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

# **api_v2_schools_school_id_labels_post**
> api_v2_schools_school_id_labels_post(school_id, body=body)

Create assignment label

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.AssignmentLabelsApi(ans_app_api.ApiClient(configuration))
school_id = 'school_id_example' # str | school_id
body = ans_app_api.SchoolIdLabelsBody() # SchoolIdLabelsBody |  (optional)

try:
    # Create assignment label
    api_instance.api_v2_schools_school_id_labels_post(school_id, body=body)
except ApiException as e:
    print("Exception when calling AssignmentLabelsApi->api_v2_schools_school_id_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| school_id | 
 **body** | [**SchoolIdLabelsBody**](SchoolIdLabelsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


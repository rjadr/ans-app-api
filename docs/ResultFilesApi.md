# ans_app_api.ResultFilesApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_files_id_delete**](ResultFilesApi.md#api_v2_files_id_delete) | **DELETE** /api/v2/files/{id} | Delete file
[**api_v2_results_result_id_files_new_get**](ResultFilesApi.md#api_v2_results_result_id_files_new_get) | **GET** /api/v2/results/{result_id}/files/new | Request url to upload a file
[**api_v2_results_result_id_files_post**](ResultFilesApi.md#api_v2_results_result_id_files_post) | **POST** /api/v2/results/{result_id}/files | Create file

# **api_v2_files_id_delete**
> InlineResponse2014 api_v2_files_id_delete(id)

Delete file

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ResultFilesApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete file
    api_response = api_instance.api_v2_files_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultFilesApi->api_v2_files_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_files_new_get**
> api_v2_results_result_id_files_new_get(result_id, file_name=file_name, file_size=file_size)

Request url to upload a file

Before importing a file you must create a result in the hand-in assignment. Use the result ID and                    a file name of your choosing to request an upload URL and a file key.                    This key can be used to create a file instance using a POST request. After the file has been                    uploaded and the instance created, you must change the result status to `submitted` to submit the                    result

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ResultFilesApi(ans_app_api.ApiClient(configuration))
result_id = 'result_id_example' # str | result_id
file_name = 'file_name_example' # str | The name of the file (optional)
file_size = 56 # int | The size of the file in bytes (optional)

try:
    # Request url to upload a file
    api_instance.api_v2_results_result_id_files_new_get(result_id, file_name=file_name, file_size=file_size)
except ApiException as e:
    print("Exception when calling ResultFilesApi->api_v2_results_result_id_files_new_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| result_id | 
 **file_name** | **str**| The name of the file | [optional] 
 **file_size** | **int**| The size of the file in bytes | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_files_post**
> InlineResponse2014 api_v2_results_result_id_files_post(result_id, body=body)

Create file

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.ResultFilesApi(ans_app_api.ApiClient(configuration))
result_id = 'result_id_example' # str | result_id
body = ans_app_api.ResultIdFilesBody() # ResultIdFilesBody |  (optional)

try:
    # Create file
    api_response = api_instance.api_v2_results_result_id_files_post(result_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultFilesApi->api_v2_results_result_id_files_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| result_id | 
 **body** | [**ResultIdFilesBody**](ResultIdFilesBody.md)|  | [optional] 

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


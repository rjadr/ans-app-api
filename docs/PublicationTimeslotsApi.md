# ans_app_api.PublicationTimeslotsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_assignments_assignment_id_publication_timeslots_get**](PublicationTimeslotsApi.md#api_v2_assignments_assignment_id_publication_timeslots_get) | **GET** /api/v2/assignments/{assignment_id}/publication_timeslots | List publication timeslots
[**api_v2_assignments_assignment_id_publication_timeslots_post**](PublicationTimeslotsApi.md#api_v2_assignments_assignment_id_publication_timeslots_post) | **POST** /api/v2/assignments/{assignment_id}/publication_timeslots | Create publication timeslot
[**api_v2_publication_timeslots_id_delete**](PublicationTimeslotsApi.md#api_v2_publication_timeslots_id_delete) | **DELETE** /api/v2/publication_timeslots/{id} | Delete publication timeslot
[**api_v2_publication_timeslots_id_get**](PublicationTimeslotsApi.md#api_v2_publication_timeslots_id_get) | **GET** /api/v2/publication_timeslots/{id} | Show publication timeslot
[**api_v2_publication_timeslots_id_patch**](PublicationTimeslotsApi.md#api_v2_publication_timeslots_id_patch) | **PATCH** /api/v2/publication_timeslots/{id} | Update publication timeslot

# **api_v2_assignments_assignment_id_publication_timeslots_get**
> list[InlineResponse20015] api_v2_assignments_assignment_id_publication_timeslots_get(assignment_id, items=items, page=page)

List publication timeslots

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PublicationTimeslotsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List publication timeslots
    api_response = api_instance.api_v2_assignments_assignment_id_publication_timeslots_get(assignment_id, items=items, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationTimeslotsApi->api_v2_assignments_assignment_id_publication_timeslots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **items** | **int**| Items per page, possible values are 5, 10, 20, 50 and 100 | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**list[InlineResponse20015]**](InlineResponse20015.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_assignments_assignment_id_publication_timeslots_post**
> InlineResponse20015 api_v2_assignments_assignment_id_publication_timeslots_post(assignment_id, body=body)

Create publication timeslot

All students are selected for the timeslot if the klass_id and group_id are null and with_extra_time is false. Either group_id or klass_id can be set, not both. If either klass_id or group_id is set, with_extra_time must be false. Otherwise if klass_id and group_id are null, with_extra_time can be true, which sets a timeslot for students with the right to extra time

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PublicationTimeslotsApi(ans_app_api.ApiClient(configuration))
assignment_id = 'assignment_id_example' # str | assignment_id
body = ans_app_api.AssignmentIdPublicationTimeslotsBody() # AssignmentIdPublicationTimeslotsBody |  (optional)

try:
    # Create publication timeslot
    api_response = api_instance.api_v2_assignments_assignment_id_publication_timeslots_post(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationTimeslotsApi->api_v2_assignments_assignment_id_publication_timeslots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| assignment_id | 
 **body** | [**AssignmentIdPublicationTimeslotsBody**](AssignmentIdPublicationTimeslotsBody.md)|  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_publication_timeslots_id_delete**
> api_v2_publication_timeslots_id_delete(id)

Delete publication timeslot

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PublicationTimeslotsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete publication timeslot
    api_instance.api_v2_publication_timeslots_id_delete(id)
except ApiException as e:
    print("Exception when calling PublicationTimeslotsApi->api_v2_publication_timeslots_id_delete: %s\n" % e)
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

# **api_v2_publication_timeslots_id_get**
> InlineResponse20015 api_v2_publication_timeslots_id_get(id)

Show publication timeslot

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PublicationTimeslotsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show publication timeslot
    api_response = api_instance.api_v2_publication_timeslots_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationTimeslotsApi->api_v2_publication_timeslots_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_publication_timeslots_id_patch**
> InlineResponse20015 api_v2_publication_timeslots_id_patch(id, body=body)

Update publication timeslot

All students are selected for the timeslot if the klass_id and group_id are null and with_extra_time is false. Either group_id or klass_id can be set, not both. If either klass_id or group_id is set, with_extra_time must be false. Otherwise if klass_id and group_id are null, with_extra_time can be true, which sets a timeslot for students with the right to extra time

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.PublicationTimeslotsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.PublicationTimeslotsIdBody() # PublicationTimeslotsIdBody |  (optional)

try:
    # Update publication timeslot
    api_response = api_instance.api_v2_publication_timeslots_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationTimeslotsApi->api_v2_publication_timeslots_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**PublicationTimeslotsIdBody**](PublicationTimeslotsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


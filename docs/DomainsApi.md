# ans_app_api.DomainsApi

All URIs are relative to *https://ans.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_courses_course_id_domains_get**](DomainsApi.md#api_v2_courses_course_id_domains_get) | **GET** /api/v2/courses/{course_id}/domains | List course domains
[**api_v2_courses_course_id_domains_post**](DomainsApi.md#api_v2_courses_course_id_domains_post) | **POST** /api/v2/courses/{course_id}/domains | Create course domain
[**api_v2_domains_id_delete**](DomainsApi.md#api_v2_domains_id_delete) | **DELETE** /api/v2/domains/{id} | Delete domain
[**api_v2_domains_id_get**](DomainsApi.md#api_v2_domains_id_get) | **GET** /api/v2/domains/{id} | Show domain
[**api_v2_domains_id_patch**](DomainsApi.md#api_v2_domains_id_patch) | **PATCH** /api/v2/domains/{id} | Update domain
[**api_v2_question_banks_question_bank_id_domains_get**](DomainsApi.md#api_v2_question_banks_question_bank_id_domains_get) | **GET** /api/v2/question_banks/{question_bank_id}/domains | List question bank domains
[**api_v2_question_banks_question_bank_id_domains_post**](DomainsApi.md#api_v2_question_banks_question_bank_id_domains_post) | **POST** /api/v2/question_banks/{question_bank_id}/domains | Create question bank domain

# **api_v2_courses_course_id_domains_get**
> api_v2_courses_course_id_domains_get(course_id, items=items, page=page)

List course domains

List all domains in a course

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DomainsApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List course domains
    api_instance.api_v2_courses_course_id_domains_get(course_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling DomainsApi->api_v2_courses_course_id_domains_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 
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

# **api_v2_courses_course_id_domains_post**
> api_v2_courses_course_id_domains_post(course_id, body=body)

Create course domain

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DomainsApi(ans_app_api.ApiClient(configuration))
course_id = 'course_id_example' # str | course_id
body = ans_app_api.CourseIdDomainsBody() # CourseIdDomainsBody |  (optional)

try:
    # Create course domain
    api_instance.api_v2_courses_course_id_domains_post(course_id, body=body)
except ApiException as e:
    print("Exception when calling DomainsApi->api_v2_courses_course_id_domains_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| course_id | 
 **body** | [**CourseIdDomainsBody**](CourseIdDomainsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_domains_id_delete**
> api_v2_domains_id_delete(id)

Delete domain

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DomainsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete domain
    api_instance.api_v2_domains_id_delete(id)
except ApiException as e:
    print("Exception when calling DomainsApi->api_v2_domains_id_delete: %s\n" % e)
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

# **api_v2_domains_id_get**
> api_v2_domains_id_get(id)

Show domain

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DomainsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Show domain
    api_instance.api_v2_domains_id_get(id)
except ApiException as e:
    print("Exception when calling DomainsApi->api_v2_domains_id_get: %s\n" % e)
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

# **api_v2_domains_id_patch**
> api_v2_domains_id_patch(id, body=body)

Update domain

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DomainsApi(ans_app_api.ApiClient(configuration))
id = 'id_example' # str | id
body = ans_app_api.DomainsIdBody() # DomainsIdBody |  (optional)

try:
    # Update domain
    api_instance.api_v2_domains_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling DomainsApi->api_v2_domains_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **body** | [**DomainsIdBody**](DomainsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_question_banks_question_bank_id_domains_get**
> api_v2_question_banks_question_bank_id_domains_get(question_bank_id, items=items, page=page)

List question bank domains

List all domains in a question bank

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DomainsApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
items = 56 # int | Items per page, possible values are 5, 10, 20, 50 and 100 (optional)
page = 56 # int | Page number (optional)

try:
    # List question bank domains
    api_instance.api_v2_question_banks_question_bank_id_domains_get(question_bank_id, items=items, page=page)
except ApiException as e:
    print("Exception when calling DomainsApi->api_v2_question_banks_question_bank_id_domains_get: %s\n" % e)
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

# **api_v2_question_banks_question_bank_id_domains_post**
> api_v2_question_banks_question_bank_id_domains_post(question_bank_id, body=body)

Create question bank domain

### Example
```python
from __future__ import print_function
import time
import ans_app_api
from ans_app_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ans_app_api.DomainsApi(ans_app_api.ApiClient(configuration))
question_bank_id = 'question_bank_id_example' # str | question_bank_id
body = ans_app_api.QuestionBankIdDomainsBody() # QuestionBankIdDomainsBody |  (optional)

try:
    # Create question bank domain
    api_instance.api_v2_question_banks_question_bank_id_domains_post(question_bank_id, body=body)
except ApiException as e:
    print("Exception when calling DomainsApi->api_v2_question_banks_question_bank_id_domains_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_bank_id** | **str**| question_bank_id | 
 **body** | [**QuestionBankIdDomainsBody**](QuestionBankIdDomainsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


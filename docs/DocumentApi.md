# docstore_python_client.DocumentApi

All URIs are relative to *https://api.docstore.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_document**](DocumentApi.md#add_new_document) | **POST** /document | adds a new document
[**add_new_document_for_template**](DocumentApi.md#add_new_document_for_template) | **POST** /document/template/{templateUuid} | adds a new document by template
[**get_document**](DocumentApi.md#get_document) | **GET** /document/{uuid}/{env} | get latest updated documents
[**get_latest_documents**](DocumentApi.md#get_latest_documents) | **GET** /document | get latest updated documents
[**search_documents**](DocumentApi.md#search_documents) | **POST** /document/search | search for documents


# **add_new_document**
> Document add_new_document(document)

adds a new document

### Example

```python
from __future__ import print_function
import time
import docstore_python_client
from docstore_python_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docstore.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = docstore_python_client.Configuration(
    host = "https://api.docstore.dev"
)


# Enter a context with an instance of the API client
with docstore_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = docstore_python_client.DocumentApi(api_client)
    document = docstore_python_client.Document() # Document | 

    try:
        # adds a new document
        api_response = api_instance.add_new_document(document)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->add_new_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**400** | bad request, see response data for details |  -  |
**403** | operation not allowed for the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_document_for_template**
> Document add_new_document_for_template(template_uuid, template_data)

adds a new document by template

### Example

```python
from __future__ import print_function
import time
import docstore_python_client
from docstore_python_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docstore.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = docstore_python_client.Configuration(
    host = "https://api.docstore.dev"
)


# Enter a context with an instance of the API client
with docstore_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = docstore_python_client.DocumentApi(api_client)
    template_uuid = 'template_uuid_example' # str | 
template_data = docstore_python_client.TemplateData() # TemplateData | 

    try:
        # adds a new document by template
        api_response = api_instance.add_new_document_for_template(template_uuid, template_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->add_new_document_for_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_uuid** | **str**|  | 
 **template_data** | [**TemplateData**](TemplateData.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**400** | bad request, see response data for details |  -  |
**403** | operation not allowed for the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> Document get_document(uuid, env)

get latest updated documents

### Example

```python
from __future__ import print_function
import time
import docstore_python_client
from docstore_python_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docstore.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = docstore_python_client.Configuration(
    host = "https://api.docstore.dev"
)


# Enter a context with an instance of the API client
with docstore_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = docstore_python_client.DocumentApi(api_client)
    uuid = 'uuid_example' # str | 
env = 'env_example' # str | 

    try:
        # get latest updated documents
        api_response = api_instance.get_document(uuid, env)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **env** | **str**|  | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**400** | bad request, see response data for details |  -  |
**403** | operation not allowed for the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_documents**
> list[Document] get_latest_documents()

get latest updated documents

### Example

```python
from __future__ import print_function
import time
import docstore_python_client
from docstore_python_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docstore.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = docstore_python_client.Configuration(
    host = "https://api.docstore.dev"
)


# Enter a context with an instance of the API client
with docstore_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = docstore_python_client.DocumentApi(api_client)
    
    try:
        # get latest updated documents
        api_response = api_instance.get_latest_documents()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->get_latest_documents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**400** | bad request, see response data for details |  -  |
**403** | operation not allowed for the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_documents**
> list[Document] search_documents(body)

search for documents

### Example

```python
from __future__ import print_function
import time
import docstore_python_client
from docstore_python_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.docstore.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = docstore_python_client.Configuration(
    host = "https://api.docstore.dev"
)


# Enter a context with an instance of the API client
with docstore_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = docstore_python_client.DocumentApi(api_client)
    body = 'body_example' # str | 

    try:
        # search for documents
        api_response = api_instance.search_documents(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->search_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**list[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**400** | bad request, see response data for details |  -  |
**403** | operation not allowed for the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


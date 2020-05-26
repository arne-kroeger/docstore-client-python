# docstore-python-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/arne-kroeger/docstore-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/arne-kroeger/docstore-client-python.git`)

Then import the package:
```python
import docstore_python_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import docstore_python_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
with docstore_python_client.ApiClient(configuration) as api_client:
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

## Documentation for API Endpoints

All URIs are relative to *https://api.docstore.dev*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DocumentApi* | [**add_new_document**](docs/DocumentApi.md#add_new_document) | **POST** /document | adds a new document
*DocumentApi* | [**add_new_document_for_template**](docs/DocumentApi.md#add_new_document_for_template) | **POST** /document/template/{templateUuid} | adds a new document by template
*DocumentApi* | [**get_document**](docs/DocumentApi.md#get_document) | **GET** /document/{uuid}/{env} | get latest updated documents
*DocumentApi* | [**get_latest_documents**](docs/DocumentApi.md#get_latest_documents) | **GET** /document | get latest updated documents
*DocumentApi* | [**search_documents**](docs/DocumentApi.md#search_documents) | **POST** /document/search | search for documents


## Documentation For Models

 - [BadRequest](docs/BadRequest.md)
 - [Document](docs/Document.md)
 - [Environment](docs/Environment.md)
 - [ErrorItem](docs/ErrorItem.md)
 - [Space](docs/Space.md)
 - [TemplateData](docs/TemplateData.md)
 - [TemplateVariable](docs/TemplateVariable.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

contact@docstore.dev



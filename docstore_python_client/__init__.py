# coding: utf-8

# flake8: noqa

"""
    docstore API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@docstore.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from docstore_python_client.api.document_api import DocumentApi

# import ApiClient
from docstore_python_client.api_client import ApiClient
from docstore_python_client.configuration import Configuration
from docstore_python_client.exceptions import OpenApiException
from docstore_python_client.exceptions import ApiTypeError
from docstore_python_client.exceptions import ApiValueError
from docstore_python_client.exceptions import ApiKeyError
from docstore_python_client.exceptions import ApiException
# import models into sdk package
from docstore_python_client.models.bad_request import BadRequest
from docstore_python_client.models.document import Document
from docstore_python_client.models.environment import Environment
from docstore_python_client.models.error_item import ErrorItem
from docstore_python_client.models.space import Space
from docstore_python_client.models.template_data import TemplateData
from docstore_python_client.models.template_variable import TemplateVariable

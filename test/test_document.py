# coding: utf-8

"""
    perf::act Documentation API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: documentation@perf-act.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.document import Document  # noqa: E501
from openapi_client.rest import ApiException

class TestDocument(unittest.TestCase):
    """Document unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Document
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.document.Document()  # noqa: E501
        if include_optional :
            return Document(
                id = 56, 
                uuid = '0', 
                title = '0', 
                content = '0', 
                latest_change = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                latest_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                space = openapi_client.models.space.Space(
                    name = '0', ), 
                environment = openapi_client.models.environment.Environment(
                    name = '0', ), 
                other_environments = [
                    openapi_client.models.environment.Environment(
                        name = '0', )
                    ], 
                tags = [
                    '0'
                    ]
            )
        else :
            return Document(
                uuid = '0',
                title = '0',
                content = '0',
                latest_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                space = openapi_client.models.space.Space(
                    name = '0', ),
                environment = openapi_client.models.environment.Environment(
                    name = '0', ),
                other_environments = [
                    openapi_client.models.environment.Environment(
                        name = '0', )
                    ],
                tags = [
                    '0'
                    ],
        )

    def testDocument(self):
        """Test Document"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
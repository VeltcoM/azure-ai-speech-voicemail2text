#!/usr/bin/env python
# coding: utf-8
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.


import pytest
from api_tests.tests.fixtures.http_server_fixture import http_server_fixture
from api_tests.tests.fixtures.http_listener_fixtures import http_listener_fixture
import api_tests.tests.http_tests.http_common_test as http_common_test
from api_tests.core.assert_utils import validate_notes

@pytest.mark.usefixtures('http_listener_fixture')
@pytest.mark.usefixtures('http_server_fixture')
@pytest.mark.httpbadaudio
@pytest.mark.httpregression
def test_bad_audio(http_bad_audio_test):
    test_data = http_bad_audio_test
    response = http_common_test.test_http(test_data)
    http_common_test.valiate_success_external_request_id(response)
    validate_notes(test_data, response)
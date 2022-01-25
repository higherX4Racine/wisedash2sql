# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Configuration and common fixtures for unit tests"""

from pandas import (
    BooleanDtype,
    StringDtype,
    UInt32Dtype,
)

import pytest


@pytest.fixture
def wisedash_fields() -> dict:
    r"""The common fields in all WISEDash tables"""
    return {
        'SCHOOL_YEAR': StringDtype(),
        'AGENCY_TYPE': StringDtype(),
        'CESA': UInt32Dtype(),
        'COUNTY': StringDtype(),
        'DISTRICT_CODE': UInt32Dtype(),
        'SCHOOL_CODE': UInt32Dtype(),
        'GRADE_GROUP': StringDtype(),
        'CHARTER_IND': BooleanDtype(),
        'DISTRICT_NAME': StringDtype(),
        'SCHOOL_NAME': StringDtype(),
        'GROUP_BY': StringDtype(),
        'GROUP_BY_VALUE': StringDtype(),
    }


@pytest.fixture
def wisedash_empty_codes() -> list:
    r"""The string values in WISEDash tables that indicate missing data"""
    return [
        '*'
    ]


@pytest.fixture
def wisedash_false_codes() -> list:
    r"""The string values in WISEDash tables that indicate missing data"""
    return [
        'N',
        'n',
        'No',
        'no',
    ]


@pytest.fixture
def wisedash_truth_codes() -> list:
    r"""The string values in WISEDash tables that indicate missing data"""
    return [
        'Y',
        'y',
        'Yes',
        'yes',
    ]



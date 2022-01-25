# Copyright (C) 2022 by Higher Expectations for Racine County

from pandas import (
    Float32Dtype,
    StringDtype,
    UInt32Dtype,
)

import pytest

from wisedash2sql.importers import ForwardImporter


@pytest.fixture
def extra_forward_fields():
    r"""The additional fields present in WISEDash Forward Exam data tables"""
    return {
        'TEST_SUBJECT': StringDtype(),
        'GRADE_LEVEL': StringDtype(),
        'TEST_RESULT': StringDtype(),
        'TEST_RESULT_CODE': UInt32Dtype(),
        'TEST_GROUP': StringDtype(),
        'STUDENT_COUNT': UInt32Dtype(),
        'PERCENT_OF_GROUP': Float32Dtype(),
        'GROUP_COUNT': UInt32Dtype(),
        'FORWARD_AVERAGE_SCALE_SCORE': Float32Dtype(),
    }


@pytest.fixture
def extra_forward_empty_codes():
    r"""There is at least one extra empty code in Forward Exam data"""
    return [
        'No Test',
        'no test',
    ]


@pytest.fixture
def forward_importer():
    r"""An instance of a ForwardImporter"""
    return ForwardImporter()


def test_forward_dtypes(forward_importer,
                        wisedash_fields,
                        extra_forward_fields):
    r"""Successfully import Forward Exam Data"""

    assert forward_importer.column_types == \
           wisedash_fields | extra_forward_fields


def test_forward_empty_codes(forward_importer,
                             wisedash_empty_codes,
                             extra_forward_empty_codes):
    r"""Be aware of the correct 'empty value' codes."""

    assert forward_importer.empty_codes == \
           wisedash_empty_codes + extra_forward_empty_codes

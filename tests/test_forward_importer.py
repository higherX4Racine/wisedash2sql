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


def test_forward_importer(wisedash_fields,
                          extra_forward_fields):
    r"""Successfully import Forward Exam Data"""

    importer = ForwardImporter()
    assert importer.column_types == wisedash_fields | extra_forward_fields

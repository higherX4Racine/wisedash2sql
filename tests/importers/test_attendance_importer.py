# Copyright (C) 2022 by Higher Expectations for Racine County
r"""AttendanceImporter objects help read tables about attendance"""

from pandas import (
    Float32Dtype,
    StringDtype,
    UInt32Dtype,
)

import pytest

from wisedash2sql.importers import AttendanceImporter


@pytest.fixture
def extra_attendance_fields():
    r"""Fields that are specific to attendance tables"""
    return {
        'ABSENTEE_MEASURE': StringDtype(),
        'STUDENT_COUNT': UInt32Dtype(),
        'ABSENCE_COUNT': UInt32Dtype(),
        'ABSENCE_RATE': Float32Dtype(),
    }


def test_attendance_importer(wisedash_fields,
                             extra_attendance_fields):
    r"""AttendanceImporter objects identify common and subject-specific fields"""
    importer = AttendanceImporter()
    assert importer.column_types == wisedash_fields | extra_attendance_fields

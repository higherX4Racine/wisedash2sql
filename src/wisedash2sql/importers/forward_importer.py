# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Logic and Settings for importing data tables about the Forward Exam"""

from pandas import (
    Float32Dtype,
    StringDtype,
    UInt32Dtype,
)

from wisedash2sql.importers.wisedash_importer import WISEDashImporter


class ForwardImporter(WISEDashImporter):
    r"""Instances can import Forward Exam data tables from WI DPI."""

    def __init__(self):
        super().__init__()
        self._column_types = super().column_types | {
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

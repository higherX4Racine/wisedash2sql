# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Logic and settings for importing attendance data."""

from pandas import (
    Float32Dtype,
    StringDtype,
    UInt32Dtype,
)

from wisedash2sql.importers.wisedash_importer import WISEDashImporter


class AttendanceImporter(WISEDashImporter):
    r"""Logic and settings to read WISEDash attendance spreadsheets

    """

    def __init__(self):
        super().__init__()
        self._column_types = super().column_types | {
            'ABSENTEE_MEASURE': StringDtype(),
            'STUDENT_COUNT': UInt32Dtype(),
            'ABSENCE_COUNT': UInt32Dtype(),
            'ABSENCE_RATE': Float32Dtype(),
        }

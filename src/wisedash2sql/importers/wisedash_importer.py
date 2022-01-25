# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Logic and settings that all WISEDash tables have in common."""

from pandas import (
    BooleanDtype,
    StringDtype,
    UInt32Dtype,
)


class WISEDashImporter:
    r"""Logic and settings for importing WISEDash spreadsheets.

    """

    def __init__(self):
        self._column_types = {
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
        self._empty_codes = ['*']
        self._false_codes = ['No', 'no', 'N', 'n']
        self._truth_codes = ['Yes', 'yes', 'Y', 'y']

    @property
    def column_types(self) -> dict:
        r"""A column name-column type dictionary"""

        return self._column_types

    @property
    def empty_codes(self) -> list:
        r"""A list of string values that count as `NA`, `NaN`, or `None`"""
        return self._empty_codes

    @property
    def false_codes(self) -> list:
        r"""A list of string values that count as `False`"""
        return self._false_codes

    @property
    def truth_codes(self) -> list:
        r"""A list of string values that count as `True`"""
        return self._truth_codes

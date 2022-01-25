# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Logic and settings that all WISEDash tables have in common."""

from pandas import (
    BooleanDtype,
    StringDtype,
    UInt32Dtype,
    read_csv,
    read_excel,
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

    def read_table(self, table_file, *args, **kwargs):
        r"""read in a CSV or Excel file.

        Parameters
        ----------
        table_file : path-like
            The path to and file name of the data table
        *args : list
            Further positional arguments to pass to the `pandas` function.
        **kwargs : dict
            Further key-value arguments to pass to the `pandas` function.

        """

        file_extension = table_file[-3:].lower()
        if file_extension == 'csv':
            func = read_csv
        elif file_extension in ('xls', 'xlsx'):
            func = read_excel
        else:
            raise ValueError('the file must be in CSV or Excel format')

        return func(table_file,
                    header=0,
                    dtype=self.column_types,
                    true_values=self.truth_codes,
                    false_values=self.false_codes,
                    na_values=self.empty_codes,
                    *args,
                    **kwargs)

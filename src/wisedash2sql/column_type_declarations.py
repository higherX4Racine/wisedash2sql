# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Specific column types."""

from sqlite3 import (
    Binary,
    Date,
)

from numpy import (
    bytes_,
    float_,
    int_,
    str_,
)

from .column_data_type import ColumnDataType


COLUMN_BLOB = ColumnDataType('blob',
                             bytes_,
                             Binary)
r"""A blob or buffer of raw binary data."""

COLUMN_COUNT = ColumnDataType('count',
                              int_,
                              int)
r"""A column of whole numbers, like counts."""

COLUMN_REAL = ColumnDataType('real',
                             float_,
                             float)
r"""A column of continuous numeric data, like percentages."""

COLUMN_TEXT = ColumnDataType('text',
                             str_,
                             str)
r"""A column of text data, like category labels or long notes."""

COLUMN_DATE = ColumnDataType('date',
                             str_,
                             Date)
r"""A column of date-times in YYYY-MM-DD HH:MM:SS format."""

COLUMN_NULL = ColumnDataType('null',
                             float_,
                             type(None))
r"""A NULL column."""

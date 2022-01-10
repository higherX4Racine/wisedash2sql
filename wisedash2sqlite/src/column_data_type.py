# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Type declarations for columns"""

from numpy import dtype


class ColumnDataType:
    r"""Define a mapping between `pandas` and `dbapi` types

    Parameter
    ---------
    name : str
        The name of the type
    np_type : np.dtype
        The column's data format when stored as a pandas data frame.
    db_type : type
        The column's data format when stored in a DBAPI database.

    """

    def __init__(self,
                 name: str,
                 np_type: dtype,
                 db_type: type):
        self._name = name
        self._np_type = np_type
        self._db_type = db_type

    @property
    def name(self) -> str:
        r"""The name of a type, not of any column in particular"""
        return self._name

    @property
    def numpy_type(self) -> dtype:
        r"""The numpy type that pandas uses to store this kind of column."""
        return self._np_type

    @property
    def dbapi_type(self) -> type:
        r"""The custom type that sqlite3 uses to store this kind of column."""
        return self._db_type

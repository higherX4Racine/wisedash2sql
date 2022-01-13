# Copyright (C) 2021 by Higher Expectations for Racine County
r"""A quick toy for reading a CSV file into an SQLite table."""

import csv
import sqlite3
import sys
from typing import Iterable, Tuple


_SNIFF_READ_LENGTH = 65536


def _sniff_dialect(file_handle,
                   read_length = _SNIFF_READ_LENGTH) -> csv.Dialect:
    r"""Inspect a file for the details of its csv format."""

    file_handle.seek(0)
    dialect = csv.Sniffer().sniff(file_handle.read(read_length))
    file_handle.seek(0)
    return dialect


def _table_sql(table_name : str,
               headers : Iterable,
               type_defs : Iterable=None) -> str:
    r"""Make an SQL command that create a table defined by headers."""

    if type_defs is not None:
        headers = [f'{a} {b}' for a, b in zip(headers, type_defs)]

    return f'CREATE TABLE {table_name}({ ", ".join(headers) });'


def _row_sql(table_name : str,
             n_columns : int) -> str:
    r"""Make an SQL command to read a row of data."""

    q = ['quote(?)'] * n_columns

    return f'INSERT INTO {table_name} VALUES({ ", ".join(q) });'


def csv_to_sqlite(csv_filename : str,
                  database_filename : str,
                  table_name : str) -> Tuple:
    r"""Migrate data from a CSV file to an SQLite table.

    Parameters
    ----------
    csv_filename : str
        The absolute path to and file name of the CSV file.
    database_filename : str
        The absolute path to and file name of the database file.
    table_name : str
        The name that you want the new table to have.

    Returns
    -------
    int : the number of rows in the output table
    int : the number of columns in the output table
    int : the number of errors that occurred while parsing rows

    """

    conn = sqlite3.connect(database_filename)
    sql_cursor = conn.cursor()
        
    with open(csv_filename, 'r') as csv_file:

        dialect = _sniff_dialect(csv_file)

        csv_reader = csv.reader(csv_file, dialect)

        headers = next(csv_reader)

        n_columns = len(headers)
        n_rows = 0
        n_errors = 0

        try:
            sql_cursor.execute(_table_sql(table_name,
                                          headers))
        except sqlite3.Error as e:
            print(f'Error creating {table_name}: {e}')

            sys.exit(1)

        for fields in csv_reader:

            n_rows += 1

            try:
                sql_cursor.execute(_row_sql(table_name,
                                            len(fields)),
                                   fields)

            except sqlite3.Error as e:
                n_errors += 1
                print(f'Error reading line {n_rows}: {e}')

    conn.commit()

    conn.close()

    return (n_rows - n_errors, n_columns, n_errors)

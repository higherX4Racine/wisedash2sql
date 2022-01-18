# Copyright (C) 2021 by Higher Expectations for Racine County
r"""read zip files and add them to a SQLite table."""

from contextlib import contextmanager
import io
import os
import zipfile


@contextmanager
def zipped_csv_handle(archive_base_name: str,
                      dir_path: str = '',
                      file_base_name: str = None,
                      mode: str = 'r'):
    r"""Access a zipped csv file as a TextIOBase stream.

    Parameters
    ----------
    archive_base_name : str
        The name of the zip archive, without its extension
    dir_path : str, optional
        The path to the archive. Defaults to ''
    file_base_name : str, optional
        The name of the csv file in the archive, if it is different
    mode : str, optional
        Either 'r' to read the file or 'w' to write the file

    Yields
    ------
    io.TextIOWrapper : a character stream

    """

    if file_base_name is None:
        file_base_name = archive_base_name

    with zipfile.ZipFile(os.path.join(dir_path,
                                      f'{archive_base_name}.zip'),
                         mode) as archive:
        with archive.open(f'{file_base_name}.csv', mode) as bh:
            with io.TextIOWrapper(bh) as fh:
                yield fh

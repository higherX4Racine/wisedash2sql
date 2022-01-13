# Copyright (C) 2021 by Higher Expectations for Racine County
r"""Learning how to use `pandas` to idiomatically read in messy Excel files."""

from typing import (
    Iterable,
)

import pandas as pd


def separate_like_tidy(df: pd.DataFrame,
                       target_column: str,
                       separator: str,
                       new_names: list = [],
                       remove: bool=True) -> pd.DataFrame:

    target_index = df.columns.get_loc(target_column) + 1

    separated = df[target_column].str.split(separator,
                                            expand=True)

    if len(new_names) == len(separated.columns):
        separated.columns = new_names

    for n in separated.columns:
        df.insert(target_index,
                  n,
                  separated[n])
        target_index += 1

    if remove:
        df.drop(target_column,
                axis=1)
    return df


def fix_one_unnamed(s: str,
                    search_pattern: str=) -> str:
    return '' if search_pattern in s else s.strip()


def fix_all_unnamed(iterable: Iterable,
                    separator: str,
                    search_pattern: str) -> str:
    return separator \
           .join(map(lambda u: fix_one_unnamed(u,
                                               search_pattern),
                     iterable)) \
           .strip(separator)

class IndexCleaner:
    r"""Replace blanks and flatten the fields of a `pandas.DataFrame`

    Parameters
    ----------
    separator: str
        A token to insert between fields
    search_pattern: str
        Text that identifies a field name as an auto-filled blank.

    """

    def __init__(self,
                 separator: str,
                 search_pattern: str):
        self._sep = separator
        self._pat = search_pattern

    @property
    def separator(self) -> str:
        r"""The token inserted between the levels of a column's MultiIndex."""
        return self._sep

    @property
    def search_pattern(self) -> str:
        r"""The string that indicates that a field name was blank."""
        return self._pat

    def fix_one(self, s: str) -> str:
        r"""Replace auto-filled blanks and strip whitespace from the input

        Parameters
        ----------
        s: str
            A field name produced by `pandas.read_excel`

        Returns
        -------
        str: `''` if `s` includes `self.search_pattern`, otherwise `s.strip()`

        """

        '' if self._pat in s else s.strip()

    def fix_many(self, iterable: Iterable) -> str:
        r"""Join every field of `iterable` after fixing blanks.

        Parameters
        ----------
        iterable : typing.Iterable
            Probably a `tuple` representing one item in a `pandas.MultiIndex`

        Returns
        -------
        str: a string to use as a value in a `pandas.Index`

        """

        self._sep.join(map(self.fix_one,
                           iterable)) \
                 .strip(self._sep)

def fix_empty_multiindex_values(df: pd.DataFrame,
                                separator: str=';',
                                search_pattern: str=r'Unnamed') -> pd.DataFrame:
    r"""change the multi-indexed headers to flat ones separated by a token.

    Parameters
    ----------
    df: pandas.DataFrame
        A dataframe with an ill-formed multi-index, like you get from merged cells.
    separator: str, optional
        The token that you want to separate valid levels. Defaults to ';'.
    search_pattern: str, optional
        A plain string that is present in index values that should be removed.

    """

    new_index = df.columns

    if isinstance(new_index, pd.MultiIndex):
        new_index.to_flat_index() \
                 .map(lambda u: fix_all_unnamed(u,
                                                separator,
                                                search_pattern))
    else:
        new_index.map(lambda u: fix_one_unnamed(u,
                                                search_pattern))

    df.columns = new_index

    return df

if __name__ == '__main__':

    NO_SUBTOTALS_QUERY = '~District.str.contains("Total$")'
    ID_VARS = ['Dist No.', 'District', 'Position', 'Not Reported', 'Total']
    DEMO_COMB = 'Demographic Combination'
    DEMO_GROUPS = ['Race', 'Sex']
    PEOPLE = 'People'
    NO_EMPTIES_QUERY = f'{PEOPLE} > 0'

    mmxi = pd.read_excel('https://dpi.wi.gov/sites/default/files/imce/cst/xls/sedl11.xls',
                       sheet_name=3,
                       header=[4]) \
           .query(NO_SUBTOTALS_QUERY) \
           .rename(columns={'Dist No':ID_VARS[0]}) \
           .melt(id_vars=ID_VARS,
                 var_name=DEMO_COMB,
                 value_name=PEOPLE) \
           .query(NO_EMPTIES_QUERY) \
           .pipe(separate_like_tidy,
                 DEMO_COMB,
                 ' ',
                 DEMO_GROUPS)

    print(mmxi.head(8))

    mmii = pd.read_excel('https://dpi.wi.gov/sites/default/files/imce/cst/xls/sedl02.xls',
                         sheet_name=2,
                         header=[0, 1]) \
           .pipe(fix_empty_multiindex_values) \
           .query(NO_SUBTOTALS_QUERY) \
           .melt(id_vars=ID_VARS,
                 var_name=DEMO_COMB,
                 value_name=PEOPLE) \
           .query(NO_EMPTIES_QUERY) \
           .pipe(separate_like_tidy,
                 DEMO_COMB,
                 ';',
                 DEMO_GROUPS)

    print(mmii.head(8))

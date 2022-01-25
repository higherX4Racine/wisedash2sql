# Copyright (C) 2022 by Higher Expectations for Racine County
r"""WISEDashImporter objects contain information about data table formats."""

import pytest

from wisedash2sql.wisedash_importer import WISEDashImporter


@pytest.fixture
def wisedash_importer() -> WISEDashImporter:
    r"""A typical WISEDashImporter instance"""
    return WISEDashImporter()


def test_column_types(wisedash_importer,
                      wisedash_fields):
    r"""Match the dictionary of named types to column names and types"""

    assert wisedash_importer.column_types == wisedash_fields


def test_empty_codes(wisedash_importer,
                     wisedash_empty_codes):
    r"""The instance has the correct codes that mean a field is empty"""
    assert list(sorted(wisedash_empty_codes)) == \
           list(sorted(wisedash_importer.empty_codes))


def test_false_codes(wisedash_importer,
                     wisedash_false_codes):
    r"""The instance has the correct codes that mean a field is false"""
    assert list(sorted(wisedash_false_codes)) == \
           list(sorted(wisedash_importer.false_codes))


def test_truth_codes(wisedash_importer,
                     wisedash_truth_codes):
    r"""The instance has the correct codes that mean a field is truth"""
    assert list(sorted(wisedash_truth_codes)) == \
           list(sorted(wisedash_importer.truth_codes))

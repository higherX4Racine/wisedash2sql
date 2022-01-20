# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Test validator mix-ins. There should be a mock table fixture..."""

import pytest

from wisedash2sql.tables.validators import CodeValidator


@pytest.fixture
def forty_two():
    return 42


@pytest.fixture
def hello_world():
    return 'Hello, world!'


def test_code_validator(forty_two, hello_world):
    r"""instantiate without crashing"""

    cv = CodeValidator(field_names=['nothing',
                                    'nil'])

    cv.nothing = forty_two
    cv.nil = hello_world

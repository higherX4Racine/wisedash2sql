# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Validators for table columns"""

from sqlalchemy import orm


class CodeValidator:
    r"""A mix-in for validating enum-like integer codes. Initially broken AF"""
    missing_code = -1

    def __init__(self, field_names, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate_integer_code = orm.validates(self._validate_integer_code,
                                                   *field_names,
                                                   include_removes=False,
                                                   include_backrefs=True)

    def _validate_integer_code(self, _, value):
        r"""Replace non-integer values with a placeholder."""
        try:
            v = int(value)
        except ValueError:
            v = self.missing_code

        return v

# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Validators for table columns"""

from sqlalchemy.orm import validates


class CodeValidator:
    r"""A mix-in for validating enum-like integer codes. Initially broken AF"""
    missing_code = -1

    @validates('DISTRICT_CODE',
               'SCHOOL_CODE',
               'TEST_RESULT_CODE',
               )
    def validate_integer_code(self, _, value):
        r"""Replace non-integer values with a placeholder."""
        try:
            v = int(value)
        except ValueError:
            v = self.missing_code

        return v

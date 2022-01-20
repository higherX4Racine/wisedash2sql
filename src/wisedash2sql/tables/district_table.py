# Copyright (C) 2022 by Higher Expectations for Racine County
r"""A table to keep track of the different school districts in Wisconsin"""

from sqlalchemy import (
    orm,
    Column,
    Float,
    Integer,
    String,
)

from .base_table import BaseTable


class DistrictTable(BaseTable, CodeValidator):
    r"""All of the school districts go in this table.

    """

    missing_real = -1.0

    __tablename__ = 'forward_exam_results'

    id = Column(Integer, primary_key=True)
    SCHOOL_YEAR = Column(String)
    AGENCY_TYPE = Column(String)
    CESA = Column(Integer)
    COUNTY = Column(String)
    DISTRICT_CODE = Column(Integer)
    SCHOOL_CODE = Column(String)
    GRADE_GROUP = Column(String)
    CHARTER_IND = Column(String)
    DISTRICT_NAME = Column(String)
    SCHOOL_NAME = Column(String)
    TEST_SUBJECT = Column(String)
    GRADE_LEVEL = Column(String)
    TEST_RESULT = Column(String)
    TEST_RESULT_CODE = Column(Integer)
    TEST_GROUP = Column(String)
    GROUP_BY = Column(String)
    GROUP_BY_VALUE = Column(String)
    STUDENT_COUNT = Column(Integer)
    PERCENT_OF_GROUP = Column(Float)
    GROUP_COUNT = Column(Integer)
    FORWARD_AVERAGE_SCALE_SCORE = Column(Float)

    @orm.validates('PERCENT_OF_GROUP',
                   'FORWARD_AVERAGE_SCALE_SCORE',
                   )
    def validate_real_number(self, _, value):
        r"""Replace non-float values with a placeholder."""
        try:
            v = float(value)
        except ValueError:
            v = self.missing_real

        return v

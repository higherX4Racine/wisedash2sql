# Copyright (C) 2022 by Higher Expectations for Racine County
r"""ORM description of the WI DPI's Forward Exam data archive."""

from sqlalchemy import (
    orm,
    Column,
    Float,
    Integer,
    String,
)

BaseTable = orm.declarative_base()


class ForwardExamResults(BaseTable):
    r"""Use `sqlalchemy`'s ORM tools to define Forward Exam Results objects."""

    missing_code = -1
    missing_real = -1.0

    __tablename__ = 'forward_exam_results'

    id                          = Column(Integer, primary_key=True)
    SCHOOL_YEAR                 = Column(String)
    AGENCY_TYPE                 = Column(String)
    CESA                        = Column(Integer)
    COUNTY                      = Column(String)
    DISTRICT_CODE               = Column(Integer)
    SCHOOL_CODE                 = Column(String)
    GRADE_GROUP                 = Column(String)
    CHARTER_IND                 = Column(String)
    DISTRICT_NAME               = Column(String)
    SCHOOL_NAME                 = Column(String)
    TEST_SUBJECT                = Column(String)
    GRADE_LEVEL                 = Column(String)
    TEST_RESULT                 = Column(String)
    TEST_RESULT_CODE            = Column(Integer)
    TEST_GROUP                  = Column(String)
    GROUP_BY                    = Column(String)
    GROUP_BY_VALUE              = Column(String)
    STUDENT_COUNT               = Column(Integer)
    PERCENT_OF_GROUP            = Column(Float)
    GROUP_COUNT                 = Column(Integer)
    FORWARD_AVERAGE_SCALE_SCORE = Column(Float)

    @orm.validates('DISTRICT_CODE',
                   'SCHOOL_CODE',
                   'TEST_RESULT_CODE',
                   )
    def validate_integer_code(self, key, value):
        r"""Replace non-integer values with a placeholder."""
        try:
            v = int(value)
        except ValueError:
            v = self.missing_code

        return v

    @orm.validates('PERCENT_OF_GROUP',
                   'FORWARD_AVERAGE_SCALE_SCORE',
                   )
    def validate_real_number(self, key, value):
        r"""Replace non-float values with a placeholder."""
        try:
            v = float(value)
        except ValueError:
            v = self.missing_real

        return v


if __name__ == '__main__':

    import csv
    import itertools
    import os

    import sqlalchemy

    from zip_to_sqlite import zipped_csv_handle

    FILE_BASE = 'forward_certified_2015-16'
    FILE_PATH = r'C:\Users\matts\Documents\Higher Expectations\RUSD\WISEDash Reports\Forward Exam'
    DB_NAME = 'forward_exam.db'

    engine = sqlalchemy.create_engine('sqlite:///' + os.path.join(FILE_PATH, DB_NAME),
                                      echo=True,
                                      future=True)

    BaseTable.metadata.create_all(engine)

    session = sqlalchemy.orm.Session(engine)

    OFFSET = 16000
    COUNT  = 8

    with zipped_csv_handle(FILE_BASE, FILE_PATH) as fh:
        drdr = csv.DictReader(fh)
        for row in itertools.islice(drdr,
                                    OFFSET,
                                    OFFSET + COUNT):
            session.add(ForwardExamResults(**row))

    session.commit()

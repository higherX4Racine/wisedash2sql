# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Classes that hold settings and logic for loading tables from DPI"""

# base class, all others inherit from it
from .wisedash_importer import WISEDashImporter

# concrete importer classes
from .attendance_importer import AttendanceImporter
from .forward_importer import ForwardImporter
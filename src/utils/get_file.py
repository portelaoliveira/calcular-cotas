import os
import sys


def get_file(path, filename, subfolder=None, path_is_file=True):
    if getattr(sys, "frozen", False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
        datadir = os.path.join(datadir, "resources")
        if subfolder is not None:
            datadir = os.path.join(datadir, subfolder)
    else:
        # The application is not frozen
        if path_is_file:
            datadir = os.path.dirname(path)
        else:
            datadir = path
            if subfolder is not None:
                datadir = os.path.join(datadir, subfolder)
    return os.path.join(datadir, filename)

"""

This file contains a method `ztz_similarity(ztz1, ztz2)`
that returns the similarity of sentences `ztz1` and `ztz2`.
ztz = sentence

All other methods in this file are used solely inside
`ztz_similarity(ztz1, ztz2)`

"""
import numpy as np
from globals import *

def get_feature(ztz):
    """

    Parameters
    ----------
    ztz: str

    Returns
    -------
    str | None

    """
    if "&z=" not in ztz:
        return None
    return ztz.split()[0].strip().replace("=", "")

def get_z(ztz):
    """

    Parameters
    ----------
    ztz: str

    Returns
    -------
    float

    """
    if "&z=" not in ztz:
        return None
    return float(ztz.split()[-1].strip())

def get_day(ztz):
    """

    Parameters
    ----------
    ztz: str

    Returns
    -------
    str

    """
    if "Today" not in ztz:
        return None
    return ztz.split()[-1].strip()

def get_common_feature(ztz1, ztz2):
    """

    Parameters
    ----------
    ztz1: str
    ztz2: str

    Returns
    -------
    str | None

    """
    feature1 = get_feature(ztz1)
    feature2 = get_feature(ztz2)
    if feature1 == feature2 and feature1 in FEATURES:
        return feature1
    else:
        return None
    
def get_common_day(ztz1, ztz2):
    """

    Parameters
    ----------
    ztz1: str
    ztz2: str

    Returns
    -------
    str | None

    """
    day1 = get_day(ztz1)
    day2 = get_day(ztz2)
    if day1 == day2 and day1 in DAYS:
        return day1
    else:
        return None

def ztz_similarity(ztz1, ztz2, **kwargs):
    """
    This method returns the similarity between sentences `ztz1` and `ztz2`.
    The similarity is measured as odds of a probability, so it ranges from 0
    to infinity.

    elif "LogDiff" in col_name:
        str0 = f"{col_name} is {entry} after {time_diff} {ZTZ_SEPARATOR}"
    else:
        str0 = f"{col_name} is {entry} {ZTZ_SEPARATOR}"

    Parameters
    ----------
    ztz1: str
    ztz2: str
    kwargs: dict[]

    Returns
    -------
    float

    """
    feature = get_common_feature(ztz1, ztz2)
    # day = get_common_day(ztz1, ztz2)
    day = None
    z1 = get_z(ztz1)
    z2 = get_z(ztz2)
    if feature and abs(z1-z2) < Z_RADIUS:
        # ssents are  similar
        # print("asderf", feature, abs(z1-z2))
        return SIMI_THRESHOLD + 1
    else:
        # ssents are too different
        return SIMI_THRESHOLD - 1

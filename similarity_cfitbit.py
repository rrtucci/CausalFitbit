"""

This file contains a function `ztz_similarity(ztz1, ztz2)`
that returns the similarity of sentences `ztz1` and `ztz2`.
ztz = sentence


"""
import numpy as np
from cfitbit_globals import *

def get_feature(ztz):
    return ztz.split().strip()[0].replace("=", "")

def get_z(ztz):
    return ztz.split().strip()[-1]

def get_common_feature(ztz1, ztz2):
    feature1 = get_feature(ztz1)
    feature2 = get_feature(ztz2)
    if feature1 == feature2 and feature1 in FEATURES:
        return feature1
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
    if not feature:
        return 0

    z1 = get_z(ztz1)
    z2 = get_z(ztz2)
    if abs(z1-z2) < Z_RADIUS:
        # ssents are  similar
        return SIMI_THRESHOLD + 1
    else:
        # ssents are too different
        return SIMI_THRESHOLD - 1

"""

This file contains a function `ztz_similarity(ztz1, ztz2)`
that returns the similarity of sentences `ztz1` and `ztz2`.
ztz = sentence


"""
from globals import *

def get_simi_root(ztz1, ztz2):
    root0 = None
    for root in SIMI_ROOTS:
        if root in ztz1 and root in ztz2:
            root0 = root
            break
    return root0

def get_diff_case(ztz1, ztz2):
    if "LogDiff" in ztz1 and "LogDiff" in ztz2:
        return "LogDiff"
    else:
        return ""

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
    root = get_simi_root(ztz1, ztz2)
    diff_case = get_diff_case(ztz1, ztz2)
    if not root or not diff_case:
        return 0
    else:
        if not diff_case:
            quantity1= float(ztz1.split()[-1].strip())
            quantity2 = float(ztz2.split()[-1].strip())
        else:
            time1= float(ztz1.split()[-1].strip())
            time2 = float(ztz2.split()[-1].strip())
            fraction1= float(ztz1.split()[-3].strip())
            fraction2 = float(ztz2.split()[-3].strip())


    return round(odds, 3)

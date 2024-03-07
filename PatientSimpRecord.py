import os
import pandas as pd
import numpy as np
from globals import *
from utils import *


class PatientSimpRecord:
    """
    The purpose of this class is to generate, for each patient, a simp file
    such as `patient_simp_records/patient_1503960366.txt`. These files are
    then used as input to the class DagAtlas , which creates a DAG atlas.

    Attributes
    ----------
    col_to_avg_std: dict[str, tuple(int, int)]
        this dictionary maps the column named `col` to a tuple containing
        the average and standard deviation for the column `col`
    df: pd.DataFrame
    id_str: str
    """

    def __init__(self, id_str):
        """
        constructor

        Parameters
        ----------
        id_str: str
        """
        self.id_str = id_str
        path = "patient_csv_records/patient_" + id_str + ".csv"
        self.df = pd.read_csv(path)
        self.col_to_avg_std = {}
        for col in self.df.columns:
            if col not in ID_TIME_COLS:
                self.col_to_avg_std[col] = \
                    (self.df[col].mean(), self.df[col].std())

    def get_ssent(self, row, col):
        """
        This method is called within `get_patient_simp_file()`. It returns a
        ssent (simple sentence) such as `f1=2.8 &z= .1` for row `row` and
        col `col'. (row, col)=(t, x) coordinates.

        Parameters
        ----------
        row: int
        col: str

        Returns
        -------
        str

        """
        zless_cols = ["Id", "DateTime", "DateTimeDiff", "DayOfWeek"]
        forbidden_num_strs = ["nan", "inf", "-inf", "", "None"]
        entry = self.df.at[row, col]
        if col in zless_cols:
            if col == "DayOfWeek":
                str0 = f"Today is {entry} {ZTZ_SEPARATOR}"
            else:
                str0 = ""
        else:
            avg, std = self.col_to_avg_std[col]
            if str(entry) not in forbidden_num_strs and \
                    str(avg) not in forbidden_num_strs and \
                    str(std) not in forbidden_num_strs and std:
                z = (entry - avg) / std
                z = round(z, 3)
                str0 = f"{col}= {entry} &z= {z} {ZTZ_SEPARATOR}"
            else:
                str0 = ""
        return str0

    def write_patient_simp_file(self):
        """
        This method reads files for each patient with paths like
        `patient_csv_records/patient_1503960366.csv`

        The method writes files for each patient with paths like
        `patient_simp_records/patient_1503960366.txt`

        The method replaces a line (with header)  like
        f1   f2
        2.8  3.4
        by
        f1=2.8 &z= .1 <SEP> f2=3.4 &z= .5

        Returns
        -------
        None

        """
        in_dir = "patient_csv_records"
        out_dir = "patient_simp_records"
        fname = "patient_" + self.id_str + ".csv"
        df = pd.read_csv(in_dir + "/" + fname)
        cols = df.columns.tolist()
        out_path = out_dir + "/" + fname.replace(".csv", ".txt")
        with open(out_path, "w") as out_f:
            out_str = ""
            for row in range(len(df)):
                for col in cols:
                    out_str += self.get_ssent(row, col)
                out_str = out_str[:-len(ZTZ_SEPARATOR)] + "\n"
            out_f.write(out_str)


def write_all_patient_simp_files():
    """
    This method calls the method `write_patient_simp_file()` for each patient.

    Returns
    -------
    None

    """
    fnames = my_listdir("patient_csv_records")
    for fname in fnames:
        patient_id = fname.replace(".csv", "").split("_")[1].strip()
        rec = PatientSimpRecord(patient_id)
        rec.write_patient_simp_file()


if __name__ == "__main__":
    write_all_patient_simp_files()

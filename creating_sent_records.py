import os
import pandas as pd
from globals import *


def create_sent_records():
    in_dir = "patient_csv_records"
    out_dir = "patient_sent_records"
    for fname in os.listdir(in_dir):
        if ".csv" not in fname:
            continue
        df = pd.read_csv(in_dir + "/" + fname)
        col_names = df.columns.tolist()
        out_path = out_dir + "/" + fname.replace(".csv", ".txt")
        with open(out_path, "w") as out_f:
            out_str = ""
            for row in range(len(df)):
                for col_name in col_names:
                    if col_name in ["Id", "DateTime", "DateTimeDiff"]:
                        continue
                    entry = df.at[row, col_name]
                    time_diff = df.at[row, "DateTimeDiff"]
                    if "Diff" not in col_name:
                        if entry:
                            out_str += f"{col_name} is {entry}" \
                                       f" {ZTZ_SEPARATOR}"
                    else:
                        if entry:
                            out_str += f"{col_name} is {entry} after" \
                                       f" {time_diff} {ZTZ_SEPARATOR}"
                out_str = out_str[:-len(ZTZ_SEPARATOR)] + "\n"
            out_f.write(out_str)


if __name__ == "__main__":
    create_sent_records()

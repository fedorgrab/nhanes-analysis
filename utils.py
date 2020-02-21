import os
import pandas as pd
import requests

CURRENT_DIR = os.getcwd()


def percentage(series: pd.Series) -> pd.Series:
    return series / series.sum() * 100


def get_sas_file_from_url(url:str) -> pd.DataFrame:
    request = requests.get(url)
    file_name = url.split("/")[-1]

    with open(file_name, 'wb') as file:
        file.write(request.content)

    pandas_data_frame = pd.read_sas(file_name)
    os.remove(f"{CURRENT_DIR}/{file_name}")
    return pandas_data_frame


def alcohol_use_group_det(instance):
    if instance.ALQ120U == 3:
        if instance.ALQ120Q <= 3:
            return 1
        elif 3 < instance.ALQ120Q < 8:
            return 2
        elif 8 <= instance.ALQ120Q < 17:
            return 3
    elif instance.ALQ120U == 2:
        if instance.ALQ120Q == 1:
            return 3
        elif 2 <= instance.ALQ120Q <= 3:
            return 4
        elif 4 <= instance.ALQ120Q <= 5:
            return 5
        elif 6 <= instance.ALQ120Q <= 12:
            return 6
        elif 13 <= instance.ALQ120Q <= 16:
            return 7
    elif instance.ALQ120U == 1:
        if instance.ALQ120Q == 1:
            return 5
        elif 2 <= instance.ALQ120Q <= 3:
            return 6
        elif instance.ALQ120Q > 3:
            return 7
    return 0


ORIENTATION_MAP = {1: "Gay", 2: "Straight", 3: "Bisexual"}


def orientation_det(instance):
    if instance.RIAGENDR == 1:
        if instance.SXQ296 in [1, 2, 3]:
            return ORIENTATION_MAP[instance.SXQ296]
        else:
            return -9999
    elif instance.RIAGENDR == 2:
        if instance.SXQ295 in [1, 2, 3]:
            return ORIENTATION_MAP[instance.SXQ295]
        else:
            return -9999

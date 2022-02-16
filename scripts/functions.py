import pandas as pd


def yyyymmdd2yyyy_mm_dd(date: str) -> str:
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    date = "{}-{}-{}".format(year,
                             month,
                             day)
    return date


def format_data(data: pd.DataFrame) -> pd.DataFrame:
    data.index = pd.to_datetime(data.index)
    return data


def read_data(path: str, filename: str) -> pd.DataFrame:
    data = pd.read_csv("{}{}".format(path,
                                     filename),
                       index_col=0)
    data = format_data(data)
    return data


def obtain_parameters() -> dict:
    parameters = {"path data": "../Data/",
                  "path graphics": "../Graphics/"}
    return parameters

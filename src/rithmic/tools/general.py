import os
from datetime import datetime as dt
from pathlib import Path

import pytz
from operator import itemgetter

from pandas import DataFrame

from rithmic.tools.pyrithmic_exceptions import RithmicCredentialPathNotSetException


def dict_destructure(input_dict, keys: list):
    missing_keys = [k for k in keys if k not in input_dict.keys()]
    if len(missing_keys) > 0:
        raise KeyError('Not all keys present')
    return itemgetter(*keys)(input_dict)


def get_utc_now():
    return dt.now(tz=pytz.UTC)


def is_datetime_utc(input_datetime: dt) -> bool:
    """Return True if datetime is TZ aware and UTC"""
    if input_datetime.tzinfo is not None:
        return input_datetime.tzinfo == pytz.utc
    return False


def get_credentials_path():
    if 'RITHMIC_CREDENTIALS_PATH' not in os.environ:
        raise RithmicCredentialPathNotSetException('Require OS Environment RITHMIC_CREDENTIALS_PATH with path location of credentials and ssl certificate')
    return Path(os.environ['RITHMIC_CREDENTIALS_PATH'])


def set_index_no_name(df: DataFrame, column_name: str, drop: bool = False) -> DataFrame:
    df = df.set_index(df[column_name], drop=drop)
    df = df.rename_axis(index=None)
    return df

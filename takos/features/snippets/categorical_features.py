import pandas as pd
from typing import *

# count encoding
def create_count_encoding_feature(input_df: pd.DataFrame, use_columns: List[str]) -> pd.DataFrame:
    """
    カウントエンコーディングを行う関数

    Args:
        input_df (pd.DataFrame): インプットとなるデータフレーム
        use_columns (List[str]): カウントエンコーディングを行う対象となるカラム

    Returns:
        pd.DataFrame: カウントエンコーディング後のデータフレーム
    """
    out_df = pd.DataFrame()

    for column in use_columns:
        # 各カラムの値ごとにinput_dfにおけるカウント数を集計する
        value_counts = input_df[column].value_counts()
        out_df[column] = input_df[column].map(vc)

    return out_df.add_prefix("CE_")


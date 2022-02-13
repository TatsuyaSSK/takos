from typing import *

import pandas as pd


# count encoding
def create_count_encoding(input_df: pd.DataFrame, use_columns: List[str]) -> pd.DataFrame:
    """
    カウントエンコーディングを行う関数

    Args:
        input_df (pd.DataFrame): インプットとなるデータフレーム
        use_columns (List[str]): 対象となるカラム

    Returns:
        pd.DataFrame: 適用後のデータフレーム
    """
    out_df = pd.DataFrame()

    for column in use_columns:
        # 各カラムの値ごとにinput_dfにおけるカウント数を集計する
        value_counts = input_df[column].value_counts()
        out_df[column] = input_df[column].map(value_counts)

    return out_df.add_prefix("CE_")


def create_one_hot_encoding(input_df: pd.DataFrame, use_columns: List[str]) -> pd.DataFrame:
    """
    ワンホットエンコーディングを行う関数

    Args:
        input_df (pd.DataFrame): インプットとなるデータフレーム
        use_columns (List[str]): 対象となるカラム

    Returns:
        pd.DataFrame: 適用後のデータフレーム
    """
    out_df = pd.DataFrame()

    for column in use_columns:
        value_counts = input_df[column].value_counts()

        cat = pd.Categorical(input_df[column], categories=value_counts.index)

        # このタイミングでone-hot化
        out_i = pd.get_dummies(cat)
        out_i.columns = out_i.columns.tolist()
        out_i = out_i.add_prefix(f"{column}=")
        out_df = pd.concat([out_df, out_i], axis=1)

    return out_df

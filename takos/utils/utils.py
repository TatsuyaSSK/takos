import os
import random
from contextlib import contextmanager
from time import time

import numpy as np
import tensorflow as tf
import torch


# https://github.com/nyk510/vivid/blob/a1acd915a609a115d470d308d35b5ec45818bf89/vivid/utils.py#L72 より
class Timer:
    def __init__(self, logger=None, format_str="{:.3f}[s]", prefix=None, suffix=None, sep=" "):
        """
        時間を計測する

        Args:
            logger (_type_, optional): _description_. Defaults to None.
            format_str (str, optional): _description_. Defaults to "{:.3f}[s]".
            prefix (_type_, optional): _description_. Defaults to None.
            suffix (_type_, optional): _description_. Defaults to None.
            sep (str, optional): _description_. Defaults to " ".

        Examples:
        for func in tqdm(processors, total=len(processors)):
        with Timer(prefix='create' + func.__name__ + ' '):
            _df = func(input_df)

        """
        if prefix:
            format_str = str(prefix) + sep + format_str
        if suffix:
            format_str = format_str + sep + str(suffix)
        self.format_str = format_str
        self.logger = logger
        self.start = None
        self.end = None

    @property
    def duration(self):
        if not self.end:
            return 0
        return self.end - self.start

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        out_str = self.format_str.format(self.duration)
        if self.logger:
            self.logger.info(out_str)
        else:
            print(out_str)


# https://github.com/nyk510/vivid/blob/a1acd915a609a115d470d308d35b5ec45818bf89/vivid/utils.py#L100 より
def timer(logger=None, format_str="{:.3f}[s]", prefix=None, suffix=None, sep=" "):
    return Timer(logger=logger, format_str=format_str, prefix=prefix, suffix=suffix, sep=sep)


def seed_everything(seed=1234):
    """
    シードを固定する

    Args:
        seed (int, optional): seed値. Defaults to 1234.
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True

import math
import random
from typing import Collection

import numpy as np
import pandas as pd


def generate_boards(input: Collection[str]) -> pd.DataFrame:

    # Shuffle the input each time to get a different result
    input = list(input)
    random.shuffle(input)

    board_size = math.isqrt(len(input))

    # split the array into equal chunks lists
    splitted = np.array_split(input, board_size)

    df = pd.DataFrame(splitted, columns=list(range(1, board_size + 1)))

    return df

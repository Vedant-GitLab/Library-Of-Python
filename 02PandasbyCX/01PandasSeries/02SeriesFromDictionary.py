import numpy as np
import pandas as pd
marks = {
    'maths':67,
    'english':45,
    'hindi':89,
    'science':67
    }

print(pd.Series(marks, name='vedant ke marks'))
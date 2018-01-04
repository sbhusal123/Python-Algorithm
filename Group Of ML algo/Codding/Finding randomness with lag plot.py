from pandas.plotting import lag_plot
import pandas as pd
import numpy as np

data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])

lag_plot(data)

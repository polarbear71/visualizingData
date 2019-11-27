#! /usr/bin/env python

import pandas as pd
from matplotlib import pyplot as plt

sample_data = pd.read_csv('.\\visualizingData\\sample_data.csv')

print(sample_data)

plt.plot(sample_data.column_a, sample_data.column_b)
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()

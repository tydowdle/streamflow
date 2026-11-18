# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime 
# Numpy Array Creation & Slicing
data_provo = np.genfromtxt(
    'June-2021-Provo-River-Streamflow-Rates.csv',
    delimiter=',',
    skip_header=1,
    dtype=str
)

# Column 0: Date (includes timestamp)
x_dates_str = data_provo[:, 0]
x_dates = [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x_dates_str]

# Columns 1 to 5: Site discharge rates
y1 = data_provo[:, 1].astype(float)
y2 = data_provo[:, 2].astype(float)
y3 = data_provo[:, 3].astype(float)
y4 = data_provo[:, 4].astype(float)
y5 = data_provo[:, 5].astype(float)

"""### Graphing the Data

Plot x, y_1, y_2, y_3, y_4, and y_5 with the elements shown in the instructions in the code block below.
"""

# Graphing the Data
plt.figure(figsize=(11, 5))
plt.plot(x_dates, y1, label='Site 10163000')
plt.plot(x_dates, y2, label='Site 10155200')
plt.plot(x_dates, y3, label='Site 10155500')
plt.plot(x_dates, y4, label='Site 10154200')
plt.plot(x_dates, y5, label='Site 10155000')

plt.title('Provo River Streamflow Rates - June 2021')
plt.xlabel('Date')
plt.ylabel('Streamflow Rate (cfs)')
plt.xticks(rotation=45)  # Rotated labels requirement
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

import os
from pdb import set_trace as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# "gpu" site:ir.aboutamazon.com after:2023-01-01 Purchases of property and equipment
# "gpu" site:investor.fb.com Purchases of property and equipment, net
# "gpu" site:abc.xyz/investor/ after:2023-01-01 Purchases of property and equipment
# "gpu" site:microsoft.com/en-us/Investor/ after:2023-01-01 Additions to property and equipment
# "gpu" site:digitalassets.tesla.com after:2023-01-01


df = pd.DataFrame()

df.index = ['22q2', '22q3', '22q4', '23q1', '23q2', '23q3', '23q4', '24q1', '24q2']
df['nvda'] = [ 3806,  3833,  3616,  4284, 10323, 14514, 18404, 22563, 28000]
df['msft'] = [ 6871,  6283,  6274,  6607,  8943,  9917,  9735, 10952, 13873]
df['meta'] = [ 7572,  9375,  9043,  6823,  6216,  6543,  7665,  6400,  8173]
df['goog'] = [ 6828,  7276,  7595,  6289,  6888,  8055, 11019, 12012, 13186]
df['amzn'] = [15724, 16378, 16592, 14207, 11455, 12479, 14588, 14925, 17620]
df['metacsp'] = (df.meta + df.amzn + df.goog + df.msft) / 2
# df['tsla'] = [ 1730,  1803,  1858,  2072,  2060,  2460,  2306,  2773,  2270]


df /= 1e3
df.plot(use_index=True)
plt.grid()
plt.show()

st()

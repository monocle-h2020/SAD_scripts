#!/usr/bin/env python

''' Simple SNR vs averaging period test'''

import numpy as numpy
import csv
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('./data/test_data_1.dat', delimiter='\s+', header=None)

raw_signal_ref_Path_ratio=plt.plot(data.iloc[:,0],data.iloc[:,7]/data.iloc[:,9])

data_sub=data.loc[900:2849,]
dat_5=data_sub.rolling(5).mean()
dat_100=data_sub.rolling(100).mean()

plt.plot(data_sub[0],data_sub[7]/data_sub[9])
plt.plot(dat_5[0],dat_5[7]/dat_5[9])
plt.plot(dat_100[0],dat_100[7]/dat_100[9])
plt.show()



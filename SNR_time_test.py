#!/usr/bin/env python

''' Simple SNR vs averaging period test'''

import numpy as numpy
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import tqdm
import matplotlib 

data=pd.read_csv('./data/test_data_1.dat', delimiter='\s+', header=None)

raw_signal_ref_Path_ratio=plt.plot(data.iloc[:,0],data.iloc[:,7]/data.iloc[:,9])

data_sub=data.loc[900:2849,]
dat_5=data_sub.rolling(5).mean()
dat_100=data_sub.rolling(100).mean()

plt.plot(data_sub[0],data_sub[7]/data_sub[9])
plt.plot(dat_5[0],dat_5[7]/dat_5[9])
plt.plot(dat_100[0],dat_100[7]/dat_100[9])
plt.show()

SNR=data_sub.rolling(10).mean()/data_sub.rolling(10).std()

data_sub['signal']=300+data_sub.rolling(10).[7]-data_sub[9]

data_sub_start=data_sub.iloc[10:890,:]
plt.plot(data_sub_start['signal'])
plt.savefig('tst.png')

SNR=[]
for i in tqdm.tqdm(np.linspace(5,400,80)):
   x=data_sub_start.rolling(int(i)).mean()['signal']/data_sub_start.rolling(int(i)).std()['signal']
   SNR.append([i,np.mean(x), np.nanpercentile(x, 5), np.nanpercentile(x, 95)])

SNR=np.asarray(SNR)

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 24}

matplotlib.rc('font', **font)

fig=plt.figure(figsize=(28,28))
plotgrid=gridspec.GridSpec(5,1, height_ratios=[2,2,2,2,2])
ax1=plt.subplot(plotgrid[0])
ax2=plt.subplot(plotgrid[1],sharex = ax1)
ax3=plt.subplot(plotgrid[2],sharex = ax1)
ax4=plt.subplot(plotgrid[3],sharex = ax1)
ax5=plt.subplot(plotgrid[4])
fig.subplots_adjust(hspace=0.04)
ax1.plot(data_sub_start[0],data_sub_start['signal'])
ax1.set_xticklabels([])
ax1.set_ylim(0,4000)
plt.text(0.8,0.65, 'Raw absorption signal at\n approx 40ms sampling' , transform=ax1.transAxes)
ax2.plot(data_sub_start.rolling(10).mean()[0],data_sub_start.rolling(10).mean()['signal']/data_sub_start.rolling(10).std()['signal'])
ax2.set_xticklabels([])
ax2.hlines(np.linspace(50,250,5), data_sub_start[0].iloc[0] ,data_sub_start[0].iloc[-1], color='red')
plt.text(0.8,0.8, 'SNR for 0.4 second\n rolling window' , transform=ax2.transAxes)
ax3.plot(data_sub_start.rolling(50).mean()[0],data_sub_start.rolling(50).mean()['signal']/data_sub_start.rolling(50).std()['signal'])
ax3.hlines(np.linspace(50,250,5), data_sub_start[0].iloc[0] ,data_sub_start[0].iloc[-1], color='red')
ax3.set_xticklabels([])
plt.text(0.8,0.8, 'SNR for 2 second\n rolling window' , transform=ax3.transAxes)
ax4.plot(data_sub_start.rolling(200).mean()[0],data_sub_start.rolling(200).mean()['signal']/data_sub_start.rolling(200).std()['signal'])
ax4.hlines(np.linspace(50,250,5), data_sub_start[0].iloc[0] ,data_sub_start[0].iloc[-1], color='red')
plt.text(0.8,0.8, 'SNR for 8 second\n rolling window' , transform=ax4.transAxes)
ax5.plot(SNR[:,0] , SNR[:,1], label='mean SNR', lw=3)
ax5.plot(SNR[:,0] , SNR[:,2], label='5th percentile SNR', lw=3)
ax5.plot(SNR[:,0] , SNR[:,3], label='p5th percentile SNR', lw=3)
ax5.set_yscale('log')
ax5.set_xlabel('Rolling window width (number of raw measurements)')
ax5.set_ylabel('SNR ratio')
ax5.legend(loc='lower right',frameon=False)
plt.savefig('test_plot_1.png')





import os, glob, time, h5py, warnings

import multiprocessing as mp
import matplotlib.pyplot as plt   # plots
import numpy as np
import scipy.sparse as sp
from scipy.optimize import curve_fit

from liblibra_core import *
import util.libutil as comn

import libra_py
from libra_py import units, data_conv #, dynamics_plotting
import libra_py.dynamics.tsh.compute as tsh_dynamics
#import libra_py.dynamics.tsh.plot as tsh_dynamics_plot
#import libra_py.data_savers as data_savers
import libra_py.workflows.nbra.decoherence_times as decoherence_times
import libra_py.data_visualize

from recipes import dish_nbra, fssh_nbra, fssh2_nbra, gfsh_nbra, ida_nbra, mash_nbra, msdm_nbra

#from matplotlib.mlab import griddata
#:wmatplotlib inline 
warnings.filterwarnings('ignore')


def exp_funct(t, _x):
    return 1 - np.exp(-np.power(t/_x, 1))

ICONDS = list(range(1,3000,100))
for c, method in enumerate(['FSSH', 'DISH', 'MSDM', 'IDA']):
    taus = []
    plt.subplot(2,2,c+1)
    #for icond in range(1,1000,300):
    for icond in ICONDS:
      #  print( F'{method}_icond_{icond}/mem_data.hdf' )
        F = h5py.File(F'{method}_icond_{icond}/mem_data.hdf')                
        sh_pop = np.array(F['sh_pop_adi/data'][:,0]) 
        se_pop = np.array(F['se_pop_adi/data'][:,0]) 
        md_time = np.array(F['time/data'][:]) * units.au2fs
        plt.plot(md_time, sh_pop, color='gray')
        F.close()
        
        popt, pcov = curve_fit( exp_funct, md_time, sh_pop, bounds=([0.0],[np.inf]))
        _tau = popt
        
        # Computing the R-squared
        residuals  = sh_pop - exp_funct(md_time, *popt)
        ss_res     = np.sum(residuals**2)
        ss_tot     = np.sum((sh_pop - np.mean(sh_pop))**2)
        r_squared  = 1.0 - (ss_res / ss_tot)        
     #   print(F"R2 = {r_squared}")
        
        if True:#r_squared>0.1:
            taus.append(_tau)
        
    plt.ylabel('Population')
    plt.xlabel('Time, fs')
    
    taus = np.array(taus)    
    ave_tau = np.average(taus)
    ave_tau = ave_tau/1000
    s = np.std(taus)
    Z = 1.96
    N = taus.shape[0]
    error_bar = Z*s/np.sqrt(N)
    error_bar = error_bar/1000

    print('The timescales for method {}: {:.2f}+-{:.2f} ps'.format(method, ave_tau, error_bar))
    clr = libra_py.data_visualize.colors[ libra_py.data_visualize.clrs_index[c]]
    ave_tau = np.average(taus)
    error_bar = Z*s/np.sqrt(N)
    plt.plot(md_time, exp_funct(md_time, ave_tau-error_bar), ls='--', color=clr)
    plt.plot(md_time, exp_funct(md_time, ave_tau), ls='-',  color=clr)
    plt.plot(md_time, exp_funct(md_time, ave_tau+error_bar), ls='--', color=clr)
#    plt.xlim(1685,1691)
    plt.savefig('dynamics.png')
    plt.legend()
    plt.tight_layout()


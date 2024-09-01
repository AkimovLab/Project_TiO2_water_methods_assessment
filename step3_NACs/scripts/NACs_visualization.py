import os
import glob
import numpy as np
import scipy.sparse as sp
from libra_py import units, data_stat, influence_spectrum
import matplotlib.pyplot as plt
from liblibra_core import *
from libra_py.workflows.nbra import step3
import libra_py.packages.cp2k.methods as CP2K_methods

params = {"path_to_energy_files": "res-mb-sd-DFT", "dt": 1.0, 
          "prefix": "Hvib_sd_", "suffix": "_re", "istep": 1000, "fstep": 1002}

plt.figure()
nac_ave_01 = []
titles = ['MB']
for c1, basis in enumerate([ 'ci']):
    plt.subplot(1, 1, c1+1)
    nac_files = glob.glob(F'res-mb-sd-DFT/Hvib_{basis}*im*')
    for c2, nac_file in enumerate(nac_files):
        nac_mat = sp.load_npz(nac_file).todense().real
        if c2==0:
            nac_ave = np.zeros(nac_mat.shape)
	    #std_nac = np.zeros(nac_mat.shape)
        nac_ave += np.abs(nac_mat)
        nac_ave_01_valor = nac_ave[0,1]
        nac_ave_01.append(nac_ave[0,1])

    nac_ave *= 1000*units.au2ev/c2
    nac_ave_01 = np.array(nac_ave_01)
    nac_ave_01 *= 1000*units.au2ev/c2
    nac_ave_01_valor *= 1000*units.au2ev/c2
    std_nac_01 = np.std(nac_ave_01) 
    print(std_nac_01)
    print(nac_ave_01_valor)  
    print(nac_ave)  
#    std_nac *= 1000*units.au2ev/c2
#    rounded_nac_ave = np.round(nac_ave, decimals=4)
#    rounded_nac_ave = rounded_nac_ave[::-1]
#    rounded_std_nac = np.round(std_nac, decimals=4)
#    rounded_std_nac = rounded_std_nac[::-1]
#    file_path = "output_nacs.dat"
#    file_path = "output_nacs.dat"
#    with open(file_path, "w") as file:
#       file.write(str(rounded_nac_ave))
# #      file.write(str(rounded_std_nac))
    nstates = nac_ave.shape[0]
    plt.imshow(np.flipud(nac_ave), cmap='hot', extent=(0,nstates,0,nstates))#, vmin=0, vmax=100)
    plt.xlabel('State index')
    plt.ylabel('State index')
    colorbar = plt.colorbar(shrink=0.50)
    colorbar.ax.set_title('meV')
    plt.clim(vmin=0, vmax=30)
    plt.title(F'{titles[c1]} NACs')
    plt.savefig("NACs_plot.pdf", format="pdf")
    plt.tight_layout()



# Project_TiO2_water_methods_assessment. Step 2: Time-overlaps and TD-DFT calculations

This folder contains inputs, scripts and outputs for computing the molecular orbital overlaps and time-overlaps
**inputs and scripts to be in the same directory to start the calculation**

## 1. inputs

AIMD trajectory for the (TiO2)4(H2O)0 system as example (dynamcis_AIMD.xyz)

CP2K input where TD-DFT options are detailed (es_diag_temp.inp)


## 2. scripts

* `distribute_jobs.py` is the file that you need modify by specifying initial and final step of the trajectory 
and the number of jobs. Libra will split the trajectory based on these values and will submit them by creating 
the specific folders for each job. 

* `run_template.py`: A file that contains the data to run the MO overlap calculations

* `submit_template.slm` the file which will be submitted and runs the python `run.py` where the `run.py` file is the copy 
of the `run_template.py` file but with the initial and final steps filled based on the requested number of jobs and the 
initial and final step for the trajectory. 

* `vmd_input_template`: The VMD input template. This input will be modified by Libra but only the mol load cube and 
rendering line, render Tachyon ... will be changed. You can make your own input template by opening the VMD on your computer 
and from File choose Log Tcl commands to file... and it will append all the commands for reproducing that image into a file. 

To start the TD-DFT calculation simply run: 

    python distribute_jobs.py

* `test.py`: home-made script to run after the calculation is peformed. It tells you the
excitation energies of the various TD-DFT states, the MO involved in such excitations
and the excitation amplitudes.


## 3. outputs

Including all step2 results for each 3000 geometries' trajectories would be extremely difficult, given the 
large number of possible branches: 6 systems x 2 methodologies x 
3 TD-DFT functionals (and given also the weight of MO overlaps and time-overlaps).

For this reason, we include per each of the 36 brances (6x2x3) a file including the excitation energies of the 10 TD-DFT states, the MO involved in such excitations
and the excitation amplitudes (this is indeed the output of running the `test.py` script). This information is contained in a compressed file.
To unpack:

    tar -xjf step2_key_outputs.bz2

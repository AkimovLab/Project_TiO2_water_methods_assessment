# Project_TiO2_water_methods_assessment. Step 1: MD

This folder contains inputs, scripts and outputs for the MD generation of initial nuclear trajectory

** the inputs and scripts to be in the same directory to start the calculation**

## 1. inputs

Two different folders: 

- one for DFT-based AIMD and 

- one for force-fields ffMD

AIMD is performed with CP2K. The folder contains the (TiO2)4(H2O)0 files as case example: geometry (04_00.xyz), 
cp2k input (md.inp) and submit file (submit.slm).

ffMD is performed with GULP code. The folder contains the (TiO2)4(H2O)0 files as case example: input
file (TiO2_04_H2O_0.gin) and submit file (gulpscript.sh)


## 2. scripts

again the submit.slm and gulpscript.sh files for performing each type of MD + the script
for generating the velocity-velocity autocorrelation function and power spectra "velo_autocorr".
To do so, just run: 

    velo_autocorr geo_end.xyz name_system 1 20000 10000 0.0005


(assuming you have 20000 MD steps and the time step is 0.5 fs. The 10000 value is telling the code 
to use this number of MD steps to evaluate the autocorrelation, but as there are 20000 steps, it 
calculates multiple windows of this size and averages to reduce noise.)


## 3. outputs

compressed file with the 3000 geometries' 12 trajectories (6 nanosystems x 2 methodologies)
To unpack:

    tar -xjf trajectory_files.bz2

For the (TiO2)4(H2O)0 system: geo_end.xyz file which is made by positions and velocities
all along the trajectory. This file is needed to obtain the velocity-velocity autocorrelation 
function and power spectra (see below)








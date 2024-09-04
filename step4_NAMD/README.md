# Project_TiO2_water_methods_assessment
scripts and selected outputs from performing the nonadiabatic molecular dynamics (NA-MD) runs

**scripts** 

Again, the inputs are part of the outcome from the previous steps. No "inputs" folder here.

`NAMD_*.py` the script for starting the NA-MD using one trajectory surface hoping
(TSH) method. In our case, we have applied FSSH, mSDM, ID-A and the 2023 revised version
of DISH

recipes:This folder contains the pre-defined recipes for the different TSH schemes. Don't modify
this folder, just leave in the same directory where the NA-MD runs are conducted.

To start the calculations, simply run the NAMD_*py file with Python or call it with
the submit (submit_template.slm) file.

After finishing the NA-MD runs, the script `plot_populations.py` is used to plot the excited 
states' evolution with the different TSH methods.

**key_outputs**

The different `TiO2_*` directories contain 6 folders (each one corresponding to a step1 methodology +
a step2 functional). Each of these 6 folders contains a compressed file gathering the  **icond** folders 
which contain the evolution (per each initial condition) of first excited state (S1) per each system 
+ methodology + trajectory surface hopping (TSH) scheme. 

To unpack:
`tar -xjf (name of the .bz2 compressed file)`


We've also added in the `plots` directory the .png files with the S0 population evolution for all clusters and methodologies.
(the output of properly running the `plot_populations.py` script).



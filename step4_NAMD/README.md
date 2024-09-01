# Project_TiO2_water_methods_assessment
scripts and selected outputs from performing the nonadiabatic molecular dynamics (NA-MD) runs

**scripts** 

Again, the inputs are part of the outcome from the previous steps. No "inputs" folder here.

`NAMD_*.py` the script for starting the NA-MD using one trajectory surface hoping
(TSH) method. In our case, we have applied FSSH, mSDM, ID-A and the 2023 revised version
of DISH

**recipes** 
This folder contains the pre-defined recipes for the different TSH schemes. Don't modify
this folder, just leave in the same directory where the NA-MD runs are conducted.

To start the calculations, simply run the NAMD_*py file with Python or call it with
the submit (submit_template.slm) file.

After finishing the NA-MD runs, the script `plot_populations.py` is used to plot the excited 
states' evolution with the different TSH methods.

**key_outputs**

The outputs are large and heavy as to include them here. We add the PNG files
with the S0 population evolution for all clusters and methodologies.



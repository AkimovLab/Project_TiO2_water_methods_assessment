# Project_TiO2_water_methods_assessment
scripts and selected outputs from computing the nonadiabatic couplings (NACs) between pairs of TD-DFT states.

**scripts**:

The inputs in this case are part of the outcome from step2, so the required files are invoked 
in the `step3_NACs.py` file (4th and 5th line). It is not needed to move such files to this directory. 
There is not a "input" folder in this case.


We add the scripts `ExciEnergies_visualization.py` and `NACs_visualization.py` that
(after conducting the NACs calculation) generate the plots for, respectively, TD-DFT states' 
energies evolutions and the average NACs among pairs of states.

**key_outputs**:

The outputs from this step (the NACs) are heavy files so are not included here. They 
are easy to obtain by running the step3_NACs.py file with Python or calling it with 
the proper submit (`submit_template.sh`) file. We have included a PNG file with the
trajectory-averaged excitation energies and NACs for all branches.



import os
from libra_py.workflows.nbra import step3

params_mb_sd = {
          'lowest_orbital': 48-16, 'highest_orbital': 49+17, 'num_occ_states': 16, 'num_unocc_states': 16,
          'isUKS': 0, 'number_of_states': 5, 'tolerance': 0.01, 'verbosity': 0, 'use_multiprocessing': False, 'nprocs': 12,
          'is_many_body': True, 'time_step': 1.0, 'es_software': 'cp2k',
          'path_to_npz_files': os.getcwd()+'/../../../../step2_Exci/AIMD/pbe/morelevels/res',
          'logfile_directory': os.getcwd()+'/../../../../step2_Exci/AIMD/pbe/morelevels/all_logfiles/',
          'path_to_save_sd_Hvibs': os.getcwd()+'/res-mb-sd-DFT',
          'outdir': os.getcwd()+'/res-mb-sd-DFT', 'start_time': 1000, 'finish_time': 4000, 'sorting_type': 'identity',
         }

step3.run_step3_sd_nacs_libint(params_mb_sd)


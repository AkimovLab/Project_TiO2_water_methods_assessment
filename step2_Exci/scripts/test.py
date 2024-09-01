import libra_py.packages.cp2k.methods as CP2K_methods

params = {"logfile_name": "step_1.log", "tolerance": 0.01, "number_of_states": 10}

min_ = 1000
max_ = 0
min_orb=[]
max_orb=[]
for i in range(0, 3000):
   print('-------------------------------', i, '-----------------------------')
   params.update({"logfile_name":F"all_logfiles/step_{i}.log"});
   tmp = CP2K_methods.read_cp2k_tddfpt_log_file(params)
   print(tmp)
   min_orb.append(tmp[1][0][0][0])
   max_orb.append(tmp[1][0][0][1])
   if (int(tmp[0][0])) < 1 or (tmp[1][0][0][0]) < 58 or (tmp[1][0][0][1]) > 174:
      print('Flago not found', i)
   for j in range(len(tmp[1])):
       for k in range(len(tmp[1][j])):
#           print(tmp[1][j][k][0])
           min_ = min(tmp[1][j][k][0], min_)
           max_ = max(tmp[1][j][k][1], max_)

   if len(tmp[0]) != 5:
            print("not one")

print('Min index is:', min_)
print('Max index is:', max_)
 

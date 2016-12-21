import subprocess
import os 

subprocess.call("scp work@180.76.155.167:/home/work/data_hub/bidmax_data/ip_location.dat /home/work/run_env/scripts/data/", shell=True)
filesize = os.path.getsize("/home/work/run_env/scripts/data/ip_location.dat");
if filesize < 1024 * 1024:
    print "abnormal ip loc file"
else:
    subprocess.call("cp /home/work/run_env/scripts/data/ip_location.dat /home/work/run_env/DEPLOY/BidMax/Router/data/", shell = True)
    #subprocess.call("cp /home/work/run_env/scripts/data/ip_location.dat /home/work/run_env/scripts/data/ip_location.dat_cp", shell = True)


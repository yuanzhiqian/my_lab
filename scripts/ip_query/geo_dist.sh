log="/home/work/run_env/DEPLOY/BidMax/Logger/log/pv.log" 

grep cooxian $log | cut -d'"' -f18 > ip_data 

total_num=`wc -l ip_data | cut -d' ' -f1`

echo "total: $total_num" > result 
python ./main.py | cut -d'	' -f1 | sort -nr | uniq -c | sort -nr | awk -F " " '{print $(NF-1) " " $(NF-1)/'$total_num'*100 "%" " " $NF}' >> result

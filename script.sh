curl "https://www.marketwatch.com/investing/index/spx" > /home/ubuntu/Projet/Project/Generated_data/SP500.html
curl "https://www.marketwatch.com/investing/index/ndx" > /home/ubuntu/Projet/Project/Generated_data/NASDAQ.html
Value1=$(cat /home/ubuntu/Projet/Project/Generated_data/SP500.html | grep -oP '(?<=<span class="value">)\w+,\w+.\w+'| sed 's/,//g')
Value2=$(cat /home/ubuntu/Projet/Project/Generated_data/NASDAQ.html | grep -oP '(?<=<span class="value">)\w+,\w+.\w+'| sed 's/,//g')
Date=$(date +%Y-%m-%d-%H:%M)
echo "$Date;$Value1;$Value2" >> /home/ubuntu/Projet/Project/Generated_data/data.csv
git add .
git commit -m " Actualisation des données - $(date -d "now" +"%Y-%m-%d à %Hh%M")" 

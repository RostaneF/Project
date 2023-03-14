curl "https://www.marketwatch.com/investing/index/spx" > /home/rostane/Projet_final/Project/Generated_data/SP500.html
curl "https://www.marketwatch.com/investing/index/ndx" > /home/rostane/Projet_final/Project/Generated_data/NASDAQ.html
Value1=$(cat /home/rostane/Projet_final/Project/Generated_data/SP500.html | grep -oP '(?<=<span class="value">)\w+,\w+.\w+'| sed 's/,//g')
Value2=$(cat /home/rostane/Projet_final/Project/Generated_data/NASDAQ.html | grep -oP '(?<=<span class="value">)\w+,\w+.\w+'| sed 's/,//g')
Date=$(date +%Y-%m-%d-%H:%M)
echo "$Date;$Value1;$Value2" >> /home/rostane/Projet_final/Project/Generated_data/data.csv
git add .
git commit -m "$(date -d "now" +"%Y-%m-%d:%Hh%M") : Actualisation des données" 

curl "https://www.marketwatch.com/investing/index/spx" > /home/rostane/Projet_final/Project/SP500.html
Value=$(cat /home/rostane/Projet_final/Project/SP500.html | grep -oP '(?<=<span class="value">)\w+,\w+.\w+'| sed 's/,//g')
Date=$(date +%Y-%m-%d-%H:%M)
echo "$Date;$Value" >> data.csv
git add .
git commit -m "$(date -d "now" +"%Y-%m-%d:%Hh%M") : Actualisation des données" 
git push

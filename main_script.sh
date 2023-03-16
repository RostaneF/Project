curl -s "https://www.marketwatch.com/investing/index/spx" > /home/ubuntu/Projet/Project/Generated_data/SP500.html
curl -s "https://www.marketwatch.com/investing/index/ndx" > /home/ubuntu/Projet/Project/Generated_data/NASDAQ.html
Value1=$(cat /home/ubuntu/Projet/Project/Generated_data/SP500.html | grep -oP '(?<="@context":"http://schema.org/","@type":"Intangible/FinancialQuote","name":"S&P 500 Index","tickerSymbol":"SPX","exchange":"S&P US","price":")\w+,\w+.\w+' | sed "s/,//")
Value2=$(cat /home/ubuntu/Projet/Project/Generated_data/NASDAQ.html | grep -oP '(?<="price":")[^"]*' | sed "s/,//")
Date=$(date +%Y-%m-%d-%H-%M)
echo "$Date;$Value1;$Value2" >> /home/ubuntu/Projet/Project/Generated_data/data.csv
git add .
git commit -m "Actualisation des données"

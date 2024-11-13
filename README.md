This project attempts to assign credibility ratings to users on Reddits investing forums. You can use the "tags_NOV_12_24" along with the Reddit Enhancement Suite to tag users. A single * means at least 60% of their stocks have underperformed SPY since being mentioned, ** for 70%, *** for 80% and **** for 90%. 

I compared stock picks made by Reddit users to the performance of the S&P 500 (represented by SPY). For each stock, I looked at its performance from the earliest time the user mentioned it and recorded whether it outperformed SPY (marked as TRUE) or underperformed (marked as FALSE). If at least half of a redditors picks outperformed SPY, they are included in the table below.  94k Users were analyzed; 47k mentioned at least one ticker, and 14k mentioned 5 or more. 

Of the 14k that mentioned 5+ tickers, only 2586 beat spy more than half of the time. Despite this, 89.36% of their picks reached a higher price after being mentioned.

![fifty](https://github.com/user-attachments/assets/0aaf7ee9-18b8-44e5-9f5b-993931b3b28b)

Sixty Percent:

![sixty](https://github.com/user-attachments/assets/248cf9b0-008e-4e2a-a2e4-33237cdb535e)

Sixty Five Percent:

![sixtyfive](https://github.com/user-attachments/assets/ddc1f1a6-a298-480f-81ef-6cd45c4ebce3)

If you want to recreate this data set at home, use the create_all() function in csvFunctions.py to create a local database of the 7000 Tickers used in this project. This takes ~4 minutes with 10 threads. After that, enter your API info into the config file. If there are JSON errors, try using values_as_keys(alias.json).

~

To do~ 
1. Refine Alias list
2. Convert stock_data to duckDB
3. Incorporate a LLM into evaluating the users sentiment on the mentioned stocks

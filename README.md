1. getUserTickers("example_user", 10)
   
    Fetches and parses a redditors submission and comments. The second parameter specifies the search depth. Returns the earliest mentioned date of each ticker. eg

   ('FORD', '07/18/2022'),\
   ("KO", '02/27/2023'),\
   ("AAPL", '06/29/2019'),\
   ("GME", '04/01/2021')


3. bench_vs_user("SPY", data)

    Compares the performance of the ticker relative to SPY since the date of mention, and since the tickers inception. Returns a list:

    Ticker Name, Date Mentioned, SPY > Ticker since mention?, Date of inception, SPY > Ticker since Inception?, 'Price Inc After Mention'
   
    ['FORD', 'Mention: 07/18/2022', True, 'Inception: 11/17/1994', True, 'Price Inc After Mention', True]\
    ['KO', 'Mention: 02/27/2023', True, 'Inception: 01/29/1993', True, 'Price Inc After Mention', True]\
    ['AAPL', 'Mention: 06/28/2019', False, 'Inception: 01/29/1993', False, 'Price Inc After Mention', True]\
    ['GME', 'Mention: 04/01/2021', True, 'Inception: 02/13/2002', False, 'Price Inc After Mention', True]


94k Users were analyzed, 47k mentioned at least 1 stock, 14k mentioned at least 5 stocks. ~90% of stocks mentioned hit a new high since mention. Very few, if any, users were able to consistently pick stocks that outperformed spy. See all_data.csv.

Results:

<img src="https://github.com/user-attachments/assets/0aaf7ee9-18b8-44e5-9f5b-993931b3b28b" alt="Alt Text" width="400" height="300">

Sixty Percent:

<img src="https://github.com/user-attachments/assets/248cf9b0-008e-4e2a-a2e4-33237cdb535e" alt="Alt Text" width="400" height="300">

Sixty Five Percent:

<img src="https://github.com/user-attachments/assets/ddc1f1a6-a298-480f-81ef-6cd45c4ebce3" alt="Alt Text" width="400" height="300">


If you want to recreate this data, use the create_all() function in csvFunctions.py to create a local database of the 7000 Tickers used in this project. This takes ~4 minutes with 10 threads. After that, enter your API info into the config file. If there are JSON errors, try using values_as_keys(alias.json). The 

~

To do~ 
1. Refine Alias list
2. Convert stock_data to duckDB
3. Incorporate a llama to evaluate the users sentiment on the mentioned stocks

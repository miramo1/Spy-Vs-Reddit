This project compares redditors stock picks to SPY. A credibility rating is assigned to them based on the performance of their picks. See "tags_NOV_12_24.json" for RES compatible list.

1. data = getUserTickers("example_user", 10)

    eg, [('F', '07/18/2024'), ("KO", '02/29/2024'), ("AMC", '06/29/2022')]

2. bench_vs_user("SPY", data)

    ticker, date of mention, spy>ticker?, date of inception, spy>ticker?, Price Inc After Mention, bool
   
    ['F', 'Mention: 07/18/2024', True, 'Inception: 01/29/1993', True, 'Price Inc After Mention', False]
    
    ['KO', 'Mention: 02/29/2024', True, 'Inception: 01/29/1993', True, 'Price Inc After Mention', True] 
    
    ['AMC', 'Mention: 06/29/2022', True, 'Inception: 12/18/2013', True, 'Price Inc After Mention', True]


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

<h1>SPY VS. Reddit</h1>

<h3>Process: Scrape redditor profiles for stock picks. Stock performance is compared to SPY according to redditors earliest mention date.</h3>

106k Reddit profiles analyzed, of which 16.2k mentioned at least 5 stocks.

3200 of them were able to beat SPY at least 50% of the time. 

Price Increase Post Mention, PIPM, checks if the stock hit a higher price at least once after the date of mention. 

<h3>Users that beat SPY at least 50.0% of the time</h3>
<pre>
+---------+-------+----------+-------+-------+
| Tickers | Users | Beat SPY | %     | PIPM  |
+---------+-------+----------+-------+-------+
| 5       | 16266 | 3182     | 19.56 | 89.65 |
| 10      | 8153  | 1445     | 17.72 | 89.96 |
| 15      | 4669  | 739      | 15.83 | 90.14 |
| 20      | 2847  | 411      | 14.44 | 90.34 |
| 25      | 1803  | 217      | 12.04 | 90.61 |
| 30      | 1182  | 122      | 10.32 | 90.68 |
| 35      | 815   | 82       | 10.06 | 90.7  |
| 40      | 564   | 51       | 9.04  | 90.68 |
| 45      | 401   | 29       | 7.23  | 90.88 |
| 50      | 296   | 24       | 8.11  | 91.01 |
+---------+-------+----------+-------+-------+   
</pre>


<h3>55%</h3>
<pre>
+---------+-------+----------+-------+-------+
| Tickers | Users | Beat SPY | %     | PIPM  |
+---------+-------+----------+-------+-------+
| 5       | 16266 | 2692     | 16.55 | 89.65 |
| 10      | 8153  | 955      | 11.71 | 89.96 |
| 15      | 4669  | 488      | 10.45 | 90.14 |
| 20      | 2847  | 238      | 8.36  | 90.34 |
| 25      | 1803  | 116      | 6.43  | 90.61 |
| 30      | 1182  | 61       | 5.16  | 90.68 |
| 35      | 815   | 40       | 4.91  | 90.7  |
| 40      | 564   | 24       | 4.26  | 90.68 |
| 45      | 401   | 11       | 2.74  | 90.88 |
| 50      | 296   | 8        | 2.7   | 91.01 |
+---------+-------+----------+-------+-------+   
</pre>

<h3>60%</h3>
<pre>
+---------+-------+----------+------+-------+
| Tickers | Users | Beat SPY | %    | PIPM  |
+---------+-------+----------+------+-------+
| 5       | 16266 | 1609     | 9.89 | 89.65 |
| 10      | 8153  | 533      | 6.54 | 89.96 |
| 15      | 4669  | 237      | 5.08 | 90.14 |
| 20      | 2847  | 109      | 3.83 | 90.34 |
| 25      | 1803  | 53       | 2.94 | 90.61 |
| 30      | 1182  | 30       | 2.54 | 90.68 |
| 35      | 815   | 15       | 1.84 | 90.7  |
| 40      | 564   | 11       | 1.95 | 90.68 |
| 45      | 401   | 3        | 0.75 | 90.88 |
| 50      | 296   | 1        | 0.34 | 91.01 |
+---------+-------+----------+------+-------+</pre>

<h3>65%</h3>
<pre>
+---------+-------+----------+------+-------+
| Tickers | Users | Beat SPY | %    | PIPM  |
+---------+-------+----------+------+-------+
| 5       | 16266 | 1157     | 7.11 | 89.65 |
| 10      | 8153  | 270      | 3.31 | 89.96 |
| 15      | 4669  | 103      | 2.21 | 90.14 |
| 20      | 2847  | 56       | 1.97 | 90.34 |
| 25      | 1803  | 18       | 1.0  | 90.61 |
| 30      | 1182  | 9        | 0.76 | 90.68 |
| 35      | 815   | 3        | 0.37 | 90.7  |
| 40      | 564   | 1        | 0.18 | 90.68 |
| 45      | 401   | 0        | 0.0  | 90.88 |
| 50      | 296   | 0        | 0.0  | 91.01 |
+---------+-------+----------+------+-------+</pre>

<h3>Conclusion: SPY overwhelmingly defeats the majority of redditors stock picks in binary terms. Effect is most pronounced in the short-squeeze and penny stock focused subreddits, even when accounting for actual returns.</h3>

See Results folder for data. No favorites omits ['GME', 'TSLA', 'AAPL', 'GOOGL', 'AMZN', 'NVDA', 'AMC', 'V', 'META', 'MSFT']. No spy omits any stock already included in SPY.

<h1>CODE</h1>

1. Alias.json is converted into a Trie in order to parse out text. eg.
   
   <pre>"MSFT":  [
              "$MSFT",
              "MICRO SOFT",
              "MICROSOFT",
              "MSFT",
              "WINDOWS"
            ]</pre>
          
2. <h3>getUserTickers("example_user", 10)</h3>
   
   Fetches and parses a redditors submission and comments. The second parameter specifies the search depth. Returns the earliest mentioned date of each ticker. eg
   
   <pre>[('FORD', '07/18/2022'),
   ("KO", '02/27/2023'),
   ("AAPL", '06/29/2019'),
   ("GME", '04/01/2021')]
   </pre>


3. <h3>bench_vs_user("SPY", data)</h3>

    Compares the performance of the ticker relative to SPY since the date of mention, and since the tickers inception. Returns a list:

    Ticker Name, Date Mentioned, SPY > Ticker since mention?, Date of inception, SPY > Ticker since Inception?, 'Price Inc After Mention'

   <pre>
    (['FORD', 'Mention: 07/18/2022', True, 'Inception: 11/17/1994', True, 'Price Inc After Mention', True],
    ['KO', 'Mention: 02/27/2023', True, 'Inception: 01/29/1993', True, 'Price Inc After Mention', True],
    ['AAPL', 'Mention: 06/28/2019', False, 'Inception: 01/29/1993', False, 'Price Inc After Mention', True],
    ['GME', 'Mention: 04/01/2021', True, 'Inception: 02/13/2002', False, 'Price Inc After Mention', True])</pre>


To do~ 
1. Refine Alias list
2. Convert stock_data to duckDB
3. Incorporate a llama to evaluate the users sentiment on the mentioned stocks
4. Yahoo API, as of 11/18/24, has hidden rate limits. Figure out way to update data with async.
5. Get exact returns for redditors. Allocate equal weight to each mentioned ticker? Investigate further.

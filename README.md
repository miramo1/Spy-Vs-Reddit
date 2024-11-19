<div id="user-content-toc">
  <ul align="center" style="list-style: none;">
    <summary>
      <h1>SPY VS. Reddit</h1>
    </summary>
  </ul>
</div>

<h4>Process: Scrape redditor profiles for stock picks. Stock performance is compared to SPY according to redditors earliest mention date.</h4>

106k Reddit profiles analyzed, 57k mentioned at least 1 stock, 16k mentioned at least 5 stocks.

Of the 16k, 3.2k were able to beat SPY at least 50% of the time.

Price Increase Post Mention, PIPM, checks if the stock hit a higher price at least once after the date of mention. 

<h4>Users that beat SPY at least 50% of the time</h4>
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


<h4>55%</h4>
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

<h4>60%</h4>
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

<h4>65%</h4>
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

* <h1>OMITING FAVORITES</h1>

nofavs.csv excludes top 10 most mentioned - ['GME', 'TSLA', 'AAPL', 'GOOGL', 'AMZN', 'NVDA', 'AMC', 'V', 'META', 'MSFT']. nospy.csv omits any stock already included in SPY. Returns degrade substantially when favorites are omitted. See Results folder for data. 

<h4>Without Favorites, Users that beat SPY at least 50% of the time</h4>
<pre>
+---------+-------+----------+-------+-------+
| Tickers | Users | Beat SPY | %     | PIPM  |
+---------+-------+----------+-------+-------+
| 5       | 12108 | 1737     | 14.35 | 88.25 |
| 10      | 5653  | 702      | 12.42 | 88.7  |
| 15      | 3103  | 351      | 11.31 | 89.14 |
| 20      | 1849  | 180      | 9.73  | 89.48 |
| 25      | 1157  | 96       | 8.3   | 89.79 |
| 30      | 769   | 66       | 8.58  | 89.97 |
| 35      | 528   | 41       | 7.77  | 90.03 |
| 40      | 374   | 28       | 7.49  | 90.32 |
| 45      | 282   | 19       | 6.74  | 90.64 |
| 50      | 214   | 16       | 7.48  | 90.75 |
+---------+-------+----------+-------+-------+</pre>

<h4>Without SPY, Users that beat SPY at least 50% of the time</h4>
<pre>
+---------+-------+----------+-------+-------+
| Tickers | Users | Beat SPY | %     | PIPM  |
+---------+-------+----------+-------+-------+
| 5       | 7512  | 1062     | 14.14 | 84.44 |
| 10      | 2559  | 298      | 11.65 | 84.31 |
| 15      | 1121  | 104      | 9.28  | 84.25 |
| 20      | 551   | 49       | 8.89  | 84.38 |
| 25      | 306   | 20       | 6.54  | 84.43 |
| 30      | 180   | 10       | 5.56  | 84.13 |
| 35      | 122   | 8        | 6.56  | 83.83 |
| 40      | 82    | 5        | 6.1   | 83.47 |
| 45      | 66    | 5        | 7.58  | 83.36 |
| 50      | 52    | 3        | 5.77  | 84.03 |
+---------+-------+----------+-------+-------+</pre>

* <h1>CODE</h1>

1. <h4>Alias.json is converted into a Trie in order to parse out text.</h4> 

   eg.
   <pre>"MSFT":  [
              "$MSFT",
              "MICRO SOFT",
              "MICROSOFT",
              "MSFT",
              "WINDOWS"
            ]</pre>
          
2. <h4>getUserTickers("example_user", 10)</h4>
   
   Fetches and parses a redditors submission and comments. The second parameter specifies the search depth. Returns the earliest mentioned date of each ticker.
   
   eg.
   <pre>[('FORD', '07/18/2022'),
   ("KO", '02/27/2023'),
   ("AAPL", '06/29/2019',
   ("GME", '04/01/2021')]
   </pre>


4. <h4>bench_vs_user("SPY", data)</h4>

   Compares the performance of the ticker relative to SPY since the date of mention, and since the tickers inception. Returns a list:

   <pre>
   [0] - [Ticker, 
   [1] - Date Mentioned, 
   [2] - SPY > Ticker since mention?, 
   [3] - Date of inception, 
   [4] - SPY > Ticker since Inception?, 
   [5] - Price Inc After Mention?,
   [6] - True/False]</pre>
   
   eg.
   <pre>
    [['FORD', 'Mention: 07/18/2022', True, 'Inception: 11/17/1994', True, 'Price Inc After Mention', True],
    ['KO', 'Mention: 02/27/2023', True, 'Inception: 01/29/1993', True, 'Price Inc After Mention', True],
    ['AAPL', 'Mention: 06/28/2019', False, 'Inception: 01/29/1993', False, 'Price Inc After Mention', True],
    ['GME', 'Mention: 04/01/2021', True, 'Inception: 02/13/2002', False, 'Price Inc After Mention', True]]</pre>

* <h1>DISCUSSION</h1>

1. Project does not take into account sentiment and context when scraping tickers. "I think SO-SO Corp is terrible, but I think THIS-AND-THAT Inc. is a gem!" In this case, both tickers would be picked up by the Trie. Although negative sentiment mentions are rare, and most likely don't have a tangible effect on the data, their existence should still be acknowledged.
 
      <code>Proposed remedy - Incorporate LLM to interpret sentiment and context in order to omit negative sentiment tickers. Might need new graphics card?</code>

2. This project relies on the Alias.json to match words and phrases to their respective tickers. While the list has been reasonably well refined, false positives do occur from time to time. This is most promiment when factoring in non-english users and non-english subreddits.

      <code>Proposed remedy - Further refine Alias.json, or omit problematic subreddits/languages altogether.</code>

3. The data base of this project relies on YAHOO FINANCE, and by extension, the yfinance module. As of this week, 11/18/2024, YAHOO FINANCE seems to have silently implemented limits on API calls. The current itteration of the database includes about ~7000 CSVs which must be updated daily. The updating process seems to hit the API call limit around 2000-2500. Furthermore, the nature of CSVs makes them cumbersome and slow to work with.
   
      <code>Temporary remedy - Keep SPY updated daily. When comparing SPY to the users TICKER, trim the length of SPY to match the length of TICKER. At worst, this results the omission of a day or two of returns. Overall inconsequential, but nonetheless very annoying.</code>
      
      <code>Proposed remedy 1 - Update the database in a staggered/asynch formation throughout the day to avoid API call limits. Look into AlphaVantage, or consider paying for data. Reach out to testfol.io creator for second opinion.</code>

      <code>Proposed remedy 2 - Convert CSV database to SQL for faster access and compatibility with multiprocess. Duck DB looks promising.</code>

4. The exact returns generated by each redditor isn't calculated. It's plausible, though tenuous, that a redditor may pick one or two stocks that generate enough alpha to create net profit despite losses on all other stock picks. 2.4% of firms generated the bulk of market returns, Bessembinder et al. Took a preliminary look into this, specifically in the pennystock and short-squeeze focused subreddits. These redditors, in aggregate, were consistently and overwhelmingly net negative even when accounting for squeezes. Results to be posted later.

   <code>Proposed remedy - Incorporate exact returns into bench_vs_user function. Allocate one single dollar to each stock starting at its earliest mention? Reconcile when redditor choose to "yolo" on a stock.</code>


<div id="user-content-toc">
  <ul align="center" style="list-style: none;">
    <summary>
      <h1>Always bet on SPY.</h1>
    </summary>
  </ul>
</div>

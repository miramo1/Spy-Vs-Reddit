import pandas as pd
import logging, timeFunctions

logger = logging.getLogger('yfinance')
logger.disabled = True
logger.propagate = False
stock_folder = r""

def get_ticker_data(ticker) -> list | list | list | list:
    # date, close, dividends
    df = pd.read_csv(f"{stock_folder}/{ticker}.csv")
    
    pct_change = df.close.pct_change(fill_method=None)+1
    pct_change.iloc[0] = 1
    pct_change = pct_change.tolist()

    dates = df.date.tolist()

    return pct_change, dates, df.close.tolist()

def chal_ticker_returns(ticker, mention_date) -> list | list | list:

    df = pd.read_csv(f"{stock_folder}/{ticker}.csv")
    
    pct_change = df.close.pct_change(fill_method=None)+1
    pct_change.iloc[0] = 1
    pct_change = pct_change.tolist()

    div = df.dividends.tolist()
    dates = df.date.tolist()

    if mention_date not in dates:
        mention_date = timeFunctions.closest_date(mention_date, dates)
        adj_index = dates.index(mention_date)

        pct_change = pct_change[adj_index:]
        dates = dates[adj_index:]
        div = div[adj_index:]

    return pct_change, dates, div

def trim_data(close, date, chal_inception_date) -> list | list | list:

    trimmed_start_idx = date.index(chal_inception_date)
    return close[trimmed_start_idx:], date[trimmed_start_idx:]

def newHighAfterMention(ticker, date_mention) -> bool:
    df = pd.read_csv(f"{stock_folder}/{ticker}.csv")
    close, dates = df.close.tolist(), df.date.tolist()
    offset = dates.index(date_mention)
    close = close[offset:]
    close_on_mention_date = close[0]
    return any(price > close_on_mention_date for price in close[1:])

if __name__ == "__main__":
    mylist = [14, 12, 11]
    price = 15
    print(newHighAfterMention(price, mylist))

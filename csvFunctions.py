from aliasFunctions import add_alias, values_as_keys, tickers_as_keys
from timeFunctions import delisted_checker
import json, os, multiprocessing, time
import pandas as pd
import yfinance as yf

folder_path = r""
stock_data = os.listdir(folder_path)

json_file = r""
values_as_keys(json_file)
known_tickers = sorted(set(json.load(open(json_file)).values()))

def clean_corp_name(corp_name):
    omit = ['-', ',' 'ASSOCIATION', 'BRANDS', 'CO/THE', 'COMMON', 'COMMUNICATIONS', 'COMPANIES', 'COMPANY', 'CORP.', 'CORPS', 'CORP','ENTERTAINMENT', 'GROUP', 'HOLDING', 'HOLDINGS', 'INC', 'INC.', 'INCORPORATED', 'INDUSTRIES', 'INLT.HOLDINGS', 'INSURANCE', 'INTERNATIONAL', 'INVESTMENT','LIMITED', 'LTD', 'LTD.', 'PARTNERS', 'PLC', 'SERVICES', 'SCIENCES', 'SOLUTIONS', 'SYSTEMS', 'TECHNOLOGIES', "TRUST"]

    name = corp_name.upper().split(" ")

    if len(name) > 3:
        name = name[:3]

    name = [x for x in name if x not in omit]
    name = ' '.join(name)
    return name

def create_single_csv(ticker: str):
    name = ticker.upper()
    known = json.load(open(json_file)).values()
    if name in known:
        print(f"{name} already in database")
        return
    try:
        # try to get the tickers data, if not, assume delisted
        data = yf.Ticker(name).history(period="max")
        dates, dividends, close = data.index, data.Dividends, data.Close
        dates_formatted = [day.strftime('%m-%d-%Y').replace("-", "/") for day in dates]

        if delisted_checker(dates[-1]):
            print(f"{ticker} has not traded in the last 5 days; writing to delisted.\n")
            with_ticker = "$"+ticker
            add_alias(json_file, "DELISTED", ticker)
            add_alias(json_file, "DELISTED", with_ticker)
            return

        # adjusted the dividends to be a percent of the price on that day, instead of their raw value.
        # eg $0.25 dividend on $15.00 = .01667. we do this because our closing will be converted
        # into pandas pct_change when comparing equities later. 

        divs_adjusted = []
        for i in range(len(dates)):
            if dividends.iloc[i] != 0:
                percent = dividends.iloc[i]/close.iloc[i]
                divs_adjusted.append(percent)
            else:
                divs_adjusted.append(0)

        ticker_data = pd.DataFrame({'date': dates_formatted, 'close': close, "dividends": divs_adjusted})
        ticker_data.to_csv(f'{folder_path}/{ticker}.csv', index=False)
        print(f"{ticker} CSV created, last traded on {dates_formatted[-1]}")

    except:
        print(f"{ticker} not on yfinance")
        values_as_keys(json_file)
        print()
        return

    ### add to alias
    try:
        with_ticker = "$"+ticker
        corp_name = clean_corp_name(data.info["shortName"]).replace(",", "")
        add_alias(json_file, ticker, with_ticker)
        add_alias(json_file, ticker, corp_name)
        print(f"{ticker} ticker added, {corp_name} alias")

    except:
        with_ticker = "$"+ticker
        add_alias(json_file, ticker, with_ticker)
        print(f"{ticker} ticker added to alias")

    values_as_keys(json_file)

    print()

def create_multi(tickers: list):
    for ticker in tickers:
        if ticker == "DELISTED":
            continue
        else:
        # try to get the tickers data, if not, assume delisted
            data = yf.Ticker(ticker).history(period="max")
            dates, close = data.index, data.Close
            dates_formatted = [day.strftime('%m-%d-%Y').replace("-", "/") for day in dates]
            ticker_data = pd.DataFrame({'date': dates_formatted, 'close': close})
            ticker_data.to_csv(f'{folder_path}/{ticker}.csv', index=False)

def create_all():
    print(f"Creating all {len(known_tickers)} CSVs, ETA 06:00 on 7 threads")
    start_time = time.time()
    worker_list = []
    for i in range(0,7000,1000):
        if i == 7000:
            worker = multiprocessing.Process(target=create_multi, args=(known_tickers[i:],))
        else:
            worker = multiprocessing.Process(target=create_multi, args=(known_tickers[i:i+1000],))
        worker_list.append(worker)
        worker.start()

    for worker in worker_list:
        worker.join()

    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    elapsed_time_formatted = f"{minutes:02}:{seconds:02}"
    values_as_keys(json_file)
    print(f"Fin. Actual time: {elapsed_time_formatted}")

if __name__ == "__main__":
    create_all()

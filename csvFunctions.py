from aliasFunctions import add_alias, values_as_keys, tickers_as_keys
from timeFunctions import delisted_checker
import json, os, multiprocessing, time
import pandas as pd
import yfinance as yf

folder_path = r"stock_data/"
stock_data = os.listdir(folder_path)

json_file = r"alias.json"
tickers_as_keys(json_file)
known_tickers = sorted(json.load(open(json_file)).keys())
delisted = sorted(json.load(open(json_file))["DELISTED"])

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

def create_multi(tickers: list, json_file):
    for ticker in tickers:
        if ticker == "DELISTED":
            continue
        try:
            info = yf.Ticker(ticker)
            # try to get the tickers data, if not, assume delisted
            data = yf.Ticker(ticker).history(period="max")
            dates, dividends, close = data.index, data.Dividends, data.Close
            dates_formatted = [day.strftime('%m-%d-%Y').replace("-", "/") for day in dates]

            # adjusted the dividends to be a percent of the price on that day, instead of their raw value.
            # eg $0.25 dividend on $15.00 = .01667. we do this because our closing will be converted
            # into pandas pct_change when comparing equities later. 
            divs_adjusted = []
            for i in range(len(dates)):
                if dividends.iloc[i] != 0:
                    percent = dividends.iloc[i]/close.iloc[i]
                    # print(dividends[i], close[i], percent, dates[i])
                    divs_adjusted.append(percent)
                else:
                    divs_adjusted.append(0)

            ticker_data = pd.DataFrame({'date': dates_formatted, 'close': close, "dividends": divs_adjusted})
            ticker_data.to_csv(f'{folder_path}/{ticker}.csv', index=False)
            # print(f"{ticker} CSV created, last traded on {dates_formatted[-1]}")

        except:
            # print(f"{ticker} not on yfinance")
            continue

        ### add to alias

def create_all():
    print(f"Creating all {len(known_tickers)} CSVs, ETA 04:00 on 10 threads")
    start_time = time.time()
    worker_list = []
    for i in range(0,11001,1000):
        if i == 10000:
            worker = multiprocessing.Process(target=create_multi, args=(known_tickers[i:], json_file))
        else:
            worker = multiprocessing.Process(target=create_multi, args=(known_tickers[i:i+1000], json_file))
        worker_list.append(worker)
        worker.start()

    for worker in worker_list:
        worker.join()

    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    elapsed_time_formatted = f"{minutes:02}:{seconds:02}"
    print(f"Fin. Actual time: {elapsed_time_formatted}")

def update_stock_data(stock_data: list):

    for stock in stock_data:
        if stock in delisted:
            continue
        else:
            try:
                current_stock_data = pd.read_csv(f"{folder_path}/{stock}.csv")
            except:
                pass

            cur_stock_last_updated = current_stock_data.date.iloc[-1]

            # get new data
            stock_data = yf.Ticker(stock).history(period="5d")
            # format date to match csv
            new_data_dates = [day.strftime('%m-%d-%Y').replace("-", "/") for day in stock_data.index.tolist()]
            
            try:
                if cur_stock_last_updated == new_data_dates[-1]:
                    continue
                else:
                    starting_index = new_data_dates.index(cur_stock_last_updated) + 1
                    new_close = stock_data.Close.tolist()[starting_index:]
                    new_dates = new_data_dates[starting_index:]
                    new_dividend = stock_data.Dividends.tolist()[starting_index:]

                    divs_adjusted = []
                    for i in range(len(new_dates)):
                        if new_dividend[i] != 0:
                            percent = new_dividend[i]/close[i]
                            divs_adjusted.append(round(percent,4))
                        else:
                            divs_adjusted.append(0)

                    with open(f"{folder_path}/{stock}.csv", 'a') as file:
                        for date, close, div in zip(new_dates, new_close, divs_adjusted):
                            formatted_data = f"{date},{close},{div}\n"
                            file.write(formatted_data)
            except:
                continue

def update_all():
    # 00:55 @ 10000
    print(f"Updating {len(known_tickers)} CSVs, ETA 01:10 on 10 threads")
    start_time = time.time()
    worker_list = []
    for i in range(0,11001,1000):
        if i == 10000:
            worker = multiprocessing.Process(target=update_stock_data, args=(known_tickers[i:],))
        else:
            worker = multiprocessing.Process(target=update_stock_data, args=(known_tickers[i:i+1000],))
        worker_list.append(worker)
        worker.start()

    for worker in worker_list:
        worker.join()

    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    elapsed_time_formatted = f"{minutes:02}:{seconds:02}"

    print(f"Fin. Actual time: {elapsed_time_formatted}")

def check_broken_update(stock_data: list):

    for stock in stock_data:
        if stock in delisted:
            continue
        try:
            current_stock_data = pd.read_csv(f"stock_data/{stock}.csv")
            pct_change = current_stock_data.close.pct_change(fill_method=None)+1
            pct_change.iloc[0] = 1
            pct_change = pct_change.tolist()

            div = current_stock_data.dividends.tolist()
            dates = current_stock_data.date.tolist()

        except:
            div = type(div)
            dates = type(dates)
            pct_change = type(pct_change)
            close = type(current_stock_data.tolist())
            print(stock, div, dates, pct_change, close)

def check_all():
    # 00:55 @ 10000
    print(f"Checking {len(known_tickers)} CSVs for broken update, ETA 01:00")
    start_time = time.time()
    worker_list = []
    for i in range(0,11001,1000):
        if i == 10000:
            worker = multiprocessing.Process(target=check_broken_update, args=(known_tickers[i:],))
        else:
            worker = multiprocessing.Process(target=check_broken_update, args=(known_tickers[i:i+1000],))
        worker_list.append(worker)
        worker.start()

    for worker in worker_list:
        worker.join()

    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    elapsed_time_formatted = f"{minutes:02}:{seconds:02}"

    print(f"Fin. Actual time: {elapsed_time_formatted}")

if __name__ == "__main__":
    create_all()
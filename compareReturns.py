from aliasFunctions import tickers_as_keys
from stockFunctions import get_ticker_data, trim_data, newHighAfterMention
from timeFunctions import closest_date, first_mutual_date
import json

json_file = "alias.json"


def bench_vs_user(benchmark, user_tickers: list) -> list:
    """
    returns [challenger ticker, 
            mention date, 
            bench > challenger since mention,
            inception date challenger,
            bench > challenger since inception,
            challenger price increase since mention?]

    ['F', 'Mention: 07/18/2024', True, 'Inception: 01/29/1993', True, 'Price Inc After Mention', False]
    """
    tickers_as_keys(json_file)
    alias_dict = json.load(open(json_file))
    benchmark_wins = []
    bench_close, bench_dates, bench_raw_returns = get_ticker_data(benchmark)
    def benchmark_vs_challenger(challenger, mention_date):

        if alias_dict[challenger] == "DELISTED":
            return [f"{challenger}", f"Delisted, Bench win:", True, f"Mention: {mention_date}", True, "Price Inc After Mention", False]
        
        chal_close, chal_dates, raw_returns = get_ticker_data(challenger)

        if mention_date not in chal_dates:
            mention_date = closest_date(mention_date, chal_dates)

        fmd = first_mutual_date(bench_dates, chal_dates)

        chal_close, chal_dates = trim_data(chal_close, chal_dates, fmd)
        temp_close, temp_dates = trim_data(bench_close, bench_dates, fmd)

        idx_since_reddit_mention = chal_dates.index(mention_date)
        newATH = newHighAfterMention(challenger, mention_date)

        bench_incept, chal_incept = 1,1
        bench_mention, chal_mention = 1,1

        for index in range(len(chal_close)):
            try:
                # before reddit mention date, only apply changes to inception values
                if index < idx_since_reddit_mention:
                    bench_incept *= temp_close[index]
                    chal_incept *= chal_close[index]

                else:
                    bench_incept *= temp_close[index]
                    chal_incept *= chal_close[index]

                    bench_mention *= temp_close[index]
                    chal_mention *= chal_close[index]

            except:
                print(f"error with {challenger} dates: {chal_dates[-1]}, {chal_dates[0]}, {len(chal_dates)}")
                print(f"{benchmark}: {temp_dates[-1]}, {temp_dates[0]}, {len(temp_dates)}")
                continue

        bench_incept = round(bench_incept, 3)
        chal_incept = round(chal_incept, 3)
        bench_mention = round(bench_mention, 3)
        chal_mention = round(chal_mention, 3)
        inception_date_formatted = f"Inception: {chal_dates[0]}"
        mention_date_formatted = f"Mention: {mention_date}"

        return [f"{challenger}", mention_date_formatted, bench_mention > chal_mention, inception_date_formatted, bench_incept > chal_incept, "Price Inc After Mention", newATH]

    for ticker_data in user_tickers:

        challenger = ticker_data[0]
        mention_date = ticker_data[1]
        benchmark_wins.append(benchmark_vs_challenger(challenger, mention_date))

    return benchmark_wins

if __name__ == "__main__":
    print(*bench_vs_user("SPY", [('FORD', '07/18/2024'), ("KO", '02/29/2024'), ("AAPL", '06/29/2022')]), sep="\n")

    # ['F', 'Mention: 07/18/2024', True, 'Inception: 01/29/1993', True, 'Price Inc After Mention', False]
    # ['KO', 'Mention: 02/29/2024', True, 'Inception: 01/29/1993', True, 'Price Inc After Mention', True] 
    # ['AMC', 'Mention: 06/29/2022', True, 'Inception: 12/18/2013', True, 'Price Inc After Mention', True]
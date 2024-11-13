# from aliasFunctions import values_as_keys
from compareReturns import bench_vs_user
from getUserTickers import getUserTickers

def format_results(results):
    bWinsSinceMention = sum([i[2] for i in results])
    bWinsSinceInception = sum([i[4] for i in results])
    higherPriceAfterMention = sum(i[6] for i in results)
    total_tickers = len(results)
    return total_tickers, higherPriceAfterMention, bWinsSinceMention, bWinsSinceInception

if __name__ == '__main__':

    user = "echoapollo_bot"
    search_limit = 10
    benchmark = "SPY"

    usertickers, processingTime = getUserTickers(user, search_limit)
    raw_results = bench_vs_user(benchmark, usertickers)
    resFiltered = format_results(raw_results)

    formatted = f"{resFiltered[0]},{resFiltered[1]},{resFiltered[2]},{resFiltered[3]},{user},{processingTime},{benchmark}\n"
    # totalTickers, benchWinsSinceMention, benchWinsSinceInception, higherPriceAfterMention, user, scrapeAndParseTime, benchmark
    
    print(formatted)
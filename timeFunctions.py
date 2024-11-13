from datetime import datetime

def convert_unix_time(unix_time):
    timestamp = float(unix_time)
    date = datetime.fromtimestamp(timestamp)
    return date.strftime("%m/%d/%Y")

def closest_date(mention_date: str, valid_dates: list) -> str:
    dt_mention_date = datetime.strptime(mention_date, "%m/%d/%Y")
    dt_valid_dates = [datetime.strptime(date_str, "%m/%d/%Y") for date_str in valid_dates]

    def days_apart(date: datetime) -> int:
        return abs(date - dt_mention_date)
    
    closest_date = min(dt_valid_dates, key=days_apart)

    return closest_date.strftime("%m/%d/%Y")

def first_mutual_date(benchmark_dates, challenger_dates):
    seen_dates = set(challenger_dates)
    for date in benchmark_dates:
        if date in seen_dates:
            return date
    print(f"error, no matching dates")

def delisted_checker(last_traded):
    # check if the ticker has been traded in the last 5 days
    last_traded_raw = last_traded.replace(tzinfo=None)
    today = datetime.now()
    days_since_last_trade = abs(last_traded_raw-today)
    return days_since_last_trade.days > 5
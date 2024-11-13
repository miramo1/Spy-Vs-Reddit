import json

file = r"alias.json"

def sort_alias(json_file):
    data = json.loads(open(json_file, "r").read())
    sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[0])}
    with open(json_file, "w") as f:
        f.write(json.dumps(sorted_data, indent=4))

def add_alias(json_file, ticker, alias):
    # tickers must be keys for add_alias to work properly
    try:
        tickers_as_keys(json_file)
    except:
        pass

    ticker = ticker.upper()
    alias = alias.upper()

    data = json.loads(open(json_file, "r").read())
    if ticker in data:
        if alias in data[ticker]:
            return
        else:
            data[ticker].append(alias)
    else:
        data[ticker] = [alias]

    with open(json_file, "w") as f:
        f.write(json.dumps(data, indent=4))
    # values_as_keys(file)
    # sort_alias(file)

    print(f"Added ticker {ticker} with alias {alias}")

def values_as_keys(json_file):
    data = json.loads(open(json_file, "r").read())

    # if there are any spaces in the keys, then values are already keys
    if any([True for key in data.keys() if " " in key]):
        return
    
    new_data = {}
    for k, v in data.items():
        for string in v:
            new_data[string] = k
    with open(json_file, "w") as f:
        f.write(json.dumps(new_data, indent=4))
    sort_alias(file)

def tickers_as_keys(json_file):
    data = json.loads(open(json_file, "r").read())

    # if there are any spaces in the keys, then tickers arent keys
    if any([True for key in data.keys() if " " in key]):
        new_dict = {}
        for k, v in data.items():
            if v in new_dict:
                new_dict[v].append(k.upper())
            else:
                new_dict[v] = [k.upper()]
        with open(json_file, "w") as f:
            f.write(json.dumps(new_dict, indent=4))
        sort_alias(file)
    else:
        return

if __name__ == "__main__":
    tickers_as_keys(file)
    known_tickers = list(json.load(open(file)).keys())
    print(len(known_tickers))
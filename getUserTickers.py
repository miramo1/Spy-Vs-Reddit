from aliasFunctions import values_as_keys
from datetime import datetime
from timeFunctions import convert_unix_time
import json, multiprocessing, praw, prawcore, re, yaml

json_file = "alias.json"
values_as_keys(json_file)
alias_dict = json.load(open(json_file))
alias = alias_dict.keys()
configFile = "config.yaml"

class word_node:
    def __init__(self):
        self.children = {}
        self.is_end_of_key = False
        self.value = None  # the ticker associated with the alias, eg "MICRO SOFT": "MSFT"

class ticker_tree:
    def __init__(self):
        self.root = word_node()

    def insert(self, key, value):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = word_node()
            node = node.children[char]
        node.is_end_of_key = True
        node.value = value  # ticker is stored at the end

    def find_all_matches(self, text):
        matches = set()
        words = text.split()
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    break
                node = node.children[char]
            else:
                if node.is_end_of_key and node.value == word:
                    matches.add(node.value)

        return list(matches)

ticker_tree = ticker_tree()
for key, val in alias_dict.items():
    ticker_tree.insert(key, val)

def strip_text(text):
    # upper case to match alias list
    text = text.replace("\n", " ").upper()
    text = text.replace("[REMOVED]", text)
    # filter out links
    text = ' '.join([word for word in text.split() if 'HTTP' not in word])
    # Use regex to replace all punctuation except for the dollar sign
    text = re.sub(r'[^\w\s]', "", text)
    # get rid of all extra spaces
    text = text.replace("\n", " ")
    text = re.sub(r'\s+', " ", text)
    text = text.rstrip()

    return text

def time_delta(startTime):
    return round((datetime.now()-startTime).total_seconds(),4)

def set_sort_ticker_dates(userData: list) -> list:
    # orders the ticker by date of appearance
    # userData = [("DATE-2023": ["AAPL, "MSFT"]), ""DATE-2019": ["AMD", "MSFT"]]

    date_ticker_dict = {}
    for item in userData:
        # text is currently a string, must convert to list to use parse_tickers()
        date = item[0]
        for ticker in item:
            date_ticker_dict[date] = ticker

    # date_ticker_dict now = {"DATE": ["AAPL, TWTR", "MSFT"], "DATE": ["MSFT", "GOOGL"]}
    # need to sort dictionary by date with newest first. 
    sorted_date_ticker = dict(sorted(date_ticker_dict.items()))
    # print(*sorted_date_ticker.items(), sep="\n")

    set_sorted_dict = {}
    for date, ticker_list in sorted_date_ticker.items():
        for tickers in ticker_list:
            if tickers not in set_sorted_dict:
                set_sorted_dict[tickers] = convert_unix_time(date)
    return list(set_sorted_dict.items())

def get_con_comments(author, search_limit, output_queue):

    with open(configFile) as config_file:
        config = yaml.safe_load(config_file)
        client_id = config["client_id"]
        client_secret = config["client_secret"]
        username = config["username"]
        password = config["password"]
        user_agent = config["user_agent"]
        subreddits = config["investing_subs"]

    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent,
                        username=username,
                        password=password)
    raw_data = []
    scrape_time = 0
    parse_time = 0
    comments = reddit.redditor(author).comments.controversial(limit=search_limit)
    try:
        for item in comments:
            startingTime = datetime.now()
            if item.subreddit in subreddits:
                if item.body != None:
                    text = strip_text(item.body)
                    scrape_time += time_delta(startingTime)
                    start_parse = datetime.now()

                    tickers = ticker_tree.find_all_matches(text)

                    if tickers:
                        raw_data.append((item.created_utc, tickers))
                    parse_time += time_delta(start_parse)

    except prawcore.exceptions.Forbidden:
        output_queue.put((raw_data, scrape_time, parse_time))
    except prawcore.exceptions.NotFound:
        output_queue.put((raw_data, scrape_time, parse_time))

    output_queue.put((raw_data, scrape_time, parse_time))

def get_hot_comments(author, search_limit, output_queue):

    with open(configFile) as config_file:
        config = yaml.safe_load(config_file)
        client_id = config["client_id"]
        client_secret = config["client_secret"]
        username = config["username"]
        password = config["password"]
        user_agent = config["user_agent"]
        subreddits = config["investing_subs"]

    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent,
                        username=username,
                        password=password)
    raw_data = []
    scrape_time = 0
    parse_time = 0

    comments = reddit.redditor(author).comments.hot(limit=search_limit)

    try:
        for item in comments:
            startingTime = datetime.now()
            if item.subreddit in subreddits:
                if item.body != None:
                    text = strip_text(item.body)
                    scrape_time += time_delta(startingTime)
                    start_parse = datetime.now()

                    tickers = ticker_tree.find_all_matches(text)

                    if tickers:
                        raw_data.append((item.created_utc, tickers))
                    parse_time += time_delta(start_parse)

    except prawcore.exceptions.Forbidden:
        output_queue.put((raw_data, scrape_time, parse_time))
    except prawcore.exceptions.NotFound:
        output_queue.put((raw_data, scrape_time, parse_time))

    output_queue.put((raw_data, scrape_time, parse_time))

def get_posts(author, search_limit, output_queue):

    with open(configFile) as config_file:
        config = yaml.safe_load(config_file)
        client_id = config["client_id"]
        client_secret = config["client_secret"]
        username = config["username"]
        password = config["password"]
        user_agent = config["user_agent"]
        subreddits = config["investing_subs"]

    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent,
                        username=username,
                        password=password)
    raw_data = []
    scrape_time = 0
    parse_time = 0

    submissions = reddit.redditor(author).submissions.top(limit=search_limit)

    try:
        for item in submissions:
            startingTime = datetime.now()
            if item.subreddit in subreddits:
                if item.selftext != None:
                    text = strip_text(item.title + " " +  item.selftext)
                    scrape_time += time_delta(startingTime)
                    start_parse = datetime.now()
                    tickers = ticker_tree.find_all_matches(text)
                    if tickers:
                        raw_data.append((item.created_utc, tickers))
                    parse_time += time_delta(start_parse)

    except prawcore.exceptions.Forbidden:
        output_queue.put((raw_data, scrape_time, parse_time))
    except prawcore.exceptions.NotFound:
        output_queue.put((raw_data, scrape_time, parse_time))

    output_queue.put((raw_data, scrape_time, parse_time))

def getUserTickers(user, count):
    start_time = datetime.now()

    con_comments_queue = multiprocessing.Queue()
    hot_comments_queue = multiprocessing.Queue()
    posts_queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=get_con_comments, args=(user, count, con_comments_queue,)) 
    p2 = multiprocessing.Process(target=get_hot_comments, args=(user, count, hot_comments_queue,))
    p3 = multiprocessing.Process(target=get_posts, args=(user, count, posts_queue,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    d1, scrape1, parse1 = con_comments_queue.get()
    d2, scrape2, parse2 = hot_comments_queue.get()
    d3, scrape3, parse3 = posts_queue.get()

    data = d1+d2+d3
    scrape_time = round(scrape1+scrape2+scrape3, 3)
    parse_time = round(parse1+parse2+parse3, 3)

    fin = round((datetime.now()-start_time).total_seconds(),3)

    return set_sort_ticker_dates(data), round(scrape_time+parse_time+fin,3)

if __name__ == "__main__":
    x = getUserTickers("echoapollo_bot", 10)
    print(*x[0], sep="\n")
    # ([('APH', '05/22/2018'), ('TSLA', '08/25/2018'), ('TNDM', '08/29/2018'), ('SQ', '08/29/2018'), ('MU', '09/03/2018'), ('AAPL', '11/04/2018'), ('ROL', '12/11/2018'), ('WMT', '12/19/2018'), ('ORCL', '12/20/2018')], 2.369)



from schemas.ticker import Ticker

DIFF = 1.1  # 10%


def is_higher_than_year_ago(ticker_today: Ticker, ticker_year_ago: Ticker) -> bool:
    return ticker_today.value >= ticker_year_ago.value * DIFF

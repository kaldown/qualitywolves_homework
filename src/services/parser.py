from utils.comparator import is_higher_than_year_ago
from schemas.ticker import TickerResult
from services.fetcher import fetch_ticker
from datetime import date, timedelta


async def process_ticker(session, ticker: str, trade_date: date) -> TickerResult | None:
    if not (ticker_today := await fetch_ticker(session, ticker, trade_date)):
        return

    year_ago = trade_date - timedelta(days=365)
    if not (ticker_year_ago := await fetch_ticker(session, ticker, year_ago)):
        return
    if not is_higher_than_year_ago(ticker_today, ticker_year_ago):
        return
    return TickerResult(ticker_today=ticker_today, ticker_year_ago=ticker_year_ago)

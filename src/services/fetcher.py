import aiomoex
from utils.converter import candle_to_ticker, response_to_candle
from schemas.ticker import Ticker
from datetime import date


async def fetch_ticker(session, ticker: str, trade_date: date) -> Ticker | None:
    trade_date = str(trade_date)
    candle_data = await aiomoex.get_market_candles(session, ticker, start=trade_date, end=trade_date)
    if not (candle := response_to_candle(candle_data)):
        return
    return candle_to_ticker(ticker=ticker, candle=candle)

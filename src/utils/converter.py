from schemas.ticker import Ticker, Candle


def response_to_candle(data: list[dict[str, str | int | float]]) -> Candle | None:
    if not data:
        return
    candle_data = data[0]
    return Candle(open=candle_data["close"], datetime=candle_data["end"])


def candle_to_ticker(ticker: str, candle: Candle) -> Ticker:
    return Ticker(
        ticker=ticker,
        value=candle.open,
        datetime=candle.datetime,
    )

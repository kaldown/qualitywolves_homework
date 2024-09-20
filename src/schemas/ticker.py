from dataclasses import dataclass, field
from datetime import datetime
from utils.time import to_utc


@dataclass
class Candle:
    open: float
    datetime: field(init=False)

    def __post_init__(self):
        self.datetime = to_utc(self.datetime)


@dataclass
class Ticker:
    ticker: str
    datetime: datetime
    value: float

    def __repr__(self):
        return f"{self.ticker}: {self.value} by {str(self.datetime)}"


@dataclass
class TickerResult:
    ticker_year_ago: Ticker
    ticker_today: Ticker

    def __repr__(self):
        return f"Year ago: {self.ticker_year_ago}. Today: {self.ticker_today}"

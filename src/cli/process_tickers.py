import click
import aiohttp
import asyncio
from datetime import date
from services.parser import process_ticker
from utils.misc import coro
from utils.default import DEFAULT_TICKERS

LIMIT_CONTAINER = 10


@click.command()
@click.option("--tickers", type=list[str], default=DEFAULT_TICKERS)
@click.argument("trade_date", type=click.DateTime(formats=["%Y-%m-%d"]))
@coro
async def process_tickers(tickers: list[str], trade_date: date) -> None:
    async with aiohttp.ClientSession() as session:
        tasks = [process_ticker(session, ticker, trade_date) for ticker in tickers]
        result = [res for res in await asyncio.gather(*tasks) if res]
        click.echo(result)


if __name__ == "__main__":
    process_tickers()

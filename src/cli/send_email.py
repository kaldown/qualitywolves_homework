from services.sender import send_email
from utils.default import DEFAULT_TICKERS
from utils.misc import coro
import os
from datetime import date
import aiohttp
from services.parser import process_ticker
import asyncio
import click


@click.command()
@click.argument("trade_date", type=click.DateTime(formats=["%Y-%m-%d"]))
@coro
async def process_tickers_and_send(trade_date: date) -> None:
    async with aiohttp.ClientSession() as session:
        tasks = [process_ticker(session, ticker, trade_date) for ticker in DEFAULT_TICKERS]
        if not (result := [res for res in await asyncio.gather(*tasks) if res]):
            click.echo("No tickers satisfy business logic")
        else:
            send_email(
                sender_email=os.getenv("SMTP_SENDER"),
                receiver_email="kaldownj@gmail.com",
                subject="Blue Chips prices",
                body=result,
                smtp_server=os.getenv("SMTP_SERVER"),
                port=587,
                login=os.getenv("SMTP_LOGIN"),
                password=os.getenv("SMTP_PASSWORD"),
            )


if __name__ == "__main__":
    process_tickers_and_send()

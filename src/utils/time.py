from datetime import timezone, datetime, timedelta, date


def _datetime_moscow() -> datetime:
    return datetime.now(tz=timezone.utc) + timedelta(hours=3)


def today_moscow() -> date:
    return _datetime_moscow().date()


def year_ago_moscow() -> date:
    return (_datetime_moscow() - timedelta(days=365)).date()


def to_utc(dt) -> datetime:
    dt = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
    dt -= timedelta(hours=3)
    return dt.replace(tzinfo=timezone.utc)

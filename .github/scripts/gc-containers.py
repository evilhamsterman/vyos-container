#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ghapi",
#     "pendulum",
#     "typer",
# ]
# ///

import re
from enum import StrEnum
from typing import Annotated, Final

import typer
from pendulum import DateTime, parse

DEFAULT_AGE: Final[str] = "1m"


class AgeSuffix(StrEnum):
    DAYS = "d"
    WEEKS = "w"
    MONTHS = "m"
    YEARS = "y"


def validate_age(age: str) -> str:
    """
    Checks if the age string is in the format <number><suffix>
    where suffix is d, w, m, y
    """
    if not re.match(r"^[\d]+[dwmy]$", age):
        raise typer.BadParameter("Age must be formatted like '4w'")
    return age


def parse_age(age: str) -> DateTime:
    """
    Parses the age and returns a Date = today - age
    """
    t = DateTime.today()

    match age[-1]:
        case AgeSuffix.DAYS:
            days = int(age[:-1])
            return t.subtract(days=days)
        case AgeSuffix.WEEKS:
            weeks = int(age[:-1])
            return t.subtract(weeks=weeks)
        case AgeSuffix.MONTHS:
            months = int(age[:-1])
            return t.subtract(months=months)
        case AgeSuffix.YEARS:
            years = int(age[:-1])
            return t.subtract(years=years)
        case _:
            raise ValueError("Somehow the value couldn't be parsed")


def main(
    age: Annotated[
        str, typer.Argument(callback=validate_age, help="Age of containers to remove.")
    ] = DEFAULT_AGE,
) -> None:
    print(parse_age(age))


if __name__ == "__main__":
    typer.run(main)

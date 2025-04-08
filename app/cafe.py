from __future__ import annotations
import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Friends should be vaccinated")

        vaccine = visitor["vaccine"]

        if vaccine["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Friends should be vaccinated again")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Friends should buy masks")

        return f"Welcome to {self.name}"

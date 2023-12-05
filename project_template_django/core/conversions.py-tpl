from decimal import Decimal


def to_decimal(n: float | int, places: int = 3) -> Decimal:
    """
    Convert any float | int to a decimal with a given number of places.
    """
    round_places = Decimal(10) ** -places  # == Decimal("0.001") for places=3
    return Decimal(n).quantize(round_places)

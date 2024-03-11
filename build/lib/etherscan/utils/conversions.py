from decimal import Decimal


class Conversions:
    @staticmethod
    def to_ticker_unit(val: int, decimals: int = 18) -> Decimal:
        factor = Decimal("10") ** Decimal("-{}".format(decimals))
        return Decimal(val) * factor

    @staticmethod
    def to_smallest_unit(val: int, decimals: int = 18) -> Decimal:
        factor = Decimal("10") ** Decimal("+{}".format(decimals))
        return Decimal(val) * factor

"""Display helpers for revenue values."""


def format_cents(cents):
    """Format integer cents as a string with two decimals and no currency symbol."""
    sign = "-" if cents < 0 else ""
    whole, fraction = divmod(abs(cents), 100)
    return f"{sign}{whole}.{fraction:02d}"

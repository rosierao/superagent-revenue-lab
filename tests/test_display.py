from revenue.display import format_cents


def test_formats_whole_dollars():
    assert format_cents(2000) == "20.00"


def test_formats_cents_with_leading_zero():
    assert format_cents(5) == "0.05"


def test_formats_negative_cents():
    assert format_cents(-5) == "-0.05"


def test_formats_zero():
    assert format_cents(0) == "0.00"


def test_formats_negative_whole_dollars():
    assert format_cents(-2000) == "-20.00"


def test_pads_single_digit_cents():
    assert format_cents(105) == "1.05"


def test_never_includes_a_currency_symbol():
    formatted = format_cents(1234)
    assert formatted == "12.34"
    assert not any(symbol in formatted for symbol in ("$", "€", "£", "¥"))

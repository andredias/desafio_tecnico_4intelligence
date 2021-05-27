from string import digits


def remove_symbols(value: str) -> str:
    return ''.join(v for v in value if v in digits)

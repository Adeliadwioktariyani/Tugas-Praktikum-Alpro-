# Modul untuk menghitung bunga tabungan

def compound_interest(principal, rate, years):
    """
    Menghitung nilai akhir dengan bunga majemuk.
    """
    future_value = principal * (1 + rate) ** years
    return future_value


def simple_interest(principal, rate, years):
    """
    Menghitung nilai akhir dengan bunga sederhana.
    """
    future_value = principal * (1 + rate * years)
    return future_value

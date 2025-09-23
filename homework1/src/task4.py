
def calculate_discount(price, discount):
    try:
        return round(price * (1 - discount / 100), 2)
    except TypeError:
        raise ValueError(" The pric and discount must both be a numerical value")

# Task4
# Sebastian Sanchez
# CS4300

# Function to calulate the final price after applying a percentage discount
def calculate_discount(price, discount):
    try:
        # calculate the discounted price
        # if a floating point is calculated, round to the result to 2 decimal places
        return round(price * (1 - discount / 100), 2)
        # raise an error if a non-numerica value is passed
    except TypeError:
        raise ValueError(" The price and discount must both be a numerical value")

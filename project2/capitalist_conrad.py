from typing import TextIO

MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
price = INITIAL_PRICE
print(f"starting price ${price:,.2f}")
out_file: TextIO = open("OUTPUT_FILE.txt", 'w')
i = 0
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    import random

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + price_change)
    i += 1
    print(f"on day {i} price is ${price:,.2f}", file=out_file)
out_file.close()

print(max(2, 7))
print(min(500, 2000))

# sum([list])
print(sum([2, 2]))
print(sum([2, 4, 6, 8]))

# round
print(round(7.2))
print(round(-1.2))
print(round(7.8))
print(round(.349, 2))
print(round(4500.6732458723, 5))

#ceil, floor - math module
import math
print('ceil', math.ceil(4.2))
print('floor', math.floor(5.9))

# random #s
import random
# roll the dice
die = random.randint(1, 6)
print('die', die)
rand_1 = random.randint(10,20)
print(rand_1)

# format a currency
car_price = 34782.454444
car_price_formatted = "${:,.2f}".format(car_price)
print('formatted car price', car_price_formatted)

# format a percent
interest_pct = .0378645
interest_pct_formatted = "{:.4%}".format(interest_pct)
print('pct', interest_pct_formatted)
price_per_item = 5
item_amount = 10

total_price = item_amount * price_per_item

print("total price: " + str(total_price) + "$")

arbitrary_price = price_per_item + price_per_item + price_per_item * 2

print("arbitrary price: " + str(arbitrary_price) + "$")

ratio = total_price / arbitrary_price

print("the total price is " + str(ratio) + " greater than the arbitrary price")

remainder = total_price % item_amount

if remainder == 0:
    print("the total price is valid")
else:
    print("the total price is invalid")

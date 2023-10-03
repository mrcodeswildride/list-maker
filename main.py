def print_item(quantity, item):
  if quantity == 1:
    print(f"1 {item}")
  elif quantity > 1:
    print(f"{quantity} {item}s")

print()

num_apples = int(input("How many apples to buy? "))
num_oranges = int(input("How many oranges to buy? "))
num_candy_bars = int(input("How many candy bars to buy? "))

print("\nYour shopping list:")
print_item(num_apples, "apple")
print_item(num_oranges, "orange")
print_item(num_candy_bars, "candy bar")

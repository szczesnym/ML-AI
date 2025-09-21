cheeses = [
    ("Roquefort", 12.5, 2),
    ("Stilton", 11.24, 1),
    ("Brie", 9.3, 1),
    ("Gouda", 8.55, 1),
    ("Edam", 11.0, 1),
    ("Parmezan", 16.5, 3.5),
    ("Mozzarella", 14.0, 0.13),
    ("Czechoslovak sheep's milk cheese", 122.32, 0.22)
]
max_name_length = 0
max_number_length = 0
order_value = 0

for cheese in cheeses:
    if len(cheese[0]) > max_name_length:
        max_name_length = len(cheese[0])
    if len(str(int(cheese[1]))) > max_number_length:
        max_number_length = len(str(int(cheese[1])))
    order_value += cheese[1] * cheese[2]

for cheese in cheeses:
    price_str_len = len(str(int(cheese[1])))
    cheese_value = cheese[1] * cheese[2]
    line = (f"Produkt: %s" % cheese[0] + " " * (max_name_length - len(cheese[0])) +
                 f"\tmasa w kg: %.2f" % cheese[2] +
                 f"\t\tcena za kg: " + " " * (max_number_length - price_str_len) +"%.2f" % cheese[1])
    print(line)
print("Suma PLN: %3.2f" % order_value)
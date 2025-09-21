shop_basket= {
    'piekarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
item_count = 0
for (shop, items) in shop_basket.items():
    print(f"Idę do {shop.capitalize()}, kupuję tu nastęujące rzeczy %s" % [str(item.capitalize()) for item in items])
    item_count += len(items)
print(f'W sumie kupuję %.0f produktów' % item_count)
cheese_1_name = "Roquefort"
cheese_1_price = 12.5
cheese_2_name = "Stilton"
cheese_2_price = 11.24
cheese_3_name = "Brie"
cheese_3_price = 9.3
cheese_4_name = "Gouda"
cheese_4_price = 8.55
cheese_5_name = "Edam"
cheese_5_price = 11.0
cheese_6_name = "Parmezan"
cheese_6_price = 16.5
cheese_7_name = "Mozzarella"
cheese_7_price = 14.0
cheese_8_name = "Czechoslovak sheep's milk cheese"
cheese_8_price = 122.32

#ver1
print("Shopping list:\n" + \
      f"\tCheese name: %s, Price per 1 kg: %3.2f" % (cheese_1_name, cheese_1_price) + "\n" + \
      f"\tCheese name: %s, Price per 1 kg: %3.2f" % (cheese_2_name, cheese_2_price) + "\n" + \
      f"\tCheese name: %s, Price per 1 kg: %3.2f" % (cheese_3_name, cheese_3_price) + "\n" + \
      f"\tCheese name: %s, Price per 1 kg: %3.2f" % (cheese_4_name, cheese_4_price) + "\n" + \
      f"\tCheese name: %s, Price per 1 kg: %3.2f" % (cheese_5_name, cheese_5_price) + "\n" + \
      f"\tCheese name: %s, Price per 1 kg: %3.2f" % (cheese_6_name, cheese_6_price) + "\n" + \
      f"\tCheese name: %s, Price per 1 kg: %3.2f" % (cheese_7_name, cheese_7_price) + "\n" + \
      f"\tCheese name: %s, Price per 1 kg: %3.2f" % (cheese_8_name, cheese_8_price) + "\n")
#ver2
head= "Shopping list:\n"
line1 = "\tCheese name: {0} Price per 1 kg: {1:.2f}\n".format(cheese_1_name, cheese_1_price)
line2 = "\tCheese name: {cheese} Price per 1 kg: {cheese_price:.2f}\n".format(cheese = cheese_2_name, cheese_price = cheese_2_price)
line3 = "\tCheese name: {} Price per 1 kg: {:.2f}\n".format(cheese_3_name, cheese_3_price)
#Na tym etapie skończyły mi się pomysły na inne sposoby formatowania
line4 = "\tCheese name: {} Price per 1 kg: {:.2f}\n".format(cheese_4_name, cheese_4_price)
line5 = "\tCheese name: {} Price per 1 kg: {:.2f}\n".format(cheese_5_name, cheese_5_price)
line6 = "\tCheese name: {} Price per 1 kg: {:.2f}\n".format(cheese_6_name, cheese_6_price)
line7 = "\tCheese name: {} Price per 1 kg: {:.2f}\n".format(cheese_7_name, cheese_7_price)
line8 = "\tCheese name: {} Price per 1 kg: {:.2f}\n".format(cheese_8_name, cheese_8_price)

print(head + line1 + line2 + line3 + line4 + line5 + line6  + line7 + line8)








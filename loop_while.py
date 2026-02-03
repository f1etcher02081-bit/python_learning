money = 100
price_per_product = 100
products_bought = 0

while money >= price_per_product:
    money -= price_per_product
    products_bought += 1

print(f"You bought {products_bought} products.")
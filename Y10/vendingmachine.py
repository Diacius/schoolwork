total_drink_cost = 1.50
drink_cost = 1.50

coin_value = 0
while coin_value < drink_cost:
    coin_value = float(input("coin as deicaml"))
    print(drink_cost)
    print(coin_value)
    drink_cost = drink_cost - coin_value
    print(drink_cost)
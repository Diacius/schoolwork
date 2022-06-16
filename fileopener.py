import io
print('Cars Incorporated')
with io.open('cars.txt', 'w+', encoding='utf8') as f:
    carName = input('Whats the name of the car?')
    f.write("\nVehicle Name:" + carName)
    carPrice = float(input('What is the price of the car'))
    f.write(f"\nPrice of car: {carPrice}")
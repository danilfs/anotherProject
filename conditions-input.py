user_age = int(input("Введите ваш возраст:\n"))

if user_age >= 18 and user_age <= 65:
	print("Больше 18")
elif user_age > 65:
	print("Пенсия")
else:
	print("Меньше 18")
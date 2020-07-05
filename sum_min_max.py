import random
import sys
import math

min_l = 5 #мінімальна кількість елементів масиву
max_l = 10 #максимальна кількість елементів масиву
min_val = -100 #мінімальний можливий ліміт ряду
max_val = 100 #максимальний можливий ліміт ряду

#Функція визначає чи введене значення є числом чи символом
def to_number(s):
	res = None
	try:
		res = float(s) #Якщо введене значення є числом, то перетворюємо його в десяткове
	except Exception as e: #в іншому випадку надаємо значення "NaN"
		res = 'NaN'
	return res

def create():
	a = None
	while not a:
		r = input('Manual input or Random? M / R (x to exit): ').upper()
		if r == 'M': #визначений ввід елементів
			str_input = input('Type in an array or numbers (separate with " " (space), decimal delimiter - . (dot)):')
			# 2 3 4 99 -7 37.4
			str_a = str_input.split(' ') # отримуємо масив з введеними елементами 
			# ['2', '3', '4', '99', '-7', '37.4', 'sds']
			a = [to_number(x) for x in str_a] # Помилка, якщо ввели не число
		elif r == 'R': # випадковий ввід елементів
			print('Random array generation, length range: {}...{}'.format(min_l, max_l))
			l = random.randrange(min_l, max_l + 1) #визначаємо кількість елементів у масиві
      #Друкуємо кількість елементів у масиві і верхній та нижній ліміти ряду
			print('Making array of {} ints from {} to {}'.format(l, min_val, max_val))
      #визначаємо елементи масиву
			a = [random.randrange(min_val, max_val + 1) for x in range(0, l)]
		elif r == 'X': #Вийти
			print("exitting")
			break
		else:
			print("Type M, R or X")
	return a

def find_min_max(arr):
	## Poshuk checkez sortuvannya
	# arr.sort()
	## first element - arr[0] - minimal
	## last element - arr[-1] - maximal
	# min = arr[0]
	# max = arr[-1]
	# Часова складність сортування mix/max = O(n*log(n))
	# https://www.bigocheatsheet.com/

	# Часова складність пошуку mix/max = O(n) - krashe za .sort()
	# https://afteracademy.com/blog/find-the-minimum-and-maximum-value
	## ручний пошук min / max
	# _min = arr[0]
	# _max = arr[0]
	# for x in arr:
	# 	if x < _min:
	# 		_min = x
	# 	if x > _max:
	# 		_max = x

	##Вбудовані функції:
	_min = min(arr)
	_max = max(arr)

	return (_min, _max)

def sum_min_max(arr):
	if not arr:
		print("No array created :-(")
		return math.nan

	print("Our array: ", arr)
	# перевірити чи набір являється множиною чи пустою множиною
	if (type(arr) is not list or len(arr) == 0):
		print("Broken array")
		return math.nan
	# Перевірити чи всі елементи масиву являються числами, виключити ті, що не являються
	arr = [x for x in arr if type(x) in [int, float]]
	# необхідна знову перевірка на тривалість ряду:
	if len(arr) == 0:
		print ("No numbers in this array")
		return math.nan
	_min, _max = find_min_max(arr) # виклик функціі пошуку мінімуму та максимуму
	s =  _min + _max #знаходимо суму знайдених елементів
  #Роздрукувати результат
	print("Sum of minimal and maximal: {} + {} = {}".format(_min, _max, s))
	return s

def main():
	arr = create()
	sum_min_max(arr)

if __name__ == "__main__":
	main()
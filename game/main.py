import json
from os import system, name
import random

def saving(arg): #сохранение файла
	with open('save.json', 'w') as js:
		json.dump(arg, js)
		js.close()

def output(matrix): #вывод матрицы
	count = 1
	print(end = '  ')
	for i in range(1, len(matrix[0])+1):
		print(i, end = ' ')
	print()
	for i in matrix:
		print(count, end = ' ')
		count += 1
		print(*i, ' ')

def clear(): #очистка экрана
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')


answ = input('Привет! Вы зашли в игру "Сапёр"! Для того чтобы начать новую игру - напишите "new"\nДля того чтобы загрузить сохранение - напишите "load" >>> ')
if answ == 'new': #создание матрицы и установка бомб
	while True: #предохранитель от ошибок в размере поля
		try: x,y = map(int, input('Введите размеры поля (например 6 50) >>> ').split(' '))
		except: 
			print('Ошибка в размерах поля!')
			continue
		break; 
	matrix = []
	for i in range(x): #генерация "скрытой" матрицы 
		matrix.append([0]*y)
	matrusr = []
	for j in range(x): #генерация матрицы пользователя
		matrusr.append(['*']*y)
	while True: #предохранитель от ошибок в количестве бомб
		try: bomb = int(input('введите кол-во бомб >>> '))
		except: 
			print('Ошибка в кол-ве бомб (не число)!')
			continue; 
		if bomb > 0 and bomb < (x*y):
			break;  
	for i in range(bomb): #
		rand1 = random.randint(0, x-1)
		rand2 = random.randint(0,y-1)
		matrix[rand1][rand2] = 'B'
		if rand1 != 0 and matrix[rand1-1][rand2] != 'B': matrix[rand1-1][rand2] += 1
		if rand1 != x-1 and matrix[rand1+1][rand2] != 'B': matrix[rand1+1][rand2] += 1
		if rand2 != 0 and matrix[rand1][rand2-1] != 'B': matrix[rand1][rand2-1] += 1
		if rand2 != y-1 and matrix[rand1][rand2+1] != 'B': matrix[rand1][rand2+1] += 1
		if rand1 != 0 and rand2 != 0 and matrix[rand1-1][rand2-1] != 'B': matrix[rand1-1][rand2-1] += 1
		if rand1 != x-1 and rand2 != y-1 and matrix[rand1+1][rand2+1] != 'B': matrix[rand1+1][rand2+1] += 1
		if rand2 != 0 and rand1 != x-1 and matrix[rand1+1][rand2-1] != 'B': matrix[rand1+1][rand2-1] += 1
		if rand2 != y-1 and rand1 != 0 and matrix[rand1-1][rand2+1] != 'B': matrix[rand1-1][rand2+1] += 1

elif answ == "load": #загрузка сохранённой матрицы
	f = open('save.json', 'r')
	data = json.load(f)
	matrix = data['matrix']
	matrusr = data['usermatrix']
	x = data['height']
	y = data['width']
	bomb = data['bombs']
	print('Загружено!')
	f.close()

while True: #цикл игры
	clear()
	output(matrusr)
	try: x1, y1 = map(int, input('Введите координаты (например 2 3) >>> ').split(' ')) #текущие координаты пользователя
	except: continue; 
	if y1 > x or x1 > y or y1 <= 0 or x1 <= 0: continue; #неправильные координаты
	x1 -= 1
	y1 -= 1
	if matrusr[x1][y1] != '*' and matrusr[x1][y1] != 'P': continue; #неповторение открытия клетки
	try: answ = int(input('Кнопка действия: 0 - открыть клетку или убрать флажок, \n1 - поставить флажок, 2 - сохранить и 3 - выйти. >>> ')) #действие пользователя
	except: continue; 
	if answ == 0: #ничего не делать/удалить флажок
		if matrusr[x1][y1] == 'P':
			matrusr[x1][y1] = '*'
			if matrix[x1][y1] == 'R':
				matrix[x1][y1] = 'B'
			continue; 
		else: matrusr[x1][y1] = matrix[x1][y1] #"открытие" текущей клетки
	if answ  == 1: #поставить флажок
		matrusr[x1][y1] = 'P'
		if matrix[x1][y1] == 'B': #
			matrix[x1][y1] = 'R'
		coun1 = 0
		coun2 = 0
		for i in range(x): #поиск количества флажков и флажков с бомбами
			for j in range(y):
				if matrusr[i][j] == 'P':
					coun1 += 1
				if matrix[i][j] == 'R':
					coun2 += 1
		if coun1 == coun2 and coun1 == bomb: #проверка на выигрыш
			clear()
			output(matrusr)
			print('Вы выиграли! Поздравляем!')
			break; 
		continue; 
	elif answ == 2: #сохранение текущей игры
		dic = {
			'matrix':matrix,
			'usermatrix':matrusr,
			'height':x,
			'width':y,
			'bombs':bomb
			}
		saving(dic)
		print('Сохранено!')
		continue; 
	elif answ == 3: #завершение игры
		break; 
	if matrix[x1][y1] == 'B': #проигрыш
		output(matrix) #вывод скрытого поля
		print('Вы проиграли!')
		break; 
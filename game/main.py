import json
from os import system, name
import random

def saving(arg):
	with open('save.json', 'w') as js:
		json.dump(arg, js)
		js.close()

def vivod(o):
	count = 1
	print(end = '  ')
	for x in range(1, len(o[0])+1):
		print(x, end = ' ')
	print()
	for i in o:
		print(count, end = ' ')
		count += 1
		print(*i, ' ')

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')


answ = input('Привет! Вы зашли в игру "Сапёр"! Для того чтобы начать новую игру - напишите "new"\nДля того чтобы загрузить сохранение - напишите "load" >>> ')
if answ == 'new':
	x,y = map(int, input('Введите размеры поля (например 6 50) >>> ').split(' '))
	o = []
	for i in range(x):
		o.append([0]*y)
	r = []
	for j in range(x):
		r.append(['*']*y)
	while True:
		q = int(input('введите кол-во бомб >>> '))
		if q > 0 and q < (x*y):
			break;
	for i in range(q):
		k = random.randint(0, x-1)
		l = random.randint(0,y-1)
		o[k][l] = 'B'
		if k != 0 and o[k-1][l] != 'B': o[k-1][l] += 1
		if k != x-1 and o[k+1][l] != 'B': o[k+1][l] += 1
		if l != 0 and o[k][l-1] != 'B': o[k][l-1] += 1
		if l != y-1 and o[k][l+1] != 'B': o[k][l+1] += 1
		if k != 0 and l != 0 and o[k-1][l-1] != 'B': o[k-1][l-1] += 1
		if k != x-1 and l != y-1 and o[k+1][l+1] != 'B': o[k+1][l+1] += 1
		if l != 0 and k != x-1 and o[k+1][l-1] != 'B': o[k+1][l-1] += 1
		if l != y-1 and k != 0 and o[k-1][l+1] != 'B': o[k-1][l+1] += 1

elif answ == "load":
	f = open('save.json', 'r')
	data = json.load(f)
	o = data['matrix']
	r = data['usermatrix']
	x = data['height']
	y = data['width']
	q = data['bombs']
	print('Загружено!')
	f.close()

while True:
	clear()
	vivod(r)
	try:
		n,m = map(int, input('Введите координаты (например 2 3) >>> ').split(' '))
	except:
		continue;
	if n > x or m > y or n <= 0 or m <= 0:
		continue;
	m -= 1
	n -= 1
	if r[m][n] != '*' and r[m][n] != 'P':
		print('Вы уже туда ходили!')
		continue;
	try:
		answ = int(input('Кнопка действия: 0 - ничего не делать или убрать флажок, \n1 - поставить флажок, 2 - сохранить и выйти. >>> '))
	except:
		continue;
	if answ == 0:
		if r[m][n] == 'P':
			r[m][n] = '*'
			if o[m][n] == 'R':
				o[m][n] = 'B'
			continue;
	if answ  == 1:
		r[m][n] = 'P'
		if o[m][n] == 'B':
			o[m][n] = 'R'
		coun1 = 0
		coun2 = 0
		for i in range(x):
			for j in range(y):
				if r[i][j] == 'P':
					coun1 += 1
				if o[i][j] == 'R':
					coun2 += 1
		if coun1 == coun2 and coun1 == q:
			clear()
			vivod(r)
			print('Вы выиграли! Поздравляем!')
			break;
		continue;
	elif answ == 2:
		dic = {
			'matrix':o,
			'usermatrix':r,
			'height':x,
			'width':y,
			'bombs':q
			}
		saving(dic)
		print('Сохранено!')
		break;
	if o[m][n] == 'B':
		vivod(o)
		print('Вы проиграли!')
		break;
	r[m][n] = o[m][n]
	o[m][n] = '*'

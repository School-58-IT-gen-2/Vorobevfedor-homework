import json

def saving(arg):
    with open('save.json', 'w') as js:
        json.dump(arg, js)
        js.close()


answ = input('Привет! ')
if answ == 'y':
    answ = input('')
    dic = {
        "save1": answ
    }
    saving(dic)
    
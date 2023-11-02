def head_smash(arr):
    if arr != [] and arr != '':
        if not isinstance(arr, int):
            arra = []
            for x in arr:
                y = x.replace('O', ' ')
                arra.append(y)
            return arra
        else:
            return 'This isn\'t the gym!!'
    else:
        return 'Gym is empty'
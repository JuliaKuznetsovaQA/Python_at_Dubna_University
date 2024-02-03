_list = list(map(int, input().split()))
for i in range((len(_list)-1)):
    if (_list[i] * _list[i+1]) > 0:
        print(_list[i], _list[i+1])
        break

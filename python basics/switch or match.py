def switch(val):
    match val:
        case 1:
            return 1
        case 2:
            return 'test'
        case 3:
            return 6
        case _:
            return 'gahaha'
print(switch(3))
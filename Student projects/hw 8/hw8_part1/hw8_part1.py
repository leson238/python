import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist

name = input("Please type in the json file name: ")
active_bears = []
active_tourists = []
try:
    with open(name) as f:
        data = json.loads(f.read())
        field = BerryField(data["berry_field"])
        field_map = field.grid
        for bear in data["active_bears"]:
            b = Bear(bear[0], bear[1], bear[2])
            active_bears.append(b)
            if b.row < 0 or b.row > field.w:
                continue
            else:
                field_map[b.row][b.col] = 'B'
        for t in data["active_tourists"]:
            t = Tourist(t[0], t[1])
            active_tourists.append(t)
            if field_map[t.row][t.col] == 'B':
                field_map[t.row][t.col] = 'X'
            else:
                field_map[t.row][t.col] = 'T'
        print(field)
        print("Active Bears: ")
        for bear in active_bears:
            print(bear)
        print()
        print("Active Tourists: ")
        for tourist in active_tourists:
            print(tourist)
except FileNotFoundError:
    print("Wrong file name")

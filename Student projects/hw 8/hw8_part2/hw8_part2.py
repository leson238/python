import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist


class Turn:
    def __init__(self, berry_field, bear_list, tourist_list):
        self.field = berry_field
        self.bear_list = bear_list
        self.tourist_list = tourist_list
        self._update()

    def turn_passed(self):
        self.field.grow()
        self.field.spread()
        for b2 in self.bear_list:
            l = b2.walk(self.field)
            if l:
                for t in self.tourist_list:
                    if (t.row, t.col) == l:
                        t.disappear = True
        for tourist in self.tourist_list:
            tourist.should_run(self.field)
            if tourist.go_home:
                self.field.grid[tourist.row][tourist.col].tourist = False

        self.field.total_berries = self.field._total()
        return True

    def _update(self):
        for b1 in self.bear_list:
            self.field.grid[b1.row][b1.col].bear = True
        for t1 in self.tourist_list:
            self.field.grid[t1.row][t1.col].tourist = True

    def pprint(self):
        if len(self.bear_list) > 0:
            for x in [b for b in self.bear_list if (b.out_of_map)]:
                print(x)
        if len(self.tourist_list) > 0:
            for x in [t for t in self.tourist_list if (t.go_home or t.disappear)]:
                print(x)
        print(self.field)
        self.bear_list = [b for b in self.bear_list if not b.out_of_map]
        print('Active bears: ')
        if len(self.bear_list) > 0:
            for bear in self.bear_list:
                print(bear)
        print()
        self.tourist_list = [
            t for t in self.tourist_list if not (t.go_home or t.disappear)]
        print('Active tourist: ')
        if len(self.tourist_list) > 0:
            for t in self.tourist_list:
                print(t)
        print()
        self._update()


name = input("Please type in the json file name: ")
active_bears = []
reserve_bears = []
active_tourists = []
reserve_tourists = []
try:
    with open(name) as f:
        data = json.loads(f.read())
        field = BerryField(data["berry_field"])
        for bear in data["active_bears"]:
            b = Bear(bear[0], bear[1], bear[2])
            active_bears.append(b)
        for bear in data["reserve_bears"]:
            b = Bear(bear[0], bear[1], bear[2])
            reserve_bears.append(b)
        for t in data["active_tourists"]:
            t = Tourist(t[0], t[1])
            active_tourists.append(t)
        for t in data["reserve_tourists"]:
            t = Tourist(t[0], t[1])
            reserve_tourists.append(t)
        turn = Turn(field, active_bears, active_tourists)
        print("Starting Configuration")
        turn.pprint()
        turn.turn_passed()
        for i in range(5):
            print(f"Turn: {i+1}")
            turn.pprint()
            turn.turn_passed()
except FileNotFoundError:
    print("Wrong file name")

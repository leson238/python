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
        self.discard_bear = []
        self.discard_tourist = []

    def turn_passed(self):
        self.field.grow()
        self.field.spread()

        for b2 in self.bear_list:
            b2.walk(self.field)
        for t in self.tourist_list:
            t.should_run(self.field)
        self.field.total_berries = self.field.total()
        return True

    def _update(self):
        for b1 in self.bear_list:
            self.field.grid[b1.row][b1.col].bear = b1
        for t1 in self.tourist_list:
            self.field.grid[t1.row][t1.col].tourist = t1

    def update(self):
        self.discard_tourist = [t for t in self.tourist_list if (
            t.go_home or t.disappear)]
        self.discard_bear = [b for b in self.bear_list if (b.out_of_map)]
        if len(self.discard_tourist) > 0:
            for x in self.discard_tourist:
                self.field.grid[x.row][x.col].tourist = None
        self.bear_list = [
            b for b in self.bear_list if not (b.out_of_map)]
        self.tourist_list = [
            t for t in self.tourist_list if not (t.go_home or t.disappear)]
        self._update()

    def fprint(self):
        for x in self.discard_bear:
            print(x)
        for x in self.discard_tourist:
            print(x)
        self.discard_bear = []
        self.discard_tourist = []

    def pprint(self):
        discard_tourist = [t for t in self.tourist_list if (
            t.go_home or t.disappear)]
        discard_bear = [b for b in self.bear_list if (b.out_of_map)]
        for x in discard_tourist:
            self.field.grid[x.row][x.col].tourist = None
            print(x)
        for x in discard_bear:
            print(x)
        print(self.field)
        self.bear_list = [b for b in self.bear_list if not b.out_of_map]
        self.tourist_list = [
            t for t in self.tourist_list if not (t.go_home or t.disappear)]
        print('Active bears: ')
        if len(self.bear_list) > 0:
            for bear in self.bear_list:
                print(bear)
        print()
        print('Active tourist: ')
        if len(self.tourist_list) > 0:
            for t in self.tourist_list:
                print(t)
        print()


name = input("Please type in the json file name: ")
active_bears = []
reserve_bears = []
active_tourists = []
reserve_tourists = []
try:
    with open(name) as f:
        data = json.loads(f.read())
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
        field = BerryField(data["berry_field"],
                           data["active_bears"], data["active_tourists"])
        turn = Turn(field, active_bears, active_tourists)
        print("Starting Configuration")
        turn.pprint()
        turn.turn_passed()
        i = 1
        while True:
            have_new_bear = False
            have_new_tourist = False
            print(f'Turn : {i}')
            if len(reserve_bears) > 0 and turn.field.total_berries >= 500:
                new_bear = reserve_bears.pop(0)
                turn.bear_list.append(
                    new_bear)
                have_new_bear = True
            turn.update()
            turn.fprint()
            if len(turn.bear_list) > 0 and len(reserve_tourists) > 0:
                new_tourist = reserve_tourists.pop(0)
                turn.tourist_list.append(
                    new_tourist)
                have_new_tourist = True
            if len(reserve_bears) == 0 and len(turn.bear_list) == 0:
                turn.pprint()
                break
            if len(turn.bear_list) == 0 and turn.field.total_berries == 0:
                turn.pprint()
                break
            if have_new_bear:
                print(f'{turn.bear_list[-1]} - Entered the field')
            if have_new_tourist:
                print(f'{turn.tourist_list[-1]} - Entered the field')
            if i % 5 == 0:
                turn.pprint()
            # turn.pprint()
            turn.turn_passed()
            i += 1
            print()
except FileNotFoundError:
    print("Wrong file name")

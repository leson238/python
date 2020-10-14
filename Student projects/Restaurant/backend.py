class Restaurant:
    def __init__(self, name, address, average_price, distance, nationality):
        self.name = name
        self.address = address
        self.average_price = average_price
        self.distance = distance
        self.nationality = nationality

    def __str__(self):
        return f"{self.name} : {self.address} {self.average_price}$ {self.distance} miles {self.nationality}"


class Restaurants:
    def __init__(self):
        self._add_restaurant()

    def _add_restaurant(self):
        self.restaurant_list = []
        with open('restaurants.txt', 'r') as f:
            while True:
                line = f.readline()
                try:
                    name, address, price, distance, nationality = line.split(
                        ',')
                    price = float(price)
                    distance = float(distance)
                    self.restaurant_list.append(Restaurant(
                        name, address, price, distance, nationality))
                except ValueError:
                    break

    def view(self):
        return self.restaurant_list

    def search_by_location(self, n=3):
        sort_by_location = sorted(
            self.restaurant_list, key=lambda x: x.distance)
        return sort_by_location[:min(n, len(sort_by_location))]

    def search_by_price(self, n=3, lowest=True):
        sort_by_price = sorted(self.restaurant_list,
                               key=lambda x: x.average_price)

        if lowest:
            return sort_by_price[:min(n, len(sort_by_price))]
        return sort_by_price[-min(n, len(sort_by_price)):]

    def search(self, name, address, avgp, distance, nation):
        result = []
        if name:
            result += [r for r in self.restaurant_list if (
                name.lower() in r.name.lower())]
        if address:
            if result:
                result = [r for r in result if (
                    address.lower() in r.address.lower())]
            else:
                result += [r for r in self.restaurant_list if (
                    address.lower() in r.address.lower())]
        if nation:
            if result:
                result = [r for r in result if (
                    nation.lower() in r.nationality.lower())]
            else:
                result += [r for r in self.restaurant_list if (
                    nation.lower() in r.nationality.lower())]
        if avgp:
            if result:
                result = [r for r in result if r.average_price <=
                          float(avgp)]
            else:
                result += [r for r in self.restaurant_list if r.average_price <=
                           float(avgp)]
        if distance:
            if result:
                result = [r for r in result if r.distance <=
                          float(distance)]
            else:
                result += [r for r in self.restaurant_list if r.distance <=
                           float(distance)]
        return list(set(result))

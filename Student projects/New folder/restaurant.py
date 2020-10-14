"""
Class Restaurant
"""


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

    """
    Load information restaurant from csv file
    """

    def _add_restaurant(self):
        # The list of restaurant
        self.restaurant_list = []
        with open('restaurant.csv', 'r') as f:
            # Reading the first line for title
            line = f.readline()
            line_number = 1
            while True:
                line = f.readline()
                if line == "":
                    break
                line_number += 1
                try:
                    # Split each field by delim ',', and store into variable
                    name, address, price, distance, nationality = line.split(
                        ',')
                    price = float(price)
                    distance = float(distance)
                    # Create object Restaurant, and push into the list
                    self.restaurant_list.append(Restaurant(
                        name, address, price, distance, nationality))
                except ValueError:
                    print(f"Wrong input format at {line_number}")
                    pass
    """
    Method view: See all information restaurants.
    Return: string information of list's restaurant
    """

    def view(self):
        return self.restaurant_list
    """
    Method search_by_location: Search 3 (by default) nearest restaurant
    Args:
        n: Number of selection restaurant.
    Return:
        The list of 3 nearest restaurant.
    """

    def search_by_location(self, n=3):
        # Calling sorted function to sort by object
        sort_by_location = sorted(
            self.restaurant_list, key=lambda x: x.distance)
        # Slicing the list to get result
        return sort_by_location[:min(n, len(sort_by_location))]

    """
    Method search_by_price: Search 3 (by default) lowest/highest price
    restaurant.
    Args:
        n:      Number of selection restaurant
        lowest: Search lowest by default.
    Return:
        The list of 3 lowest/highest price restaurant
    """

    def search_by_price(self, n=3, lowest=True):
        sort_by_price = sorted(self.restaurant_list,
                               key=lambda x: x.average_price)
        # Search by lowest price
        if lowest:
            return sort_by_price[:min(n, len(sort_by_price))]
        # Search by highest price
        return sort_by_price[-min(n, len(sort_by_price)):]

    """
    Method search: general search based on input
    Args:
        name:     Restaurant name
        address:  Restaurant address
        avgp:     Restaurant average price
        distance: Restaurant distance
        nation:   Restaurant nation
    Return:
        The list of result restaurant by searching
    """

    def search(self, name, address, avgp, distance, nation):
        result = []
        if name:
            # Search restaurant by looking the name if they are match
            result += [r for r in self.restaurant_list if (
                name.lower() in r.name.lower())]
        if address:
            # Search by address by looking address if they are match
            if result:
                # Prefer to look into result
                result = [r for r in result if (
                    address.lower() in r.address.lower())]
            else:
                # Look into restaurant list
                result += [r for r in self.restaurant_list if (
                    address.lower() in r.address.lower())]
        if nation:
            # Search by nationality
            if result:
                # Prefer to look into result
                result = [r for r in result if (
                    nation.lower() in r.nationality.lower())]
            else:
                # Look into restaurant list
                result += [r for r in self.restaurant_list if (
                    nation.lower() in r.nationality.lower())]
        if avgp:
            # Search by price
            if result:
                # Prefer to look into result
                result = [r for r in result if r.average_price <=
                          float(avgp)]
            else:
                # Look into restaurant list
                result += [r for r in self.restaurant_list if r.average_price <=
                           float(avgp)]
        if distance:
            # Search by distance
            if result:
                # Prefer to look into result
                result = [r for r in result if r.distance <=
                          float(distance)]
            else:
                # Look into restaurant list
                result += [r for r in self.restaurant_list if r.distance <=
                           float(distance)]
        return list(set(result))


r = Restaurants()
print(len(r.restaurant_list))

class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):

    if self.start_time > 12:
      string = "{} menu available from {}pm to {}pm".format(self.name, self.start_time  % 12, self.end_time % 12)

    elif self.start_time <= 12 and self.end_time > 12:
      string = "{} menu available from {}am to {}pm".format(self.name, self.start_time % 12, self.end_time % 12)

    else:
      string = "{} menu available from {}am to {}am".format(self.name, self.start_time % 12, self.end_time % 12)
  
    return string


  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price += self.items[item]

    return total_price


class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self,time):
    available_menus = [menu for menu in self.menus if menu.start_time <= time <= menu.end_time]
    return available_menus

class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises
  

brunch = Menu("brunch",{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50,'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

early_bird = Menu("Early-bird Dinners",{'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)

dinner = Menu("dinner",{'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)

kids = Menu("kids",{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

flagship_store = Franchise("1232 West End Road",[brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street",[brunch, early_bird, dinner, kids])

print(flagship_store)

print(brunch)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

# Our first business
first_business = Business("Basta Fazoolin' with my Heart", [flagship_store,new_installment])

print(first_business)

# Menu of Franchise called Take a' Arepa from 10am until 8pm
arepas_menu = Menu("Take a' Arepa",{'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50},10,20)

# Create our first Take a' Arepa franchise
arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])
arepas_business = Business("Take a' Arepa",arepas_place)

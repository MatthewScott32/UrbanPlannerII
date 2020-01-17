from buildings import Building
from city import City

building_1 = Building("101 Avenue", "5")
building_2 = Building("102 Avenue", "6")
building_3 = Building("103 Avenue", "7")
building_4 = Building("104 Avenue", "8")
building_5 = Building("105 Avenue", "9")

block = [building_1, building_2, building_3, building_4, building_5]

for building in block:
    print(f'{building.address} acquired by {building.owner} on {building.date_constructed} and has {building.stories} stories.')
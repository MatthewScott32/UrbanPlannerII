from buildings import Building

class City:
    def __init__(self, name, mayor, year_est, all_buildings):
        self.name = name
        self.mayor = mayor
        self.year_est = year_est
        self.all_buildings = list()
    
    def new_building(self):
        self.all_buildings.append()

building_1 = Building("101 Avenue", "5")
building_2 = Building("102 Avenue", "6")
building_3 = Building("103 Avenue", "7")
building_4 = Building("104 Avenue", "8")
building_5 = Building("105 Avenue", "9")

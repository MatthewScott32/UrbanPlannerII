import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = 1 
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, purchase):
        self.owner = purchase 
 
building_1 = Building("101 Avenue", "5")
building_2 = Building("102 Avenue", "6")
building_3 = Building("103 Avenue", "7")
building_4 = Building("104 Avenue", "8")
building_5 = Building("105 Avenue", "9")

block = [building_1, building_2, building_3, building_4, building_5]

building_1.purchase("Jim")
building_2.purchase("James")
building_3.purchase("Jimmy")
building_4.purchase("Willy")
building_5.purchase("Billy")


#for building in block:
 #   building.construct()
  #  print(f'{building.address} acquired by {building.owner} on {building.date_constructed} and has {building.stories} stories.')

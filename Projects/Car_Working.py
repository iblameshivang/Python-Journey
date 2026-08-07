class Engine:
    metal="Titanium"
    @staticmethod
    def engine_starts():
        print("um ummm ummmmmmmmm ummmmmmmmmmmmmmmmm")
    def engine_stops(self):
        print('ummmmmmmmmmmmmmm ummmmmmmmm ummm um')  
    def engine_revv(self):
        print("Raaatatatatta bumb buuub shiii' hell'") 

class Cars(Engine):
    def __init__(self,Car,Engine_Name,HP,cost):
        self.Car=Car
        self.Engine_Name=Engine_Name
        self.HP=HP
        self.cost=cost

Car1=Cars("Audi A4","V6","746HP","1Cr")
print("\n",Car1.Car, "have the",Car1.Engine_Name, "engine that can produce", Car1.HP, "and cost around", Car1.cost)
print("----------------------------------------------------------------")
print("This is how Car sounds like  when it Starts...")
Car1.engine_starts()
print("\n")
print("This is how Car sounds like  when it got Reved hard...")
Car1.engine_revv()
print("\n")
print("This is how Car sounds like  when it Stops...")
Car1.engine_stops()
print("\n")
print("====================================================================")
Car2=Cars("Supra","V12","1000HP","2Cr")
print("\n",Car2.Car, "have the",Car2.Engine_Name, "engine that can produce", Car2.HP, "and cost around", Car2.cost,"and it is made up of", Engine.metal)
print("----------------------------------------------------------------")
print("This is how Car sounds like  when it Starts...")
Car2.engine_starts()
print("\n")
print("This is how Car sounds like  when it got Reved hard...")
Car2.engine_revv()
print("\n")
print("This is how Car sounds like  when it Stops...")
Car2.engine_stops()
print("\n")
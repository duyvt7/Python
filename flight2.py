class flight ():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passenger = []
    def add(self,name):
        if not self.seat():
            return False
        else:
            self.passenger.append(name)
            return True
    def seat(self):
        return self.capacity - len(self.passenger)

f=flight(3)
names = ["naruto", "sasuke", "sakura","itachi"]
for name in names:
    if f.add(name) == True:
        print(f"add passenger {name} to the flight")
    else:
        print(f"there is no seat for {name}")
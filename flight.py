class flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passenger = []
    def add (self, name):
        if not self.seat():
            return False
        else:
            self.passenger.append(name)
            return True
    def seat (self):
        return self.capacity - len(self.passenger)


f= flight(3)
people = ["naruto", "sasuke", "sakura", "itachi"]
for person in people:
    if f.add(person) == True:
        print(f"add {person} successful")
    else:
        print(f"there is no seat for {person}")

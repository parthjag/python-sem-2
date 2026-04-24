class vehicle:
  def move(self):
    print("Vehicle is moving")
    
class Car(vehicle):
  def move(self):
    print("driving on the road") 
    
class Bicycle(vehicle):
  def move(self):
    print("pedalling on the road")    
    
vehicles=[Car(),Bicycle()]

for v in vehicles:
  v.move()
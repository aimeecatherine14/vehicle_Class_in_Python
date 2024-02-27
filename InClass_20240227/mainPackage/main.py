# main.py
# Add an import statement for Vehicle class
from vehicleClass.vehicle import *

if __name__ == "__main__":
    # Instantiate an object if type Vehicle
    myCorvette = Vehicle("Car", 120) # Trigger a call to constructor.
    myCorvette.printType()  # Invoke the method on the object
    
    # Invoke the getter for the maximum speed, store the return, value in a variable 
    # Print that to the console
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    # Instantiate another Vehicle object. You can name it
    myCorolla = Vehicle("Car") # myCorolla is an object of the vehicle type 
    
    
    # I want a list of 3 Vehicles: Car, Boat, Space Ship
    # You can pick the names and properties
    # I want some friendly output to demo your work
    myVehicles = [  Vehicle("Toyota Camry", 150)
                  , Vehicle("sailboat", 20)
                  , Vehicle("Falcon Heavy", 4000)]
    
    # iterate  over the list
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
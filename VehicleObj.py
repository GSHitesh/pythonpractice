# importing class individually from a module Vehicle.py
from Vehicle import Vehicle, Car,Motorcycle

# import an entire Module
# import Vehicle {file_name}

# importing all classes from the module
# Not Recommeded approach
# from Vehicle import *

# V1= Vehicle("Tesla","white")
# # print(V1)

# C1 = Car("Maruti","grey",4)
# print(C1)

# C1.start_engine(C1)
# C1.add_fuel(0)
# c2 = Vehicle("Honda","Black")   # Initialize the child object with base class
# c2.add_fuel(5)
# C1.add_fuel(15)
# C1.add_fuel(5)
# C1.honk()

vehicle_1 = Vehicle("Royal Enfield","Red")
motorcycle_1 = Motorcycle("125cc",vehicle_1)
motorcycle_1.start()

car_list = []

for _ in range(10):
    car_obj_1 = Car("Kia","Orange","2")

    car_list.append(car_obj_1)

for car in car_list:
    print(car)

print(len(car_list))

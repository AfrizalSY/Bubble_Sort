import random
import List

# generate random n item list
def listGenerator(n):
    arr = []
    for _ in range(n):
        arr.append(random.randint(1,1700))
    return arr

List.SaveList("list6.dat",listGenerator(1000))


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print(self):
        print(" (",self.x," , ",self.y,") ",end=" ")


def sortbyX(val):
    return val.x;

def sortbyY(val):
    return val.y;


def sort(arr,coordinate,r):
     if(coordinate=='x'):
        arr.sort(key=sortbyX,reverse=r)
     else:
         arr.sort(key=sortbyY, reverse=r)


def printPoints(a):
    for i in range (len(a)):
        a[i].print()
    print()


def ClosestPairs(a):

    #sorted by x coordinates
    sort(a,'x',False)
    printPoints(a)

    #sorted by y coordinates
    sort(a,'y',False)
    printPoints(a)





def main():
    a = [Point(1,3),Point(11,2),Point(1,5),Point(5,3),Point(6,5),Point(12,3)]
    printPoints(a)
    ClosestPairs(a)





main()


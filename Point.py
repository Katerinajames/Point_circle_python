import math 
class Point:
	def __init__(self,x,y):
		 self.x=x
		 self.y=y

print("-----------------------------")


class Circle(Point):
	def __init__(self,x,y,radiusvalue):
		Point.__init__(self,x,y)
		self.radiusvalue=radiusvalue
	def area (self):	
	   return math.pi*self.radiusvalue
	
print("------------------------------------")

p=Circle(2,3,5.2)

print ("The area of the circle is %.3f" % (p.area()))

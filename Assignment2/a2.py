from polygon import Polygon, find_point

class Example(Polygon):
	def __init__(self, angle):
		super().__init__()
		self._angle = angle

	def get_points(self):
		start = (100, 100)
		points = [start]

		next_point = find_point(start, self._angle, 100)
		points.append(next_point)

		next_point = find_point(next_point, 1.5 * self._angle, 150)
		points.append(next_point)

		points.append((-100, -100))
		points.append((0, 100))

		return points

class Rectangle(Polygon):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def get_points(self):
		points = [[0,0],[self.a,0],[0,self.b],[self.a,self.b]]
		return points
	
class Square(Rectangle):
	def __init__(self, a):
		super().__init__(a,a)
"""
class Fraction:
	def __init__(self, n, d):
		self.n = n
		self.d = d
	#def simplify(self):

	def add(self, other):
		self.n = (other.n*self.n)+(self.d*other.n)
		self.d = (other.d*self.d)
	#self.simplify()

class Compound:
	def __init__(self, w, f):
		self.w = w
		self.f = f

	def add(self, other):
		self.w += other.w
		self.f.add(other.f)
	#	self.simplify()
"""

def main():
#	a = Example(101)
#	a.draw()

#	b = Example(201)
#	b.draw()

	r = Rectangle(2,4)
	r.draw()
"""
	a = Fraction(1,2)
	b = Fraction(2,3)
	a.add(b)
	
	c = Compound(1,a)
	d = Compound(2,b)
	c.add(d)
"""



if __name__ == '__main__':
	main()

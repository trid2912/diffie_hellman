import random

class A:
	def __init__(self, n, g, p):
		# Generating a random private number selected by alice
		self.n = n
		self.g = g
		self.p = p
	def publish(self):
		# generating public values
		return (self.g**self.n)%self.p

	def compute_secret(self, gb):
		# computing secret key
		return (gb**self.n)%self.p


class B:
	def __init__(self,g,p):
		# Generating a random private number selected for alice
		self.a = random.randint(1, p)
		# Generating a random private number selected for bob
		self.b = random.randint(1, p)
		self.arr = [self.a,self.b]
		self.g = g
		self.p = p
	def publish(self, i):
		# generating public values
		return (self.g**self.arr[i])%self.p

	def compute_secret(self, ga, i):
		# computing secret key
		return (ga**self.arr[i])%self.p



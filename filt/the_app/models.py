from django.db import models


class Product:
	"""Stores information about a product and where we found it."""
	def __init__(self, source):
		self.source = source
		self.name   = None
		self.price  = None
		self.url    = None
		self.imgurl = None

		self.parent = None # will link to the reliance product
		self.reviews = []

	def __repr__(self): return f'Product({self.name!r}, {self.url!r})'

	def link(self, other):
		'''`self` is the reliance product'''
		other.parent = self

class Review:
	"""Stores information about a review and where it was made."""
	def __init__(self, product):
		self.product = product
		#product.reviews.append(self)

		self.date     = None
		self.title    = None
		self.stars    = None
		self.review   = None
		self.reviewer = None
		self.upvotes  = ''


	def __repr__(self): return f'Review({self.reviewer[:20]+(self.review[20:]and"...")})'

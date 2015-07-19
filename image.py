class Image(object):
	"""docstring for Image"""
	def __init__(self, name, dist):
		super(Image, self).__init__()
		self.name = name
		self.dist = dist
	def __cmp__(self, other):
		return self.dist < other.dist
	def __unicode__(self):
		return self.name + ':' + str(self.dist)
	def __str__(self):
		return unicode(self).encode('utf-8')
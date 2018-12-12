class clas1:
	def __init__(self,v1,v2):
		print('clas1 init')
		self.v1=v1
		self.v2=v2
	def put_dir(self):
		#print(__name__)
		print(dir(self))
	def fun(self):
		print('clas1 fun()')

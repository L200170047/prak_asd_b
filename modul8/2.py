class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.item=[]

	def isEmpty(self):
		return len(self)==0

	def __len__(self):
		return len(self.item)

	def peek(self):
		assert not self.isEmpty(), "Stack is Empty"
		return self.item[-1]

	def pop(self):
		assert not self.isEmpty(), "Stack is Empty"
		return self.item.pop()

	def push(self, data):
		self.item.append(data)

nilai=Stack()
for i in range(16):
	if i % 3==0:
		nilai.push(i)
	print(str(i) + ":" + str(nilai.peek()))

#Untuk setiapi dengan range 16 yaitu dari angka 0 samapai 15 akan dicek terlebih dahulu.
#Jika i dibagi 3 modulnya adalah 0, maka nilai dari i akan ditambahkan atau di push ke
#dalam stack. Angka dalam stack adalah 0, 3, 6, 9, 12, 15.

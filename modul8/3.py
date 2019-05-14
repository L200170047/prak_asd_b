class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.item=[]

	def isEmpty(self):
		return (len(self.item))==0

	def __len__(self):
		return len(self.item)

	def peek(self):
		if self.isEmpty() == True:
			return None
		else:
			return self.item[-1]

	def pop(self):
		if self.isEmpty() == True:
			print("Stack is Empty")	
		else:
			return self.item.pop()

	def push(self, data):
		self.item.append(data)

nilai=Stack()
for i in range(16):
	if i % 3==0:
		nilai.push(i)
	if i % 4==0:
		nilai.pop()
	print(str(i) + ":" + str(nilai.peek()))

#Untuk setiap i dengan range 16 yaitu dari angka 0 sampai 15 akan dicek terlebih dahulu.
#Jika i dibagi 3 modulnya adalah 0, maka nilai dari i akan ditambahkan atau di push ke
#dalam stack. Namun jika syarat ini tidak terpenuhi, maka akan mengeksekusi jika i dibagi
#4 modul 0 dengan hasil nilai yang berada dalam stack akan dipop atau diambil (dihapus).
#Angka dalam stack menjadi 0, 9, 12, 15.

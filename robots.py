class Product:
	def __init__(self, name, price,count,tax):
		self.name = name
		self.price = price
		self.count = count
		self.tax = tax

	def price_with_tax(self):
		total = self.price * self.count *self.tax
		if total > 500:
			return 0.9 * total
		else:
			return total

products = [
	Product(name="robot", price=900, count=2, tax=1.25), 
	Product(name="book", price=100, count=1, tax=1.06), 
	Product(name="sticker", price=10, count=1, tax=1.25)
	]

total_price = 0
for p in products:
	total_price = total_price + p.price_with_tax()
	print (p.name, p.price_with_tax())

print(
	"Totalt:", total_price
	)
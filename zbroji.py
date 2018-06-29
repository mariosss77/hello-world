# Simple python file

# New branch, adding decorator 
def decorator(func):
	def wrapper(x, y):
		print(f'Result is: {func(x, y)}')

	return wrapper
@decorator
def mnozi(x, y):
	return x * y


zbroji = lambda x, y: x + y
oduzmi = lambda x, y: x - y

if __name__ == '__main__':
	print(f'Zbroj: {zbroji(12, 10)}, razlika: {oduzmi(21, 12)},')
	mnozi(32, 100)
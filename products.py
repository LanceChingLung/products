#檢查檔案
import os #operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f: #讀取檔案
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name =='q': #quit
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
	print(products)
	return products

#列印所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])
#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		products = read_file(filename)
		print('有此檔案! ')
	else:
		print('此檔案不存在!')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
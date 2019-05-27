#檢查檔案
import os #operating system

products = []

if os.path.isfile('products.csv'):
	print('有此檔案! ')
	with open('products.csv', 'r', encoding = 'utf-8') as f: #讀取檔案
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('此檔案不存在!')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name =='q': #quit
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

#列印所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
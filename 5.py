# 5. Өгөгдсөн тоон жагсаалтаас хамгийн их болон хамгийн бага утгуудыг буцаах функц бич.

list = []

n = int(input("Elementiin too : "))

for i in range(0, n):
	e = int(input())
	list.append(e)

def max_min():
    return [max(list), min(list)]
    
print (max_min())
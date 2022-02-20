# 4. Өгөгдсөн тоон жагсаалтын 3 дахь элементийг сүүлийн сүүлийн элементтэй үржүүлэн үр дүнг буцаадаг функц бич.

list = []

n = int(input("Elementiin too : "))

for i in range(0, n):
	e = int(input())
	list.append(e)

def urjver():
    return list[2] * list[len(list) - 1]
    
print (urjver())
	


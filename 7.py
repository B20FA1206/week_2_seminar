# 7. Өгөгдсөн жагсаалтаас давхардсан утгуудыг арилгаж, хэвлэ.

list = []
n = int(input("Elementiin too : "))
for i in range(0, n):
    e = input()
    list.append(e)

result = [] 
for i in list: 
    if i not in result: 
        result.append(i) 

print (result)
# 6. Өгөгдсөн жагсаалтаас хоёроос дээш оронтой, эхний болон төгсгөлийн тэмдэгтүүд нь хоорондоо адилхан гишүүн хэд байгааг тоолох функц бич.

lst = []
n = int(input("Elementiin too : "))
count = 0;
for i in range(0, n):
    e = str(input())
    lst.append(e)

for x in range(len(lst)):
    if (len(lst[x]) > 2):
        if (lst[x][0] == lst[x][-1]):
            count+= 1

print(count)
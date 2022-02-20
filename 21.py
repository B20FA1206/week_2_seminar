# 21. Key, value нь тоон утга бүхий dictionary үүсгэж өсөх болон буурахаар эрэмбэл.

dict = {
  1 : 1,
  2: 2,
  3: 3
}

for x, y in dict.items():
    print(x, y)

for x, y in reversed(dict.items()):
    print(x, y)
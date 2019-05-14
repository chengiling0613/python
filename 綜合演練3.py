pw = input("請輸入月份:")
if(int(pw) >= 10):
    print(pw + "月是冬天")
elif(int(pw) >= 7):
    print(pw + "月是秋天")
elif(int(pw) >= 4 ):
    print(pw + "月是夏天")
elif(int(pw) >= 1):
    print(pw + "月是春天")
else:
    print("不再範圍內")
    
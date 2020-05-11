ticket = 1 
knifelength = 15
# 当进入火车站时进行安检
# if 判断条件
if ticket == 1:
    print("通过车票的检查，进入火车站，安检")
    #判断刀子的长度是否合法，合法则进入候车大厅；反之不合法，等待处理
    if knifelength <= 10:
        print("通过安检，进入候车大厅")
    else:
        print("刀子的长度不合法，等待处理")
# 当if条件不成立时，即没有车票
    print("兄弟，你还没车票")

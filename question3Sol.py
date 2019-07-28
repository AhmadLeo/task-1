lst = (range(1500,2701))
lstNew = []
for i in lst:
       if(i % 5 == 0 and i % 7 == 0):
           lstNew.append(i)
print(lstNew)

#3.feladat:	Írd ki a -200 és 150 közötti minden ötödik számot egy sorba kukac jelel elválasztva. (ne egyesével gépeld be őket, az nem jó megoldás!) A megoldásodat for-al és while-al is valósítsad meg!

for szam in range(-200, 151, 5):
    print(str(szam),end=' @')

#i = -200
#while i < 151:
 #   i =+ 5
#    print(str(i),end=' @')
i = -200
while i < 151:
  print((i),end=' @')
  if i == 151:
    break
  i += 5


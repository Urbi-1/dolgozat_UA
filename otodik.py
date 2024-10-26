#5.feladat:	Írd ki a 60 és -70 közötti számokat vesszővel elválasztva egy sorba, úgy hogy az utolsó után ne legyen vessző. A tanult két fajta módon is valósítsad meg a programod.


for szam in range(60, -71, -1):
    print(str(szam),end=' ,')

i = -70
while i < 60:
    print(i)
    i += 1
    print(str(i),end=' ,')


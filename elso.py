#1.feladat:	Írd ki a sorozat első 10 elemét. Az olyan számokat, amelyek felírhatók   alakban, ahol k egy pozitív egész szám, Kynea-számoknak nevezzük. A Kynea-számok sok esetben prímek. Például k=0; 1; 2; 3; 5; 8; 9; 12; 15; 17; 18; 21; 23; 27; 32; 51…. esetén.
#A 22 legkisebb Kynea-szám: 7, 23, 79, 287, 1087, 4223, 16639, 66047, 263167, 1050623, 4198399, 16785407, 67125247, 268468223, 1073807359, 4295098367, 17180131327, 68720001023, 274878955519, 1099513724927, 4398050705407, 17592194433023
def elso():

    k= input(str("Kérem adjon meg egy vaós számot"))

    szam= (k*2+1)**2-2

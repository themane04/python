"""Aufgabe 1"""

n1 = 22
n2 = 44
n3 = 55
n4 = 88.8
s1 = "Hello"
s2 = "World"


"Aufgabe 2a"
summe = n1 + n2 + n3 + n4
mult = n1 * n2 * n3 * n4
print(summe)
print(mult)
print(n4 - n1)
"Float als Resultat"


"Aufgabe 2b"
txt = s1 + s2
"and s1 * s2 - error"
print(txt)
"Beim Addieren von Zahlen wird das Assoziativgesetz befolgt, während bei der Konkatenation von Strings die Reihenfolge "
"entscheidend ist und das Assoziativgesetz nicht im mathematischen Sinne gilt."


"Aufgabe 3"
div = n4 / n1
print(f"{div:.3f}")
"Die // Operation führt eine ganzzahlige Division durch. Das bedeutet, dass das Ergebnis der Division abgerundet wird, um eine ganze Zahl zu erhalten."
"Die % Operation ist der Modulo-Operator, der den Rest einer Division zurückgibt."


"Aufgabe 4"
"Potenzen"
print(22**3)
"Wurzel"
print(64**(1/5))
print(25**(1/3))


"Aufgabe 5"
"+resultat ist ein Fehler"
resultat = "Ben"
text = "Das erhaltene Resultat ist: " +str(resultat)
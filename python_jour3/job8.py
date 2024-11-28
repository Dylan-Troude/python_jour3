a = float(input("Veuillez entrer la première valeur : "))
b = float(input("Veuillez entrer la deuxième valeur : "))
c = float(input("Veuillez entrer la troisième valeur : "))

var_print = False

if a + b > c or a + c > b or b + c > a:
    print("Il est possible de construire un triangle.")
    
    if a == b or a == c or b == c:
        print("Ce triangle est isocèle.")
        var_print = True
    if  round(a**2, 1) == round(b**2 + c**2, 1) or round(b**2, 1) == round(a**2 + c**2, 1) or round(c**2, 1) == round(a**2 + b**2, 1):
        print("Ce triangle est rectangle.")
        var_print = True
    if a == b and b == c:
        print("Ce triangle est  équilatéral.")
        var_print = True
    if not var_print:
        print("Ce triangle est quelconque.")
        var_print = False
else:
    print(f"Il n'est pas possible de faire un triangle avec les valeurs {a}, {b}, et {c}.")




def llegir_af():
    f_automat = open("automat.txt", "r")
    canvis_estat = []

    # Es separen els estats per espais i s'elimina el salt de linia
    estats_inicials = f_automat.readline().strip("\n").split(" ")
    estats_finals = f_automat.readline().strip("\n").split(" ")

    for line in f_automat:
        canvis_estat.append(line.strip("\n").split(" "))

    f_automat.close()
    return [estats_inicials, estats_finals, canvis_estat]


def llegir_paraula(automat, paraula):
    estats_inicials = automat[0]
    estats_finals = automat[1]
    canvis_estat = automat[2]
    estats_a_llegir = estats_inicials
    estats_seguents_a_llegir = []

    # Es llegeix cada lletra de la paraula
    for lletra in paraula:
        # Per cada lletra de la paraula es mira els següents estats a llegir(s'inicialitzen amb els estats inicials)
        for estat_a_llegir in estats_a_llegir:
            # Per a cada estat a comprovar, es miren tots els canvis d'estat possibles
            for canvi_estat in canvis_estat:
                # Si un canvi d'estat coincideix amb la lletra i estat que s'estan llegint actualment, es guarda el següent estat d'aquest canvi als següents estats per a llegir
                if estat_a_llegir == canvi_estat[0] and lletra == canvi_estat[1]:
                    estats_seguents_a_llegir.append(canvi_estat[2])
        estats_a_llegir = estats_seguents_a_llegir
        estats_seguents_a_llegir = []

    # Es comparen els estats on s'ha arribat amb la paraula amb els finals, si un d'ells coincideix la paraula es acceptada
    for estat in estats_a_llegir:
        for estat_final in estats_finals:
            if estat == estat_final:
                return True
    return False


if __name__ == "__main__":
    automat = llegir_af()

    paraula = str(input("Introdueix la paraula a llegir:\n"))
    while (paraula != "-1"):
        paraula_acceptada = llegir_paraula(automat, paraula)

        if paraula_acceptada:
            print("La paraula " + paraula + " ES acceptada per l'automat")
        else:
            print("La paraula " + paraula + " NO es acceptada per l'automat")

        paraula = str(input("Introdueix la paraula a llegir o '-1' per a finalitzar:\n"))

class Hadanka:

    def __init__(self, pocet_pokusu, min_cislo, max_cislo):
        """
        Inicializuje hru

        Argumenty:
            pocet_pokusu = Počet pokusů \n
            min_cislo = Nejmenší
            možné číslo \n
            max_cislo = Největší možné číslo
        """
        self.pocet_pokusu = pocet_pokusu
        self.min_cislo = min_cislo
        self.max_cislo = max_cislo
        self.nahodne_cislo = self.generuj_nahodne_cislo()
        self.cislo_hrace = 50

        # hlavní průběh hry
        while (self.pocet_pokusu > 0) or (self.cislo_hrace != self.nahodne_cislo):
            self.generuj_nahodne_cislo()
            self.ziskej_cislo_hrace()
            print(self.vyhodnot())
            # ošetření situace kdy hráč uhodne a ještě má dostatek pokusů
            if self.cislo_hrace == self.nahodne_cislo:
                break
            self.pocet_pokusu = self.pocet_pokusu - 1
        else:
            print("Je mi líto, ale došly ti pokusy :()")

    def generuj_nahodne_cislo(self):
        # Vygeneruje náhodné číslo
        from random import randint

        return randint(self.min_cislo, self.max_cislo)

    def ziskej_cislo_hrace(self):
        # Zadání čísla od hráče
        while True:
            try:
                self.cislo_hrace = int(
                    input(f"Zadej číslo v rozsahu {self.min_cislo} až {self.max_cislo}\n")
                )
                if self.cislo_hrace in range(self.min_cislo, self.max_cislo + 1):
                    return self.cislo_hrace
                else:
                    print(
                        f"Špatně! Zadej prosím číslo v rozsahu {self.min_cislo} až {self.max_cislo}"
                    )
            except ValueError:
                print("Neplatný vstup! Musíš zadat celé číslo")

    def vyhodnot(self):
        # Porovnání obou hodnot s vyhodnocením a příp. malou nápovědou
        if self.cislo_hrace == self.nahodne_cislo:
            return "Trefa!!! Máš to!"
        elif self.cislo_hrace < self.nahodne_cislo:
            return "Zkus hádat vyšší číslo"
        elif self.cislo_hrace > self.nahodne_cislo:
            return "Zkus hádat nižší číslo"

class Hadanka:
    from random import randint

    def __init__(self, pocet_pokusu, min_cislo, max_cislo):
        """
        Inicializuje hru

        Argumenty:
            pocet_pokusu = Počet pokusů \n
            min_cislo = Nejmenší možné číslo \n
            max_cislo = Největší možné číslo
        """
        self.pocet_pokusu = pocet_pokusu - 1
        self.min_cislo = min_cislo
        self.max_cislo = max_cislo + 1
        self.nahodne_cislo = self.generuj_nahodne_cislo()
        self.cislo_hrace = 0

        # hlavní průběh hry
        print(
            "Zahrajeme si takovou hru. Budu si myslet nějaké číslo a ty budeš hádat jaké to je!"
        )
        while self.pocet_pokusu >= 0:
            self.generuj_nahodne_cislo()
            self.ziskej_cislo_hrace()
            self.vyhodnot()
            # ošetření situace kdy hráč uhodne a ještě má dostatek pokusů
            if self.cislo_hrace == self.nahodne_cislo:
                break
            self.pocet_pokusu = self.pocet_pokusu - 1
        else:
            print("Je mi líto, ale došly ti pokusy...)")

    def generuj_nahodne_cislo(self):
        """Generuje náhodné tajné číslo."""
        return self.randint(self.min_cislo, self.max_cislo)

    def ziskej_cislo_hrace(self):
        """Zadání čísla od hráče."""
        valid_value = False
        while not valid_value:
            try:
                self.cislo_hrace = int(
                    input(
                        f"Zadej číslo v rozsahu {self.min_cislo} až {self.max_cislo -1}\n"
                    )
                )
            except ValueError:
                print("Neplatný vstup! Musíš zadat celé číslo\n")
            else:
                valid_value = self.cislo_hrace in range(self.min_cislo, self.max_cislo)
                if valid_value:
                    return self.cislo_hrace
                else:
                    print(
                        f"Zadal jsi číslo {self.cislo_hrace} a to je mimo rozsah...\n"
                    )

    def vyhodnot(self):
        """Porovnání obou hodnot s výpisem a příp. malou nápovědou."""
        if self.cislo_hrace == self.nahodne_cislo:
            print("Trefa!!! Máš to!\n")
        elif self.cislo_hrace < self.nahodne_cislo:
            print(f"Zkus hádat vyšší číslo, máš ještě {self.pocet_pokusu} pokusů\n")
        elif self.cislo_hrace > self.nahodne_cislo:
            print(f"Zkus hádat nižší číslo, máš ještě {self.pocet_pokusu} pokusů\n")

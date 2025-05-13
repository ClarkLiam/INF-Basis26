from random import randint, shuffle
class Spielkarte():
    ## eigentlich nicht nötig:
    __farbe = ""
    __wert = ""
    
    def __init__(self, farbe: str, wert: str):
        self.__farbe = farbe
        self.__wert = wert

    def __repr__(self):
        return self.__farbe + self.__wert + " "
        
    def get_farbe(self):
        return self.__farbe
    
    def get_wert(self):
        return self.__wert
    
class Stapel():
    def __init__(self):
        self._karten = []
   
    def __repr__(self):
        ausgabe = ""
        for karten_index in range(len(self._karten)):
            ausgabe += f"{self._karten[karten_index]}"
        return ausgabe
    
    def hinzufuegen(self, karte):
        self._karten.append(karte)

    def get_anzahl(self):
        return len(self._karten)

    def nimm(self, index):
        if index < self.get_anzahl():
            return self._karten.pop(index)
        else:
            return None

    def ziehe1(self) -> Spielkarte:
        return self.nimm(randint(0,self.get_anzahl()-1))

    def alle_werte_gleich(self) -> bool:
        if self.get_anzahl() == 0:
            return True
        wert_temp = self._karten[0].get_wert()
        for karte in self._karten:
            if karte.get_wert() != wert_temp:
                return False
        return True

    def get_karte(self, index) -> Spielkarte:
        if index < self.get_anzahl():
            return self._karten[index]
        else:
            return None

    def mischen(self):
        shuffle(self._karten)


if __name__ == "__main__":
    meine_hand = Stapel()
    deine_hand = Stapel()
    meine_hand.hinzufuegen(Spielkarte("Herz", "A"))
    meine_hand.hinzufuegen(Spielkarte("Pik", "7"))
    deine_hand.hinzufuegen(Spielkarte("Karo", "9"))
    print(f"{meine_hand}")
    print(f"{deine_hand}")


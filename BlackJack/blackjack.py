from random import randint, shuffle
from karten import Stapel, Spielkarte
# Dies sind Listen, die nicht verändert werden sollen. Solche "Konstanten"
# werden üblicherweise mit GROSSBUCHSTABEN benannt. 
WERTE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "A"]
FARBEN = ["♠", "♥", "♦", "♣"]
    
class BlackJackSet(Stapel):
    def __init__(self):
        super().__init__()
        for _ in range(6): 
            for farbe in FARBEN:
                for wert in WERTE:
                    self.hinzufuegen(Spielkarte(farbe, wert))
        self.mischen()

        
class BlackJackHand(Stapel):
    def __init__(self):
        super().__init__()
        
    def get_punkte(self):
        punktzahl = 0
        anzahl_asse = 0
        
        for karte in self._karten:
            if karte.get_wert() in ["B", "D", "K"]:
                punktzahl += 10
            elif karte.get_wert() == "A":
                punktzahl += 11
                anzahl_asse += 1
            else:
                punktzahl += int(karte.get_wert())

            while punktzahl > 21 and anzahl_asse > 0:
                punktzahl -= 10
                anzahl_asse -= 1

        return punktzahl

    def is_bust(self):
        if self.get_punkte() > 21:
            return True
        else:
            return False

if __name__ == "__main__":
    dealer_set = BlackJackSet()
    spieler_hand = BlackJackHand()
    dealer_hand = BlackJackHand()

    ## erste Tests:
    #print(dealer_set.ziehe1())  # beliebige Karte ziehen
    #print(dealer_set.get_anzahl())  # sollten nur noch 311 Karten sein

    # Karten hinzufügen, Punkte berechnen:
    #spieler_hand.hinzufuegen(Spielkarte("♣", "7"))
    #print(spieler_hand)
    #print(spieler_hand.get_punkte())  # Muss 7 ergeben
    #spieler_hand.hinzufuegen(Spielkarte("♣", "A"))
    #print(spieler_hand.get_punkte())  # Muss 18 ergeben
    #spieler_hand.hinzufuegen(Spielkarte("♣", "5"))
    #print(spieler_hand.get_punkte())  # Muss 13 ergeben, sonst wäre 21 überschritten
    
    
#Main Game#
def game():
    dealer_set = BlackJackSet()
    spieler_hand = BlackJackHand()
    dealer_hand = BlackJackHand()

    spieler_hand.hinzufuegen(dealer_set.ziehe1())
    spieler_hand.hinzufuegen(dealer_set.ziehe1())

    dealer_hand.hinzufuegen(dealer_set.ziehe1())
    dealer_hand.hinzufuegen(dealer_set.ziehe1())
    
    print(f"Dealer: {dealer_hand.get_karte(0)} ?")
    print(f"Dealer Punkte: {dealer_hand.get_punkte()}")
    print(f"Spieler: {spieler_hand}")
    print(f"Spieler Punkte: {spieler_hand.get_punkte()}")



print("Willkommen zu BlackJack!")
game()
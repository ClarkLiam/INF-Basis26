from random import randint, shuffle
from karten import Stapel, Spielkarte
# Dies sind Listen, die nicht verändert werden sollen. Solche "Konstanten"
# werden üblicherweise mit GROSSBUCHSTABEN benannt. 
WERTE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "A"]
FARBEN = ["♠", "♥", "♦", "♣"]
    
class BlackJackSet(Stapel):
    def __init__(self):
        super().__init__()
        # AUFGABE: 6 volle Poker-Sets hinzufügen

        
class BlackJackHand(Stapel):
    def __init__(self):
        super().__init__()
        
    def get_punkte(self):
        punktzahl = 0
        # Ideale Punktzahl berechnen. Asse können als 1 oder 11 zählen!
        return punktzahl

    def is_bust(self):
        # Rückgabewert gibt an, ob die 21 überschritten wurde.
        return False

if __name__ == "__main__":
    dealer_set = BlackJackSet()
    spieler_hand = BlackJackHand()
    dealer_hand = BlackJackHand()

    ## erste Tests:
    print(dealer_set.ziehe1())  # beliebige Karte ziehen
    print(dealer_set.get_anzahl())  # sollten nur noch 311 Karten sein

    # Karten hinzufügen, Punkte berechnen:
    spieler_hand.hinzufuegen(Spielkarte("♣", "7"))
    print(spieler_hand)
    print(spieler_hand.get_punkte())  # Muss 7 ergeben
    spieler_hand.hinzufuegen(Spielkarte("♣", "A"))
    print(spieler_hand.get_punkte())  # Muss 18 ergeben
    spieler_hand.hinzufuegen(Spielkarte("♣", "5"))
    print(spieler_hand.get_punkte())  # Muss 13 ergeben, sonst wäre 21 überschritten
    
    
    

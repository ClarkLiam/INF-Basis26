from random import randint, shuffle
import time
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
    
deposit = 0
money = 0
name = 0

def game():
    dealer_set = BlackJackSet()
    spieler_hand = BlackJackHand()
    dealer_hand = BlackJackHand()

    # Spieler zieht 2 Karten
    spieler_hand.hinzufuegen(dealer_set.ziehe1())
    spieler_hand.hinzufuegen(dealer_set.ziehe1())

    # Dealer zieht 2 Karten
    dealer_hand.hinzufuegen(dealer_set.ziehe1())
    dealer_hand.hinzufuegen(dealer_set.ziehe1())

    print(f"Dealer: {dealer_hand.get_karte(0)} ?")
    print()
    print(f"Spieler: {spieler_hand}")
    print(f"Spieler Punkte: {spieler_hand.get_punkte()}")
    print()

    while spieler_hand.get_punkte() < 21 and spieler_hand.is_bust() == False:
        action = input("(h)it (s)tand?")

        if action == "h":
            spieler_hand.hinzufuegen(dealer_set.ziehe1())
            print(f"{name}: {spieler_hand}")
            print(f"{name} Punkte: {spieler_hand.get_punkte()}")
            print()
        elif action == "s":
            break
        else:
            print("Ungültige Eingabe. Bitte 'h' oder 's' eingeben.")
            continue
        
    if spieler_hand.is_bust():
        print(f"{name} hat über 21 Punkte. Dealer gewinnt!")
        return "loss"
    else:
        print("Der Dealer ist Dran.")
        time.sleep(1.3)
        print(f"Dealer: {dealer_hand}")
        print(f"Dealer Punkte: {dealer_hand.get_punkte()}")
        print()
        while dealer_hand.get_punkte() < 17:
            print("Dealer zieht eine Karte...")
            time.sleep(1.3)
            dealer_hand.hinzufuegen(dealer_set.ziehe1())
            print(f"Dealer: {dealer_hand}")
            print(f"Dealer Punkte: {dealer_hand.get_punkte()}")
            print()
    if dealer_hand.is_bust():
        print(f"Dealer hat über 21 Punkte. {name} gewinnt!")
        return "win"
    elif spieler_hand.get_punkte() > dealer_hand.get_punkte():
        print(f"{name} gewinnt!")
        return "win"
    elif spieler_hand.get_punkte() < dealer_hand.get_punkte():
        print("Dealer gewinnt!")
        return "loss"
    elif spieler_hand.get_punkte() == dealer_hand.get_punkte():
        print("Unentschieden!")
        return "draw"

def gamble():
    global deposit
    global money

    while True:
        money = money_handling()
        result = game()
        deposit = money_processing(money, result)
        print(f"Sie haben noch {deposit} Euro übrig.")
        while(deposit > 0):
            play_again = input("Möchten Sie noch einmal spielen? (j/n): ")
            if play_again.lower() != "j":
                print("Danke fürs Spielen!")
                quit()
            elif play_again.lower() == "j":
                print("Willkommen zurück!")
                break
        if deposit <= 0:
            print("Sie haben kein Geld mehr. Spiel beendet.")
            

def depositmoney():
    global name
    name = input("Wie heißen Sie? ")
    print(f"Willkommen {name}!")

    amount = input("Wie viel Geld möchten Sie einzahlen? ")
    print("processing deposit")
    print(f"Sie haben {amount} Euro eingezahlt.")
    print("Willkommen bei BlackJack!")
    return amount


def money_handling():
    global deposit
    global money

    amount = input("Wie viel Geld möchten Sie setzen? ")
    if amount.isdigit():
        amount = int(amount)
        if amount > deposit:
            print("Sie haben nicht genug Geld.")
            print(f"Sie haben {deposit} Euro zur Verfügung.")
            money_handling()
        else:
            deposit -= amount
            print(f"Sie haben {amount} Euro gesetzt.")
            return amount
    else:
        print("Ungültiger Betrag. Bitte geben Sie eine Zahl ein.")
        money_handling()
        
    
def money_processing(money, result):
    global deposit
    if result == "win":
        deposit += money * 2
        print(f"Sie haben {money} Euro gewonnen!")
    elif result == "loss":
        print(f"Sie haben {money} Euro verloren.")
    elif result == "draw":
        deposit += money
        print("Unentschieden! Ihr Geld wird zurückerstattet.")
    else:
        print("Fehler bei der Ergebnisverarbeitung.")

    return deposit



deposit = int(depositmoney())
gamble()
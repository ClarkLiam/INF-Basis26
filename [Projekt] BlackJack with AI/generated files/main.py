import random

class Card:
    """Represents a single playing card."""
    def __init__(self, rank, value):
        self.rank = rank
        self.value = value

    def __str__(self):
        return self.rank

class Deck:
    """Represents a deck of playing cards."""
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        """Builds a standard deck of 52 cards."""
        card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }
        for rank, value in card_values.items():
            for _ in range(4):  # Four of each rank
                self.cards.append(Card(rank, value))

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def deal_card(self):
        """Deals a card from the deck."""
        return self.cards.pop()

def calculate_hand_value(hand):
    """Calculates the total value of a hand."""
    value = sum(card.value for card in hand)
    ace_count = sum(1 for card in hand if card.rank == 'A')
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

def display_hand(player, hand):
    """Displays the player's or dealer's hand."""
    hand_str = ', '.join(str(card) for card in hand)
    print(f"{player}'s hand: {hand_str} (Value: {calculate_hand_value(hand)})")

def blackjack():
    print("Welcome to the Blackjack Game!")

    balance = 100  # Player starts with $100

    while balance > 0:
        print(f"Your current balance: ${balance}")
        
        # Ask for the stake amount
        while True:
            try:
                stake = int(input("Enter your stake for this round: $"))
                if 0 < stake <= balance:
                    break
                else:
                    print(f"Invalid stake amount. You can bet between $1 and ${balance}.")
            except ValueError:
                print("Please enter a valid number.")

        # Initialize and shuffle the deck
        deck = Deck()
        deck.shuffle()

        # Initial deal
        player_hand = [deck.deal_card(), deck.deal_card()]
        dealer_hand = [deck.deal_card(), deck.deal_card()]

        # Display initial hands
        display_hand("Player", player_hand)
        print(f"Dealer's hand: {dealer_hand[0]}, ?")

        # Player's turn
        while True:
            choice = input("Do you want to 'hit' (h) or 'stand' (s)? ").strip().lower()
            if choice == 'h':
                player_hand.append(deck.deal_card())
                display_hand("Player", player_hand)
                if calculate_hand_value(player_hand) > 21:
                    print("Player busts! Dealer wins.")
                    balance -= stake
                    break
            elif choice == 's':
                break
            else:
                print("Invalid choice. Please choose 'h' or 's'.")

        # If player hasn't busted, it's dealer's turn
        if calculate_hand_value(player_hand) <= 21:
            display_hand("Dealer", dealer_hand)
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.deal_card())
                display_hand("Dealer", dealer_hand)
                if calculate_hand_value(dealer_hand) > 21:
                    print("Dealer busts! Player wins.")
                    balance += stake
                    break

        # Determine winner if no busts
        if calculate_hand_value(player_hand) <= 21 and calculate_hand_value(dealer_hand) <= 21:
            player_value = calculate_hand_value(player_hand)
            dealer_value = calculate_hand_value(dealer_hand)
            if player_value > dealer_value:
                print("Player wins!")
                balance += stake
            elif player_value < dealer_value:
                print("Dealer wins!")
                balance -= stake
            else:
                print("It's a tie!")
                # Balance remains unchanged

        # Check if the player can continue
        if balance <= 0:
            print("You have no money left to play. Game over!")
            break

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    blackjack()
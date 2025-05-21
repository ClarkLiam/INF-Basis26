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

class Player:
    """Represents a player in the game."""
    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.hand = []
        self.stake = 0

    def display_hand(self):
        """Displays the player's hand."""
        hand_str = ', '.join(str(card) for card in self.hand)
        print(f"{self.name}'s hand: {hand_str} (Value: {calculate_hand_value(self.hand)})")

def calculate_hand_value(hand):
    """Calculates the total value of a hand."""
    value = sum(card.value for card in hand)
    ace_count = sum(1 for card in hand if card.rank == 'A')
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

def blackjack():
    print("Welcome to the Multiplayer Blackjack Game!")

    # Create players
    num_players = int(input("Enter the number of players: "))
    players = [Player(input(f"Enter the name for player {i + 1}: ")) for i in range(num_players)]

    while any(player.balance > 0 for player in players):
        # Initialize and shuffle the deck
        deck = Deck()
        deck.shuffle()

        # Ask for stakes before dealing cards
        for player in players:
            if player.balance <= 0:
                print(f"{player.name} has no money left to play.")
                continue

            print(f"\n{player.name}'s turn (Balance: ${player.balance})")
            while True:
                try:
                    stake = int(input(f"{player.name}, enter your stake for this round: $"))
                    if 0 < stake <= player.balance:
                        player.stake = stake
                        break
                    else:
                        print(f"Invalid stake amount. You can bet between $1 and ${player.balance}.")
                except ValueError:
                    print("Please enter a valid number.")

        # Initial deal
        dealer_hand = [deck.deal_card(), deck.deal_card()]
        for player in players:
            if player.balance > 0:
                player.hand = [deck.deal_card(), deck.deal_card()]

        # Players' turns
        for player in players:
            if player.balance <= 0:
                continue

            player.display_hand()
            print(f"Dealer's hand: {dealer_hand[0]}, ?")

            # Player's decision
            while True:
                choice = input("Do you want to 'hit' (h) or 'stand' (s)? ").strip().lower()
                if choice == 'h':
                    player.hand.append(deck.deal_card())
                    player.display_hand()
                    if calculate_hand_value(player.hand) > 21:
                        print(f"{player.name} busts! Dealer wins.")
                        player.balance -= player.stake
                        break
                elif choice == 's':
                    break
                else:
                    print("Invalid choice. Please choose 'h' or 's'.")

        # Dealer's turn
        print("\nDealer's turn")
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.deal_card())
        display_hand("Dealer", dealer_hand)

        # Determine winners
        dealer_value = calculate_hand_value(dealer_hand)
        for player in players:
            if player.balance <= 0:
                continue
            player_value = calculate_hand_value(player.hand)
            if player_value <= 21:
                if dealer_value > 21 or player_value > dealer_value:
                    print(f"{player.name} wins!")
                    player.balance += player.stake
                elif player_value < dealer_value:
                    print(f"{player.name} loses.")
                    player.balance -= player.stake
                else:
                    print(f"{player.name} ties with the dealer.")
                    # Balance remains unchanged

        # Check if any player can continue
        if not any(player.balance > 0 for player in players):
            print("All players have run out of money. Game over!")
            break

        # Ask if the players want to play again
        play_again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

def display_hand(player, hand):
    """Displays the dealer's hand."""
    hand_str = ', '.join(str(card) for card in hand)
    print(f"{player}'s hand: {hand_str} (Value: {calculate_hand_value(hand)})")

if __name__ == "__main__":
    blackjack()
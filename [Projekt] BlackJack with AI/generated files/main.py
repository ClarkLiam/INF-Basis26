import random

# Define card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Create a standard deck of cards
deck = [rank for rank in card_values.keys()] * 4

def deal_card(deck):
    """Deals a card from the deck."""
    return deck.pop(random.randint(0, len(deck) - 1))

def calculate_hand_value(hand):
    """Calculates the total value of a hand."""
    value = sum(card_values[card] for card in hand)
    # Adjust for Aces if value is over 21
    ace_count = hand.count('A')
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

def display_hand(player, hand):
    """Displays the player's or dealer's hand."""
    print(f"{player}'s hand: {', '.join(hand)} (Value: {calculate_hand_value(hand)})")

def blackjack():
    # Shuffle the deck
    random.shuffle(deck)

    # Initial deal
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Display initial hands
    display_hand("Player", player_hand)
    print(f"Dealer's hand: {dealer_hand[0]}, ?")

    # Player's turn
    while True:
        choice = input("Do you want to 'hit' or 'stand'? ").strip().lower()
        if choice == 'hit':
            player_hand.append(deal_card(deck))
            display_hand("Player", player_hand)
            if calculate_hand_value(player_hand) > 21:
                print("Player busts! Dealer wins.")
                return
        elif choice == 'stand':
            break
        else:
            print("Invalid choice. Please choose 'hit' or 'stand'.")

    # Dealer's turn
    display_hand("Dealer", dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        display_hand("Dealer", dealer_hand)
        if calculate_hand_value(dealer_hand) > 21:
            print("Dealer busts! Player wins.")
            return

    # Determine winner
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    if player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    blackjack()
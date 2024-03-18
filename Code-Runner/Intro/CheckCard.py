valid_cards = list(range(2, 11)) + ['A', 'J', 'Q', 'K']

while True:
  card = input("Enter a card: ")
  if card.isdigit():
    card = int(card)
  if card in valid_cards:
    print("That's a playing card!")
  else:
    print("That's not a playing card!")
    break
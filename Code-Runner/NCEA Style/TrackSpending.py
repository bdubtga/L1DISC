from word2number import w2n

bank = 200
expenses = [200]
while bank > 0:
  spend = input('Enter the amount spent: ')
  if spend == '0':
    break
  # input validation
  try:
    # try to convert word to number
    try:
      spend = w2n.word_to_num(spend)
    except ValueError:
      # if it fails, try to convert string to int
      spend = int(spend)
  except ValueError:
    print('Please enter a number.')
    continue
  if spend < 0:
    print('You cannot spend a negative amount.')
  bank = bank - spend
  expenses.append(bank)

#print expenses
print(f'My bank balances have been:')
for balance in expenses:
  print(balance)
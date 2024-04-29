"""Code to track and present spending over time."""

#initialise variables
bank = 200
expenses = [200]

while bank > 0:
  spend = input('Enter the amount spent: ')
  if spend == '0': # exit loop if 0 is entered
    break
  try: # convert to integer
      spend = int(spend)
  except ValueError: # if not a number, ask for a number
    print('That is not a valid transaction.')
    continue
  if spend < 0: # check for negative number
    print('You cannot spend a negative amount.')
  bank = bank - spend # update bank balance
  expenses.append(bank) # add to list of expenses

#print expenses
print(f'My bank balances have been:')
for balance in expenses:
  print(balance)
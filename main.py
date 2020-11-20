balance = float(500.50)

amount = ' '

def account_balance(x):
  print(x)

def deposit(x,y):
  balance = float(x + y)
  return '{}'.format(balance)

def withdraw(x,y):
  balance = float(x - y)
  return '{}'.format(balance)
  


while True:
  userchoice = input('What would you like to do?: ')

  if userchoice.lower() == 'b':
    account_balance(balance)

  elif userchoice.lower() == 'd':
    amount = float(input('Enter the amount to deposit: '))
    balance = deposit(amount, balance)
    print(balance)

  elif userchoice.lower() == 'w':
    amount = float(input('Enter the amount to withdraw: '))
    balance = withdraw(balance, amount)
    print(balance)

  elif userchoice.lower() == 'q':
    break

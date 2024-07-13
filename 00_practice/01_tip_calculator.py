bill = int(input('What is your bill: $ '))
# 150

tip_percent = int(input('Choose tip: 12%, 15%, 18%: '))
# 12

tip_percent = float(tip_percent / 100)
total_tip = bill * tip_percent
print(f'Check tip amount -> ${round(total_tip, 2)} ({tip_percent})%')

total_person = int(input('How many person will pay for the bill: '))
total_bill = bill + total_tip
bill_per_person = total_bill / total_person

print('--------------------------------')
print(f'Your total bill: $ {round(total_bill, 2)}')
print(f'Each person will pay: $ {round(bill_per_person, 2)}')
print('--------------------------------')
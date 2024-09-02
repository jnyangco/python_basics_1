bill = int(input('What is your bill? $ '))

tip_percent = int(input('Choose tip percent 12%, 15%, 18%: '))

tip_percent = (tip_percent / 100)

total_tip = round(bill * tip_percent, 4)
print(total_tip)
print(f'Check tip amount {total_tip}, {tip_percent}%')

print(f'TOTAL + TIP: {bill + total_tip}')


total_person = int(input('How many person will pay for the bill?: '))

total_bill_and_tip = bill + total_tip
print(f'{total_bill_and_tip / total_person}')

print('--------------------------------')
print(f'Your total bill is {total_bill_and_tip}')
print(f'Each person will pay {total_bill_and_tip / total_person}')
print('--------------------------------')
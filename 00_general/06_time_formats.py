from datetime import datetime

now = datetime.now()
formatted_date_1 = now.strftime("%b %d, %Y")
formatted_date_2 = now.strftime("%b %-d, %Y") # padded 0 decimal number

print(formatted_date_1) # Dec 04, 2024
print(formatted_date_2) # Dec 4, 2024

# ===============================================
# Using specific date:
print("===========================")
specific_date = datetime(2024, 12, 4)
formatted_date = specific_date.strftime("%b %d, %Y")
print(formatted_date)  # Output: "Dec 4, 2024"
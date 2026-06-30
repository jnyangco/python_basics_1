def remove_dollar_sign(price_text):
    return price_text.replace("$", "")

def remove_spaces(price_text):
    return price_text.strip()

def convert_to_integer(price_text):
    return int(price_text)

def convert_to_float(price_text):
    return float(price_text)

def clean_price(price_text):
    """
    Cleanup price text and convert into float value
    Example: "$1,234.50 " -> 1234.50
    """
    cleaned_price_text = price_text.replace("$", "").replace(",", "").strip()
    return cleaned_price_text


# Test Data
print(remove_dollar_sign("$25.99"))
print(remove_spaces("  $1,234.50   "))
print(convert_to_integer("123"))
print(convert_to_float("123"))
print(clean_price("$1,234.50 "))




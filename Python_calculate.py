def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
       return price*(100-20)/100
    else :
        return price
    
OG_price = float(input('Enter the original price of the item : R '))
discount_percentage = float(input('=Enter the discount of an item as a percentage : '))

print(f'The final price after applying the discount is R{calculate_discount(OG_price,discount_percentage)}')
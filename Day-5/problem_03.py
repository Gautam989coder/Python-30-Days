# Shopping Discount Calculator
'''
Create a function calculate_discount(amount).
- ₹5,000 or more: 20% discount
- ₹3,000 or more: 10% discount
- ₹1,000 or more: 5% discount
- Below ₹1,000: no discount
Return the discount amount, then calculate and print the final price.

Example: ₹4,000 → discount ₹400 → final price ₹3,600.
'''


def calculate_discount(amount):
    if amount < 0:
        return "Invalid Amount"
    
    if amount >= 5000:
        discount_rate = 20
    elif amount >= 3000:
        discount_rate = 10
    elif amount >= 1000:
        discount_rate = 5 
    else:
        discount_rate = 0  

    discount = amount * discount_rate / 100
    final_rate = amount - discount     
    return discount, final_rate

result = calculate_discount (4400)
discount, final_ra = result

if isinstance(result, tuple):
    print(f'Discount: ₹{discount:.2f}')
    print(f'Final price: ₹{final_ra:.2f}')
else:
    print(result)    
 



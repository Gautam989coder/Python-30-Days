# #  Shopping Discount 


# Amount = int(input("Enter Shopping Amount: "))
# if Amount <= 0:
#     print("invalid Amount") 
# elif Amount >= 5000:
#     discount = Amount*20//100
#     final = Amount - discount
#     gst = final*18//100
#     final = final + gst
#     print(f"Discount amount: ₹{discount}")
#     print(f'18% Gst amount {gst}')
#     print(f"Final amount: ₹{final}")
# elif Amount >= 3000:
#     discount = Amount*10//100
#     final = Amount - discount
#     gst = final*18//100
#     final = final + gst
#     print(f"Discount amount: ₹{discount}")
#     print(f'18% Gst amount {gst}')
#     print(f"Final amount: ₹{final}")
# elif  Amount >= 1000 :
#     discount =  Amount*5//100
#     final = Amount - discount
#     gst = final*18//100
#     final = final + gst
#     print(f"Discount amount: ₹{discount}")
#     print(f'18% Gst amount {gst}')
#     print(f"Final amount: ₹{final}")
# else:
#     gst = Amount*18//100
#     Amount = Amount + gst
#     print("No Discount availabe") 
#     print(f'18% Gst amount {gst}')
#     print(f"Shopping amount: ₹{Amount}")  





Amount = int(input("Enter Shopping Amount: "))
if Amount <= 0:
    print("invalid Amount") 
else:
    if Amount >= 5000:
        discount_rate = 20    
    elif Amount >= 3000:
        discount_rate = 10
    elif Amount >= 1000:              
        discount_rate = 5
    else:
        discount_rate = 0

    discount = Amount*discount_rate//100
    discounted_amount = Amount - discount
    gst = discounted_amount*18//100
    final = discounted_amount + gst

    print(f'Shopping amount: {Amount}')
    print(f'discount: {discount}')
    print(f'gst Amount: {gst}')
    print(f'final amount: {final}')
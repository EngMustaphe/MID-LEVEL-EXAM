# item_price=100
# user_money=80
# discount=20
# price=item_price
# money=user_money
# if item_price >=100:
#     print("buy successful")
# elif item_price>=80:
#     print("buy with discount")
# else:
#     print("nor enought money")

item_price = 100
user_money = 80
discount = 20

total = user_money + discount

if total >= item_price:
    print("Buy successful with discount")
else:
    print("Not enough money")
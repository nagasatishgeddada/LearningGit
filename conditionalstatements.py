# # n=5
# # if(n<=0):
# #     print("less than zero")
# # elif(n<=5):
# #     print("value is equal to five")
# # else:
# #     print("n is higher than five")


# Products1 = float(input("No of Qunatity of Product 1:"))
# Products2 = float(input("No of Qunatity of Product 2:"))
# Products3 = float(input("No of Qunatity of Product 3:"))
# price1 = int(input("price of product1:"))
# price2 = int(input("price of product2:"))
# price3 = int(input("price of product3:"))
# if((Products1 <= 0) or (Products2 <= 0) or (Products3 <= 0)):
#     print("Please enter a positive value")
# else:
#     print("total need to pay is :")
#     total = Products1*300 + Products2*400 + Products3*500
#     print(total)


# students = ['satish', 'naga', ' geddada']
# for s in students:
#     print("The students names are :", s)


# students = ['satish', 'naga', 'geddada']
# print("The students names are :")
# for s in students:
#     print(s)


# Products1 = int(input("No of Qunatity of Product 1:"))
# Products2 = int(input("No of Qunatity of Product 2:"))
# Products3 = int(input("No of Qunatity of Product 3:"))
# Products4 = int(input("No of Qunatity of Product 4:"))
# l = [Products1, Products2, Products3, Products4]
# # for i in l:
# #     print(i)
# if((Products1 <= 0) or (Products2 <= 0) or (Products3 <= 0)):
#     print("Please enter a positive value")
# else:
#     print("total need to pay is :")
#     total = Products1*300 + Products2*400 + Products3*500 + Products4*600
#     print(total)


product1_price = 30
product2_price = 50
product3_price = 80
product1 = int(input("Quantity of 1st :"))
product2 = int(input("Quantity of 2nd :"))
product3 = int(input("Quantity of 3rd :"))
l = [product1, product2, product3]
for i in l:
    print(i)
if(product1 < 0 or product2 < 0 or product3 < 0):
    print("please enter a positive number")
else:
    print("The amount to pay is:")
    total = product1*product1_price+product2*product2_price+product3*product3_price
    x = open("mydata.txt", "a")
    print("price of allproducts:")  # to show line in terminal as well
    print("price of all products", file=x)
    dict = {product1: product1_price,
            product2: product2_price, product3: product3_price}
    for k, v in dict.items():
        print(k, v)
        print(k, v, file=x)
    print("total amount is:", total)
    print(total, file=x)

# # print("I need some money")
# # input()
# # input("Give me some money: ")
# money = input("Give me some money: ")
# print('Here is your money -> ',money)

first_money = input("Bela, friend give me some money: ")
second_money = input('Neela, firend give me some money: ')

print('Money i got from Bela: ',first_money,' and money i got from Neela: ', second_money)

total = first_money+second_money
print('Total money I got: ',total) ## here the output will be a string . By default the input function takes input as string
print(type(first_money))

first_money_int =int(first_money)
second_money_int = int(second_money)
print(type(first_money_int))

print('Money i gor from Bela:', first_money_int, 'and money i got from neela: ',second_money_int)
total_money = first_money_int+ second_money_int
print("total money I have: ", total_money)
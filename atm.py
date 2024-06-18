balance=30000
pin=5531
print("welcome to sbi")
i=1
for i in range(3):
 pinno=int(input("enter pin number:"))
 if pinno==2706:
     print("deposit : d withdrawal : w")
     option=input("choose the option")
     if option=="d":
         depositamount=int(input("enter the amount you want to deposit:"))
         print("deposit your amount")
         print("amount deposited successfully")
         option=int(input("want to exit : 0 want to check balance : 1"))
         if option==1:
             current_balance=balance+depositamount
             print(current_balance)
             break
         else:
                 print("tq for using sbi atm")
                 break
         break
     else:
             withdrawalamount=int(input("enter the amount you want to withdrawa:"))
             if withdrawalamount<=balance:
                 print("kirkirrr")
                 print("amount withdrawed successfully!!")
                 option=int(input("want to exit : 0 want to check balance : 1"))
                 if option==1:
                     current_balance=balance-withdrawalamount
                     print(current_balance)
                     break
                 else:
                     print("tq for using sbi atm")
                     break

                 
                 break
             else:
                 print("in sufficient funds")
 else:
                 print("card blocked")
else:
     print("your pin is incorrect")

#!/usr/bin/python3
ruin = 0
phone = int(input("Enter the phones: "))
sale = int(input("Enter the univalence: "))
ruin = 1500 + 200*phone + 0.02 * sale * phone
print("the phone univalence is {} ,his salas phone {} ,and his salary was: {:2f}".format(sale,phone,ruin))

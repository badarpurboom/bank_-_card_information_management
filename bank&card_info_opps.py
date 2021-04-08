# badarpur boom

class Bank:
    def __init__(self, bank, name, account_no, ifsc, card_no, cvv, exp_date, pin):
        self.bank = bank
        self.name = name
        self.account_no = account_no
        self.ifsc = ifsc
        self.card_no = card_no
        self.cvv = cvv
        self.exp_date = exp_date
        self.pin = pin

    def show_details(self):
        print("Bank Name:___________", self.bank)
        print("Account Holder Name:_", self.name)
        print("Account Number:______", self.account_no)
        print("IFSC Code:___________", self.ifsc)
        print("Card Number:_________", self.card_no)
        print("CVV :________________", self.cvv)
        print("Card Expiry Date:____", self.exp_date)
        print("Card Pin Number:_____", self.pin)


acc_ho_nam = []
while True:
    print("set bank info press 1")
    print("show bank info press 2")
    action = input("enter action: ")

    if (action == "1"):
        name = input("Enter Account Holder Name: ")
        acc_ho_nam.append(name)
        ba = input("Bank Name: ")
        ac = input("Account Number: ")
        ifsc = input("IFSC Code: ")
        ca = input("Card Number: ")
        cvv = input("Cvv: ")
        exp = input("Card Expiry Date: ")
        pin = input("Card Pin Number: ")

        acc_ho_nam[-1] = Bank(ba, name, ac, ifsc, ca, cvv, exp, pin)
    if (action == "2"):
        if len(acc_ho_nam) > 0:
            for list in acc_ho_nam:
                print(list.name)
            a = input("enter name for show: ")
            for list in acc_ho_nam:
                if list.name == a:
                    list.show_details()
        else:
            print("*****No Record Found*****")
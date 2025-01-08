def menu(data):
    user_input = int(input("Enter your choice:"))
    match user_input:
        case 1:
            new_user(data)
        case 2:
            existing_user(data)
        case 3:
            balance(data)
        case 4:
            deposit(data)
        case 5:
            withdraw(data)
        case 6:
            exit()
        case _:
            print("enter correct input")
            main()

def new_user(data):
    print("-"*30)
    account_no=int(input("Enter account no:"))
    if account_no in data:
        print('user account already exists')
    else:
        name=input("Enter user name:")
        password=input("Enter password:")

        init_balance=0
        data[account_no]=[name,password,init_balance]
        print("NAME:", data[account_no][0])
        print("ACCOUNT NO:", account_no)
        print("BALANCE:", data[account_no][2])

    print("-" * 30)

    menu(data)

def existing_user(data):
    print("-"*30)
    account_no=int(input("enter account no:"))
    if account_no in data:
        password=input("enter password:")
        if data[account_no][1]==password:
            print("password matched")
            print("NAME:",data[account_no][0])
            print("ACCOUNT NO:", account_no)
            print("BALANCE:", data[account_no][2])
            menu(data)
        else:
            print("password unmatched")
            existing_user(data)

    else:
        print("create an account")
        menu(data)
    print("-" * 30)


def balance(data):
    existing_user(data)

def deposit(data):
    print("-" * 30)
    account_no = int(input("enter account no:"))
    if account_no in data:
        password = input("enter password:")
        if data[account_no][1]==password:
            print("password matched")
            amount=int(input("Enter the amount to deposit:"))
            if amount<0:
                print("enter amount correctly!")
                deposit(data)
            print('amount deposited to your account:',amount)
            data[account_no][2]+=amount
            print('current bank balance:',data[account_no][2])
            print("-" * 30)
            menu(data)
        else:
            print("password unmatched")
            print("-" * 30)
            deposit(data)
    else:
        print("account does not exists")
        print("-" * 30)
        menu(data)

def withdraw(data):
    print("-" * 30)
    account_no = int(input("enter account no:"))
    if account_no in data:
        password = input("enter password:")
        if data[account_no][1] == password:
            print("password matched")
            amount = int(input("Enter the amount to withdraw:"))
            if amount<0:
                print("Enter amount greater than zero")
            if amount>data[account_no][2]:
                print("Insufficient Balance")
                print('bank balance:', data[account_no][2])
                withdraw(data)
            else:
                print('amount withdrawn from your account:', amount)
                data[account_no][2] -= amount
                print('current bank balance:', data[account_no][2])
                print("-" * 30)
                menu(data)
        else:
            print("password unmatched")
            print("-" * 30)
            withdraw(data)
    else:
        print("account does not exists")
        print("-" * 30)
        menu(data)





def main():
    print("===============MENU=============")
    print("\tWelcome\n 1.new user \t 2.existing user\t 3.Balance \n 4.Deposit \t 5.withdraw \t6.exit")
    print("="*30)
    data={}
    menu(data)


if __name__=="__main__":
    main()
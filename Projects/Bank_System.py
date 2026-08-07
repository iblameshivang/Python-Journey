class Account:

    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no


    def credit(self,paisa):
        self.balance+=paisa
        print(f"Your Account ({self.acc_no}) has been Credited with Rs{paisa}")
        self.ask_check_bal()
        print("\n----------------------")

        
    def debit(self,paisa):
        self.balance-=paisa
        print(f"Your account ({self.acc_no}) has been Debited with Rs{paisa} ")
        self.ask_check_bal()
        print("\n----------------------")

         
    def current_balance(self):
        print(f'Current Balance: Rs{self.balance}')

    
    def ask_check_bal(self):
        choice=input("To Check Balance Press 'B' ").capitalize()
        if choice =='B':
            self.current_balance()


A1=Account(7500,'13243XX4224')
A1.credit(2500)

A2=Account(64324,'845XX945432')
A2.debit(63444)
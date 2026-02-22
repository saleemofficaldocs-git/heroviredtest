class BankAccount:

    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.balance = balance

    def __del__(self):
        print("Account closed")
              
    def show_details(self):
        print("Name: ", self.name)
        print("Account No.: ", self.accno)
        print("Balance: ", self.balance)
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def getBalance(self):
        return self.balance
        
saleem_acc = BankAccount("Saleem",20111111,10000)
ayaan_acc = BankAccount("Ayaan",20111112,50000)

#print(saleem_acc.name, saleem_acc.balance)
saleem_acc.show_details()
saleem_acc.deposit(6000)
saleem_acc.show_details()

print("Current")


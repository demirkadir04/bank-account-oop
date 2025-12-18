class Account:
    def __init__(self, balance):

        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount #parametre olanlarda self yapmıyoruz
            return True
        else:
            return False

    def withdraw(self,amount): #parametre olan bir değişkeni instance variable yapmana gerek yok

        if amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return True

    def get_balance(self): #balance bir private değişken olduğu için get metot oluşturduk
        return self.__balance


class SavingsAccount(Account):
    def apply_interest(self, rate):
        if rate > 0:
            interest = self.get_balance() * rate
            self.deposit(interest) #faizi yüklenen paraymış gibi ekliyoruz bakiyeye
            return True
        else:
            return False

acc = SavingsAccount(1000)


print(acc.deposit(500))
print(acc.withdraw(2000))
print(acc.withdraw(300))
print(acc.apply_interest(0.1))
print(acc.get_balance())

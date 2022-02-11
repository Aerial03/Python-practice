'''
[실습]
1. Account class 작성
2. 인스턴스 변수 - account, balance, interestRate
2-1 SavingAccount(Account), FundAccount(Account)
     overriding -- printInterestRate()
-- SavingAccount - printInterestRate()
   기본 이자율에 만기시 이자율을 0.1 계산
-- FundAccount - printInterestRate()
   기본 이자율에 잔액이 10만원 이상이면 10%
   기본 이자율에 잔액이 50만원 이상이면 15%
   기본 이자율에 잔액이 100만원 이상이면 20%
3. accountInfo() - 계좌정보를 출력하는 함수
4. deposit(amount) - 매개변수로 들어온 amount를 balance에 누적
5. withDraw(amount) - 매개변수로 들어온 amount를 balance에서 차감
5-1. 단) 잔고가 부족할 경우 '잔액이 부족하여 출금이 안됩니다.'
6. abstract printInterestRate() - 현재 잔액에 이자율을 계산하여 소숫점까지 출력
'''

class Account:
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def accountInfo(self):
        print('계좌번호: {}, 잔고: {}'.format(self.account,self.balance))
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액이 부족하여 출금이 안됩니다.')
    def printInterestRate(self):
        self.balance = self.balance * (1+self.interestRate)
        print('%.2f' % self.balance)

class SavingAccount(Account):
    def __init__(self, balance, interestRate):
        super().__init__(balance, interestRate)
    def printInterestRate(self):
        return super().printInterestRate()+'만기시 잔액: {}'.format(self.balance)

class FundAccount(Account):
    def __init__(self, balance, interestRate):
        super().__init__(balance, interestRate)
    def printInterestRate(self):
        if 100000 <= self.balance < 500000:
            return super().printInterestRate()+'만기시 잔액: {}'.format(self.balance)
        elif 500000 <= self.balance < 1000000:
            return super().printInterestRate() + '만기시 잔액: {}'.format(self.balance)
        elif self.balance > 1000000:
            return super().printInterestRate() + '만기시 잔액: {}'.format(self.balance)
        else:
            print('이자가 붙지 않습니다.')

account = Account('441-2919-1234', 500000, 0.073)
print('[계좌정보]')
account.accountInfo()
print()

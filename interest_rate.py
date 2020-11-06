WAN = 10000
house_price = 240 * WAN
advance_pay = house_price * 0.3
loan = house_price - advance_pay
x = loan
p = 0.07
year = 30
n = year * 12

interest = 0
for i in range(n):
    interest = interest + (x * p / (n - i))
    
interest_rate = interest/year/x
month_pay = (interest + x) / n
# print(interest)
print("Real interest rate is %.2f%%." % (interest_rate * 100))
print("We need pay %d yuan every month." % month_pay)
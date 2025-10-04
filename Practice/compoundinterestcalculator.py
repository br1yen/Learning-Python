principle = 0
rate = 0
time = 0 

while principle <= 0: 
	principle = float(input("Enter starting balance: "))
	if principle <=  0:
		print("Must have a over 0 amount.")

while rate <= 0:
	rate = float(input("Enter interest rate: "))
	if rate <=  0:
		print("Must have a over 0 interest rate.")

while time <= 0:
	time = float(input("Enter time elapsed(years): "))
	if time <=  0:
		print("Must have a over 0 time elapsed.")

balance = principle*(1 + (rate/100))**time
print(f'{balance:.2f}')
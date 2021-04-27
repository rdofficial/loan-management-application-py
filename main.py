"""
Loan Management System

The application is made as a school project. The application serves the feature of managing monetary loans. The application is made using python3 programming language. The application does makes the use of the database connectivity to store the in-app data, instead it uses JSON format files to manage its data. The application data is stored in the file named 'database.json'.

Author : Rishav Das (https://github.com/rdofficial)
Created on : February 21, 2021
"""

# Importing the required functions and modules
try:
	from json import loads, dumps
	from datetime import datetime
	from os import system
	from sys import platform
except Exception as e:
	# If there are any errors encountered during the importing of modules, then we print the error and exit from the script

	print('[ Error : {} ]'.format(e))
	exit()

# The main script starts here

if 'linux' in platform:
	clear = lambda : system('clear')
else:
	clear = lambda : system('cls')

def getdata(item = ''):
	""" The function which extracts the data from the database.json and returns to the user """

	try:
		data = loads(open('database.json', 'r').read())
		if item == '':
			return data
		else:
			return data[item.lower()]
	except FileNotFoundError:
		# If the database.json file does not exists, then we create a new blank database file

		open('database.json', 'w+').write(dumps([]))
		return []
	except Exception as e:
		# If there are any errors encountered during the process, then we print the error to the console screen

		print('\n[ Error : {} ]'.format(e))

def main():
	""" The main function of the script (DRIVER CODE) """

	# Printing the main menu
	print("""
	Loan Management System
       [ Author : Rishav Das (https://github.com/rdofficial) ]

1. Create a new loan
2. Add payment to a loan
3. Display all existing loans
4. Clear a loan (delete)
0. About
X. Exit
""")

	# Asking the user to enter a choice
	choice = input('Enter your choice : ')
	if choice == '1':
		# If the user chooses the option to create a new loan, then we proceed for it

		item = {}
		clear()
		try:
			# Asking the user to enter the required details for a new loan entry
			print('\nEnter the required details properly')
			item["loan_owner"] = input('\nEnter the name of the person : ')
			item["loan_amount"] = int(input('\nEnter the loan amount : '))
			item["loan_rate"] = int(input('\nEnter the rate of loan : '))
			item["timestamp"] = datetime.now().timestamp()
			item["payments"] = []

			# Inserting the new data into the datbase
			data = getdata()
			data.append(item)
			open('database.json', 'w+').write(dumps(data))
		except Exception as e:
			# If there are any errors encountered during the process, then we print the error on the console screen

			print('\n[ Error : {} ]'.format(e))
			return 0
		else:
			# If there are no errors encountered during the process, then we can assume successfull execution

			print('\n[ New loan entry inserted successfully ]')
	elif choice == '2':
		# If the user chooses to add payment to an existing loan, then we proceed to it

		# Getting the data from the database
		data = getdata()

		# Printing each items in the loan data
		clear()

		if len(data) == 0:
			# If there are no existing loans saved in the database, then we print it and call off

			print('\n[ There are no loans saved in the database, start by creating a new loan entry ]')
			return 0

		print('Existing loans are :\n')
		for index, item in enumerate(data):
			# Iterating through each item in the database

			print('[{}] Name : {} | Amount : {} | Payments already done : {}'.format(index + 1, item["loan_owner"], item["loan_amount"], len(item["payments"])))

		try:
			# Asking the user to enter the index of the loan entry
			index = int(input('\nEnter the sno of the loan entry : '))
			if index <= 0:
				raise IndexError('Please enter corrent sno')
		except Exception as e:
			print('\n[ Error : {} ]'.format(e))
			return 0
		else:
			# If there are no errors in the process, then we continue further

			index -= 1
			clear()
			print('\nDetails of chosen loan are :\nOwner : {}\nLoan Amount : {}\nInterest Rate : {}%\nPayments done : {}\nDate started : {}'.format(data[index]["loan_owner"], data[index]["loan_amount"], data[index]["loan_rate"], len(data[index]["payments"]), datetime.fromtimestamp(data[index]["timestamp"])))

			try:
				# Asking the payment information from the user
				print('\nEnter new payment details')
				payment = {"payment_amount" : 0, "timestamp" : 0}
				payment["payment_amount"] = int(input('Enter the amount paid : '))
				payment["timestamp"] = datetime.now().timestamp()

				# Saving the payment info to the database
				data[index]["payments"].append(payment)
				open('database.json', 'w+').write(dumps(data))
			except Exception as e:
				# If there are any errors in the process, then we print the error on the console screen

				print('\n[ Error : {} ]'.format(e))
				return 0
			else:
				# If there are no errors in the process, then we print the success message on the console screen

				print('\n[ Paymennt added successfully ]')
	elif choice.lower() == '3':
		# If the user chooses the option to display all the loans, then we proceed for it

		# Printing the existing loans as a list on the console screen
		while True:
			# Fetching the data from the database
			data = getdata()

			if len(data) == 0:
                        	# If there are no existing loans saved in the database, then we print it and call off

				print('\n[ There are no loans saved in the database, start by creating a new loan entry ]')
				return 0

			clear()
			print('\nExisting loans are : ')
			for index, item in enumerate(data):
				# Iterating through each item

				print('[{}] Name : {} | Amount : {} | Payments already done : {}'.format(index + 1, item["loan_owner"], item["loan_amount"], len(item["payments"])))

			# Asking the user to enter a proper sno in order to work with a specific database item
			try:
				index = int(input('\nEnter the sno of the loan entry : '))
				if index <= 0:
					raise TypeError()
			except TypeError:
				# If the user enters a string input for a variable intended to take in integer input, then we print the error to the console screen

				print('\n[ Error : Please enter numeric inputs ]')
				input('Press enter key to continue...')
				continue
			else:
				# If there are no errors in entering the sno of the loan entry, then we continue further

				clear()
				print('\nLoan details are listed below : ')

				# Printing the loan details
				index -= 1
				data = data[index]
				print('Loan given to : {}\nLoan amount : Rs. {}\nLoan Interest Rate : {}%\nLoan started on : {}'.format(data["loan_owner"], data["loan_amount"], data["loan_rate"], datetime.fromtimestamp(data["timestamp"])))
				# Iterating through payments history
				total = 0
				print('\nPayment history :')
				for index, item in enumerate(data["payments"]):
					total += item["payment_amount"]
					print('[{}] Amount paid : {}  |  Date : {}'.format(index + 1, item["payment_amount"], datetime.fromtimestamp(item["timestamp"])))

				# Printing the total amount paid
				print('\nTotal amount paid till now : Rs. {}\nNumber of days till now : {} Days'.format(total, -(datetime.fromtimestamp(data["timestamp"]) - datetime.now()).days))
				input('\nPress enter key to go back to main menu...')
				break
	elif choice == '4':
		# If the user chooses the option to clear (delete) a loan, then we proceed to do it
		
		# Getting the data from the database
		data = getdata()

		if len(data) == 0:
                        # If there are no existing loans saved in the database, then we print it and call off

                        print('\n[ There are no loans saved in the database, start by creating a new loan entry ]')
                        return 0

		# Printing each items in the loan data
		clear()
		print('Existing loans are :\n')
		for index, item in enumerate(data):
			# Iterating through each item in the database

			print('[{}] Name : {} | Amount : {} | Payments already done : {}'.format(index + 1, item["loan_owner"], item["loan_amount"], len(item["payments"])))

		try:
			# Asking the user to enter the index of the loan entry
			index = int(input('\nEnter the sno of the loan entry : '))
			if index <= 0:
				raise IndexError('Please enter corrent sno')
			index -= 1
			data.pop(index)

			# Saving the data back to the database
			open('database.json', 'w+').write(dumps(data))
		except Exception as e:
			print('\n[ Error : {} ]'.format(e))
			return 0
		else:
			# If there are no errors in the process, then we print success message on the console screen

			print('[ Specified loan has been cleared (deleted from logs) ]')
	elif choice == '0':
		# If the user chooses the option for displaying the about information for the script, then we proceed to do it

		print("""
		ABOUT
	[ Loan Management System ]

The application (script) is intended to be used as a transaction and money lending management where we can manage history of payments and calculate interests. The application provides the options for saving the loan entries and their payment history in the database and then work on them in future.

The project is made by Rishav Das (https://github.com/rdofficial).
		""")
	elif choice.lower() == 'x':
		# If the user chooses the option to exit the script, then we proceed for it

		exit()
	else:
		# If the user enters an option which is not available, then we raise an error

		print('[ Error : No such option available ]')

if __name__ == '__main__':
	while True:
		try:
			clear()
			main()
			input('Press enter key to continue...')
		except KeyboardInterrupt:
			# If the user presses CTRL+C key combo, then we exit the script immediately

			exit()
		except Exception as e:
			# If there are any errors encountered during the execution of the program, then print that error to the console screen

			print('[ Error : {} ]'.format(e))
			input('Press enter key to continue...')

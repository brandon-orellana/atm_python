"""
Python ATM

This python program will prompt the user to input their 4-digit ATM PIN number.
The user will have 3 attempts to enter their correct PIN, which will display
their balance, otherwise, the user will be locked out of their account.
To begin using this code, run 'atm_python.py'
"""
#Import statements
import sys
import time
from datetime import date

def main():
    """
    The main function uses a while loop to request the user to input a valid
    PIN. The user must enter a valid PIN within 3 attempts or they will be
    locked out.
    """
    ###########################################################################
    #About my code: My code is designed using 1 while loop to ask the user to
    #input the valid PIN. While loop lasts for 3 attempts only. If the user
    #inputs nothing (ie. presses enter), it will prompt the user to enter PIN
    #again, however, it does not count as an attempt. Only actual inputs count.
    #The correct pin is '1234'.
    ###########################################################################
    today_date = date.today()
    today_day = today_date.strftime('%A')
    print(f'Happy {today_day}! \nWelcome to The Python Bank!')
    time.sleep(1)
    print('\nWhen prompted, please enter your 4-digit PIN.')
    print('The valid PIN must be entered within 3 attempts.')
    time.sleep(1)
    ###########################################################################
    sun = 1000000
    spent = 50000
    mon = int(sun - spent)
    tue = int(mon - spent)
    wed = int(tue - spent)
    thu = int(wed - spent)
    fri = int(thu - spent)
    sat = int(fri - spent)
    money = [sun, mon, tue, wed, thu, fri, sat]
    day_of_week = int(today_date.strftime('%w'))
    ###########################################################################
    #This while loop will ask the user to input a PIN. Valid PIN must be entered
    #in 3 attempts or else the account is locked.
    attempt = 0
    while attempt < 3:
        try:
            pin = input('\nPlease enter your PIN: ')
            count = 2 - attempt
            if not pin:
                print('No PIN inputted. ')
                continue
            if not pin.isnumeric():
                print('Incorrect input values. All values must be digits')
                print(f'Attempts remaining: {count}')
            elif not len(pin) == 4:
                print('Pin must be 4-digits long.')
                print(f'Attempts remaining: {count}')
            elif int(pin) == 1234:
                print(f'Your account balance is: ${money[day_of_week]}')
                print('\nHave a good day!')
                sys.exit()
            else:
                print('Invalid PIN!')
                print(f'Attempts remaining: {count}')
        except KeyboardInterrupt:
            try:
                exit_atm = input('Do you wish to exit the ATM (Y/N)?: ')
                if exit_atm in ('y','Y','yes','Yes','YES'):
                    print('Have a good day!')
                    sys.exit()
                elif exit_atm in ('n','N','no','No','NO'):
                    continue
                else:
                    print('Input value not an option.')
                    continue
            except KeyboardInterrupt:
                sys.exit()
        attempt += 1
    print('\nThe account has been locked. The police are on their way.')
    sys.exit()
    ###########################################################################
    #This is the end of the code
if __name__ == '__main__':
    main()

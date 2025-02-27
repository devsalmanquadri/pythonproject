from datetime import datetime
import random
import datetime
# =====================================================================================================
# =====================================================================================================


def calculator(num1, num2):
    ch = input(
        '''Enter any of these That You Want: 
1) addition(+)
2) subtraction(-) 
3) division(/)
4) multiplication(*)\n
------- Choose One -------\n
''')

    result = 0
    if ch == '1':
        result = num1+num2
    elif ch == '2':
        result = num1-num2

    elif ch == '3':
        result = num1*num2
    elif ch == '4':
        result = num1/num2

    else:
        print(" Invalid Chacters Input \n")

    print(f'''
   =======++++++++++++========
    Your Answer is: {result}.
   =======++++++++++++========
    ------------:Try More Services Form Here:-----------\n''')

# =====================================================================================================
# =====================================================================================================


def DateandTime():
    now = datetime.datetime.now()
    print("Current Date and Time =", now)

# =====================================================================================================
# =====================================================================================================


def Playagame():
    randnumber = random.randint(1, 100)
# print(randnumber)
    userguess = None
    guesses = 0
    print('''.......................................................................................
........................................ RULES ........................................
In This Game The Computer Choose a Random Number in Between 1-100. 
You Have To Guess This Number. 
If Your Guess is Bigger Then That Number Then You Should Have To Guess A Lower Number.
or if Your Guess is Lower Then That Number Then You Should Have To Guess A Bigger Number.
Enter "Q" To Quit.
........................................ So Lets Start ........................................ 
        ''')
    while(userguess != randnumber):
        userguess = input("Enter Your Guess Please: ")
        guesses += 1
        if (userguess == "Q"):
            print("Thank you For Playing!")
            break

        try:
            userguess = int(userguess)
            if(userguess == randnumber):
                print(f''' +++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++
Congartulation ! You Guessed it Right! in {guesses} guesses
+++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
            elif(userguess < randnumber):
                print("..................Try Higher Number Please!..................")
            elif(userguess > randnumber):
                print("..................Try Lower Number Please!..................")
        except Exception as e:
            print(f"Invalid Input ! Please Type a Number")

# =====================================================================================================
# =====================================================================================================


Name = input("Enter Your Name: ")

Welcomemsg = (f'''================ Welcome {Name} To This Interface ================
1) Use Calculator
2) Show The Date & Time 
3) Play a Game
4) Exit From This Interface\n 
''')

# -------------------------------------------------------------------------------------------------

print(Welcomemsg)

# =====================================================================================================
# =====================================================================================================

while(True):
    try:
        b = int(input("Type Your Choice: "))
        if b == 1:
            num1 = int(input("Enter the Value of x: "))
            num2 = int(input("Enter the Value of y: "))
            calculator(num1, num2)
    # ------------------------------------------------------------------------------------------------
        elif b == 2:
            print(DateandTime())
    # ------------------------------------------------------------------------------------------------
        elif b == 3:
            Playagame()
    # ------------------------------------------------------------------------------------------------
        elif b == 4:
            exit()

        elif b > 4:
            print("Invalid Input! Please Enter A Correct Number Given Below")
    # ------------------------------------------------------------------------------------------------
        print(Welcomemsg)
    except Exception as k:
        print("Invalid Input! Please Enter From The Number Given Below")
        print(Welcomemsg)

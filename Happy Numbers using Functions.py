# Function for happy number
def is_happy(n): # Return True if the given number is happy else it will return False
    while n!=1 and n!=4:
        ss = 0
        while n:
            r = n%10
            ss += r*r
            n = n//10

        n = ss
    if(n==1):
        return True
    else:
        return False
    

while(True):
    # Input from user
    x = input('Check or Range?:')
    
    # If user enters Check
    # Ask to give a number to check
    if(x == 'Check'):
        num = int(input('Enter a number to check:')) #12
        # if num is happy
        # print Happy number
        if(is_happy(num)): # Function call 1 is_happy(10)
            print('Happy')
        # else
        # print unhappy number
        else:
            print('Unhappy')

    # If user enters Range as a choice
    # Ask user to enter two numbers
    elif(x == 'Range'):
        a, b = map(int, input('Enter two numbers:').split())
        # Ask user if he wants happy series or unhappy series
        choice = input('Happy or Unhappy:')
        # If choice is happy
        # Print all the happy numbers in the given range
        if(choice == 'Happy'):
            for i in range(a,b+1):
                if(is_happy(i)):
                    print(i,end = ' ')
        # if the choice is unhappy
        # Print all the unhappy numbers in the given range
        else:
            for i in range(a,b+1):
                if(not is_happy(i)):
                    print(i,end=' ')
    else:
        print('Invalid Input')
        break
        

#Laxy calculator(Default arguments and try/except)

def div_two_number(a,b = 2):
    try:
        print(f"the result is {a / b}") 
    except ZeroDivisionError as e:
            print(f"error is {e}")
    except TypeError as e:
         print(f"please enter numbers only {e}")




div_two_number(12)
div_two_number(3,0)
div_two_number("two",4)

#The login Password checker(Loop/if else/input)

correct_password = "python123"
def password_checker():
    for times in range(1,4):
         input_password = input("Enter password: ")
         if input_password == correct_password:
              print("access granted")
              break
         else:
            print("wrong password")
    else:
        print("Account locked")

# password_checker()

#Robust data processor
datas = [10, "hello", 5, 0, "20", 4]
def processor(data_list,power = 2):
    for data in data_list:
         try:
              convert = pow(int(data),power)
              print(convert)
         except ValueError as e:
              print(f"skipping {data} not a number")
         except Exception as e:
              print("unexpected error")
        
     
processor(datas)
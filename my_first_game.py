VERSION =(1.0)


import  random
print ('Welcome to "Find Number" game')
name=input("Enter your name: ") 
print("Hello "+name+". Do you want to play?")
flag = False

while True:
    ans=input("Yes or No: ")
    if ans.lower() == "yes" :
        print('You said "yes". OK, let`s go!!!')
        flag=True
        break
    elif ans.lower() == "no":
        print ('You said "No". OK, see you later')
        break
    else:
        print("I don`t understand, try again")
        
        
#flag = True #це для тесту, потім видалити


counter=0
num = random.randint(1,100)
print ("We have some number. What is this number?")

while flag:
    user_num=input("Your number: ")
    user_num=int(user_num)
    if (user_num<=100) and (user_num >0):
        counter+=1
        if user_num > num:
            print ( "No, my number is smaller")
        elif user_num < num:
            print ( "No, my number is bigger")
        elif user_num == num:
            print("Well done. You right, my number was "+str(num))
            flag= False
            print ("You used "+str(counter)+" tries")
            # ~ print("Do you want to try again?") 
            # ~ restart_game =input("Yes or No: " )
            # ~ if restart_game.lower() == "yes" :
                # ~ print('You said "yes". OK, let`s go!!!')

                # ~ break
            # ~ elif restart_game.lower() == "no":
                # ~ print ('You said "No". OK, see you later')
                # ~ break
            # ~ else:
                # ~ print("I don`t understand, try again")
    else:
        print( "Your number can`t be bigger than 100 and smaller than 1")
        print ("Try again")

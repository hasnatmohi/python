password= 'open@'
n:int = 1
      print('Please enter password')
while n <4:

    x=input()
    if x == password:
       print('You may enter')
       break
    
    if x !=  password:
        print('please try again')
        n = n+1

if n := 3:
    print('What is your favourite color?')
    y=input()
    if y == 'black':
        print('Please enter new password')
        password = input()
        print('your password has been rest to', password)
    else:
        print('Please Contact Us.')
        

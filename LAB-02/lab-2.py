# a=input('Enter a value: ')#always returns string
# print('The given value is '+a)
# print(type(a))


# a=int(input('Enter a number: ')) #returns string but
# print('The given value is '+str(a+11))
# print('test:',a)
# print('test2:',+a)
# print(type(a))


# while True:
#     a=input('Enter your birth year')
#     if a.isdigit():
#         print('Your are '+str(2026-int(a)) + ' years old')
#         print(2026-int(a))
#         break
#     print('Wrong input')


# #indent
# i=4
# if i<5: # () not required, {} not required
#     print('Okay')
#     print('fine')
# else:
#     print('bad')
#     print('not okay') #will be excuted in each run



# x=int(input("Please enter an integer: "))
# if x<0:
#     x=0
#     print('negative changed to zero')
# elif x==0:
#     print('Zero')
# elif x==1:
#     print('Single')
# else:
#     print('More')



##For statement

#Measure some strings
# words =['Cat', 'Window','dhaka','jack']
# for w in words:
#     print(w,len(w))

# for i in range(0,len(words),2):
#     print(i,words[i],len(words[i]))


#Function

def operate(a,b):
    print(str(a) +" + " +str(b) + ' = '+str(a+b))
    print(str(a) +" - " +str(b) + ' = '+str(a-b))
    print(str(a) +" * " +str(b) + ' = '+str(a*b))
    print(str(a) +" / " +str(b) + ' = '+str(a/b))

operate(91,5)
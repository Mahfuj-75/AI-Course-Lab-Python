#addition, sub, multip, diva=10
# a=10
# b=3
# sum= a+b
# sub= a-b
# prod= a*b
# div= a/b
# print("Sum: ", sum)
# print("sub:", sub)
# print(f"Sum: {sum}, Sub: {sub}, Product: {prod}, division: {div}")
# print(type(sum))
# print(type(div))
# newProd=prod*2
# print(newProd)

# mod, power, floor div
import math as m
c=2
d=3
mod= d%c
pow= m.pow(c,d) #2^3
pow2=  c**d #c^d
fdiv= d//c #floor or intiger divison
print(f"mod: {mod}, powe_func: {pow}, Power_oper: {pow2}, and floor div: {fdiv}")



# abs and round
num1= -7.6
num2 =3.6
print("abs: ", abs(num1))
print("round num1: ",round(num1))
print("round num2: ",round(num2))

print(num1)


#sqrt, factorial, trigonometric valu
sqrt= m.sqrt(16)
fact= m.factorial(5)
sin_val= m.sin(m.radians(30))
print(f"sqrt: {sqrt}, facrotial: {fact}, Sin 30: {sin_val}")
print(type(sqrt))
print(type(fact))


# repeat string
str1= "Hello " * 7
print(str1)
#concate
str2= "Hello"
str3= "World"
text= str2+" "+str3
print(text)








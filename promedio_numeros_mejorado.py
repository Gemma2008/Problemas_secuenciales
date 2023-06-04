num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))
num3 = int(input("Dime el tercer numero: "))
def promedio(num1,num2,num3):
    media = (num1 + num2 + num3)/3
    return(media)
print("El promedio es: ", promedio(num1,num2,num3))

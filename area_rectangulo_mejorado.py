base = int(input("Dime la base: "))
altura = int(input("Dime la altura: "))

def area_rectangulo(base,altura):
  
    area = base * altura
    return(area)
print("El area del rectangulo es: ", area_rectangulo(base,altura))

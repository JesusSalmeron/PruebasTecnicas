
cantidad = float(input("Introduce una cantidad."))
interest = float(input("CUal es el tipo de interés."))
years = int(input("Años¿?"))


for i in range(years):
    cantidad *=1 + interest /100
    print("Capital tras -> ",str(i+1)," años " + str(round(cantidad,2))) #round = redondea el nº de decimales que le indiques.



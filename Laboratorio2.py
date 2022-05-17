#-----------------------------------------Transformar centimetros a metros y kilometros----------------------------------------------

#-----------------------------------------Mensaje de que debe ingresar el usuario----------------------------------------------------

print("Ingrese el valor de la longitud en centimetros")


#-----------------------------------------Declaración de variable y Asignación-------------------------------------------------------

nume1 = int(input("Valor a ingresar-> "))
#-----------------------------------------Subprogramas/funciones de metro y kilometro------------------------------------------------

def metros(nume1):
    metro= nume1*(1/100)
    print ("La longitud en metros/m de "+str(nume1)+" centimetros/cm es de "+str(metro)+" metros/m")
    return metro

def kilometros(nume1):
    kilometro=nume1*(1/100)*(1/1000)
    print ("La longitud en kilometros/km de "+str(nume1)+" centimetros/cm es de "+str(kilometro)+" kilometros/km") 
    return kilometro

#------------------------------------------Resultado a mostrar en pantalla de la trasnformación--------------------------------------

metros(nume1)
kilometros(nume1)

#------------------------------------------------------------------------------------------------------------------------------------



def saludo(nombre):
    print('hola {}'.format(nombre))
    print('bienvenido a la clases de hoy')
    print('del canal de youtube')
    #con el comando: saludo('joel') -> hola joel bienvenido...
saludo('joel')
#con numeros:
def resta(a, b):
    return a - b
c = resta(10, 4)
print('la resta es {}'.format(c))
#actualizacion
c = resta(b=10, a=4)
print('la resta es {}'.format(c))
#solucion de errores 
def resta(a = None, b = None):
    if a == None or b == None:
        print("Error, debes enviar dos numeros a la funcion")
        return
    return a - b
c = resta(10)
print('la resta es {}'.format(c))
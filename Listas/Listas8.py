def introduceDatos(listaalumno):
    from decimal import Decimal as D
    for i in range(1,3):
         lista=[]
         Alumno=input("Alumno: ")
         Nombre=input("Nombre: ")
         lista.append((Alumno,Nombre))
         for i in range(1,3):
              Asignatura=input("Asignatura: ")
              nota=input("Notas: " )
              lista.append((Asignatura,D(nota)))
         listaalumno.append(lista)         
    return listaalumno

def ordenado(milista):
    from operator import itemgetter
    milistaordenada=sorted(milista,key=lambda x: x[0][1])    
    return milistaordenada
    
def mostrar(milistaordenada):   
    print("ASIGNATURAS--Notas")
    print("==================")
    for alumno in milistaordenada:
        print("Alumno: ", alumno[0][0])
        print("Nombre: ", alumno[0][0])
        for asignatura, nota in alumno[1:]: 
            print(f"{asignatura} ----- {nota}")

def main(args):
    
    milista=[] 
    milista=introduceDatos(milista)
    milistaordenada=ordenado(milista)
    print(mostrar(milistaordenada))
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

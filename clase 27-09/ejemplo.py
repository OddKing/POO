clientes=[{'nombre':'Juan','apellido':'Perez','rut':'11111111-1'},{'nombre':'Juana','apellido':'Pereza','rut':'22222222-2'}]

print(clientes)

def mostrar_clientes(rut):
    for cliente in clientes:
        if(cliente['rut']==rut):
            print(cliente)
            return
    print("no se encontro usuario")

mostrar_clientes('22222222-2')


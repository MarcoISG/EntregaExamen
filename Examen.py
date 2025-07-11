productos = {
    '8475HD':['HP', 15.6, '8GB', 'DD','1T','Intel Core i5', 'Nvidia GTX1050'],
    '2175HD':['lenovo',14, '4GB','SSD', '512GB','Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD':['Asus',14,'16GB','SSD','256GB','Intel Core i7','Nvidia RTX2080Ti']
}

stock = {
    '8475HD':[387990,10],
    '2175HD':[327990,4],
    'JjfFHD':[424990,1]
}


def stock_marca(marca):
    contador = 0
    while True:
        marca = input('Ingrese la marca a buscar: ')
        for lista in productos.values():
            if lista[0].lower() == marca.lower():
                contador +=1
        if contador !=0:
            print(f'El stock disponible para la la marca {marca} es de {contador}')
            break
            
        else:
            print(f'No existe stock disponible para la marca {marca}')
    
        
    
  
                 
# stock_marca(productos)

def busqueda_precio(p_min,p_max):
    lista = ["",""]
    if p_min !=0 and p_max > p_min:
        for clave, valor in stock.items():
            if valor[0] >= p_min and valor[0]<= p_max:
             marca = productos[clave]
             lista = [ valor[0],marca[0]]
             print(lista) 
             break 


print("""
    ***Menú***
    1.Stock marca
    2.Búsqueda por precio
    3.Salir
""")
op = input('Ingrese su opcion: ')

if op != 3:
    while True:
        if op == '1':
            print('1.Stock por marca')
            stock_marca(productos)
            
        elif op == '2':
            print('2.Búsqueda porr rango de precio')
            pMin = int(input('Ingresa el precio minimo:  '))
            pMax = int(input('Ingresa el precio maximo:  '))
            busqueda_precio(pMin,pMax)
            
        elif op == '3':
            print('3.Atualizar precios')
            
        elif op == '4':
            print('4.Programa terminado!!!')
            break

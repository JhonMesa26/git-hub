# #Ejercicio 7
# #Una familia quiere digitalizar el árbol genealógico, están dispuestos a contratar un ingeniero que les haga un programa donde ellos puedan almacenar la información: nombres, apellidos, edad, género y generación (bisabuelos, abuelos, padres, yo, hijos). Teniendo en cuenta los parámetros dados por la familia. Usted debe hacer un programa empleando POO en Python. En una clase llamada Persona () se pueden ingresar los datos básicos (nombre, apellido, edad y genero) de los familiares, según criterio de edad él pueda ubicarse en la Clase Generación () correspondiente y cuando desee mostrar en pantalla su árbol genealógico pueda hacerse: ascendente o descendente cronológicamente y aparecer todos los datos de la persona.

# import pandas as pd
# import os

# class Persona():
#     def __init__(self):
#         self.archivos_personas = 'Personas.csv'
#         try:
#             self.P = pd.read_csv(self.archivos_personas)
#         except FileNotFoundError:
#             self.P = pd.DataFrame(columns=['NOMBRE','APELLIDO','EDAD','GENERO','GENERACION'])
#             self.P.to_csv(self.archivos_personas, index=False)
#             print('Archivo creado con éxito')
#         self.nombre = input('Ingrese su nombre: ')
#         self.apellido = input('Ingrese su apellido: ')
#         self.edad = int(input('Ingrese su edad: '))
#         self.genero = input('Ingrese su genero: ')
#         nuevo_persona = pd.DataFrame({
#             'NOMBRE': [self.nombre],
#             'APELLIDO': [self.apellido],
#             'EDAD': [self.edad],
#             'GENERO': [self.genero],
#             'GENERACION': [None]
#         })
#         if os.path.exists(self.archivos_personas):
#             personas_existentes = pd.read_csv(self.archivos_personas)
#             self.P = pd.concat([personas_existentes, nuevo_persona], ignore_index=True)

# class Generacion(Persona):
#     def __init__(self):
#         super().__init__()
#         self.generacion=input('Ingrese su generación: ')
#         mask = (self.P['NOMBRE'] == self.nombre) & (self.P['APELLIDO'] == self.apellido)
#         if mask.any():
#             # Actualizar la columna `GENERACION`
#             self.P.loc[mask, 'GENERACION'] = self.generacion
#             self.P.to_csv(self.archivos_personas, index=False)
#             print('Generación agregada con éxito')
#         else:
#             print('No se encontró a la persona con ese nombre y apellido.')
#     def ordenar_por_generacion_Mayor(self):
#         orden_generacional = ["Bisabuelo", "Abuelo", "Padre", "Hijo", "Nieto"]
        
#         # Ordenar el DataFrame `P` basado en el orden generacional y luego por edad descendente
#         self.P['GENERACION'] = pd.Categorical(self.P['GENERACION'], categories=orden_generacional, ordered=True)
#         personas_ordenadas = self.P.sort_values(by=['GENERACION', 'EDAD'], ascending=[True, False])
        
#         print("Personas ordenadas de la más antigua a la más joven:")
#         print(personas_ordenadas)
#     def ordenar_por_generacion_Menor(self):
#         orden_generacional = ["Bisabuelo", "Abuelo", "Padre", "Hijo", "Nieto"]
        
#         # Ordenar el DataFrame `P` de la más joven a la más antigua
#         self.P['GENERACION'] = pd.Categorical(self.P['GENERACION'], categories=orden_generacional, ordered=True)
#         personas_ordenadas_inverso = self.P.sort_values(by=['GENERACION', 'EDAD'], ascending=[False, True])
        
#         print("Personas ordenadas de la más joven a la más antigua:")
#         print(personas_ordenadas_inverso)

# while True:
#     op=int(input('Digite:\n1. Agregar  \n2. Orden de mayor a menor\n3. Orden de menor a mayor\n4. Salir\n'))
#     if op==1:
#         a=Generacion()
#     elif op==2:
#         a=Generacion()
#         a.ordenar_por_generacion_Mayor()
#     elif op==3:
#         a=Generacion()
#         a.ordenar_por_generacion_Menor()
#     elif op==4:
#         exit()
#     else:
#         print('Opción no válida')

#Ejercicio 8
#Diseñe un algoritmo empleando Python, POO y sus propiedades (herencia, encapsulamiento y polimorfismo) en la solución de un problema que involucre la ingeniería electrónica. Puede buscar una asignatura de su pensum para realizar una aplicación.

#Ejercicio 9
#Una empresa lo contrata para crear un algoritmo gestor que pueda manejar toda la información de un cinema. Se debe gestionar: El cinema exige una interfaz gráfica para sus empleados y usuarios (clientes), Cartelera de películas (nombre de la película y horario, mostrar en interfaz), Compra de tiquetes (permitir llevar el control de que película compran tiquetes y almacenar la información), Venta de comidas (mostrar en interfaz y almacenar la información) e Informe para administrador: Numero de tiquetes vendidos en cada película, dinero ganado por películas y venta de comida. Todos los registros deben quedar almacenados en archivo CSV.
# import pandas as pd
# import os

# class Empleado():
#     def __init__(self):
#         self.archivos_peliculas = 'Peliculas.csv'
#         self.ventas = 'Ventas.csv'  # Archivo para registrar ventas
#         try:
#             self.P = pd.read_csv(self.archivos_peliculas)
#         except FileNotFoundError:
#             self.P = pd.DataFrame(columns=['NOMBRE', 'HORARIO', 'PRECIO_TIQUETES', 'TIQUETES', 'COMIDAS_DISPONIBLES', 'COMIDAS', 'PRECIO_COMIDAS'])
#             self.P.to_csv(self.archivos_peliculas, index=False)
#             print('Archivo de películas creado con éxito')

#         # Solicitar datos de la película
#         self.pelicula = input('Ingrese el nombre de la película: ')
#         self.horario = input('Ingrese el horario de la película: ')
#         self.precio = int(input('Ingrese el precio por tiquete: '))
#         self.comidas_disponibles = int(input('Ingrese la cantidad inicial de comidas disponibles: '))

#         nuevo_pelicula = pd.DataFrame({
#             'NOMBRE': [self.pelicula],
#             'HORARIO': [self.horario],
#             'PRECIO_TIQUETES': [self.precio],
#             'TIQUETES': [0],
#             'COMIDAS_DISPONIBLES': [self.comidas_disponibles],
#             'COMIDAS': [0],
#             'PRECIO_COMIDAS': [0]
#         })
        
#         if os.path.exists(self.archivos_peliculas):
#             peliculas_existentes = pd.read_csv(self.archivos_peliculas)
#             self.P = pd.concat([peliculas_existentes, nuevo_pelicula], ignore_index=True)
#         else:
#             self.P = nuevo_pelicula

#         self.P.to_csv(self.archivos_peliculas, index=False)
#         print("Película y cantidad de comidas agregadas exitosamente")
#         self.Tiquetes()

#     def Tiquetes(self):
#         self.tiquetes = int(input('Ingrese el número de tiquetes: '))
#         self.precio_total_tiquetes = self.tiquetes * self.precio
#         self.P.loc[self.P['NOMBRE'] == self.pelicula, 'TIQUETES'] = self.tiquetes
#         self.P.loc[self.P['NOMBRE'] == self.pelicula, 'PRECIO_TIQUETES'] = self.precio_total_tiquetes
#         self.P.to_csv(self.archivos_peliculas, index=False, encoding='utf-8')
#         print('Tiquetes agregados con éxito. El precio de los tiquetes es de: ', self.precio_total_tiquetes)
#         self.Menu_Comidas()

#     def Menu_Comidas(self):
#         self.comidas = int(input('Ingrese el número de comidas: '))
#         self.precio_total_comidas = self.comidas * 1000
#         self.P.loc[self.P['NOMBRE'] == self.pelicula, 'COMIDAS_DISPONIBLES'] = self.comidas
#         self.P.loc[self.P['NOMBRE'] == self.pelicula, 'PRECIO_COMIDAS'] = self.precio_total_comidas
#         self.P.to_csv(self.archivos_peliculas, index=False, encoding='utf-8')
#         print('Comidas agregadas con éxito. El precio de las comidas es de: ', self.precio_total_comidas)

#     def Inventario(self):
#         self.P = pd.read_csv(self.archivos_peliculas)    
#         print(self.P[['NOMBRE', 'TIQUETES', 'COMIDAS', 'COMIDAS_DISPONIBLES', 'PRECIO_TIQUETES', 'PRECIO_COMIDAS']])

#     def ventas_totales(self):
#         try:
#             V = pd.read_csv(self.ventas)
#             total_tiquetes = V['TIQUETES'].sum()
#             total_precio_tiquetes = V['PRECIO_TIQUETES'].sum()
#             total_comidas = V['COMIDAS'].sum()
#             total_precio_comidas = V['PRECIO_COMIDAS'].sum()
            
#             print("\nVentas Totales:")
#             print(f"Tiquetes vendidos: {total_tiquetes} - Ingresos por tiquetes: ${total_precio_tiquetes}")
#             print(f"Comidas vendidas: {total_comidas} - Ingresos por comidas: ${total_precio_comidas}")
#         except FileNotFoundError:
#             print("No se encontró el archivo de ventas. Asegúrese de que existan registros de ventas.")

# class Cliente():
#     def __init__(self):
#         self.archivos_peliculas = 'Peliculas.csv'
#         self.ventas = 'Ventas.csv'
#         try:
#             self.V = pd.read_csv(self.ventas)
#         except FileNotFoundError:
#             self.V = pd.DataFrame(columns=['NOMBRE', 'TIQUETES', 'COMIDAS', 'PRECIO_TIQUETES', 'PRECIO_COMIDAS', 'PRECIO_TOTAL'])
#             self.V.to_csv(self.ventas, index=False)
#             print('Archivo de ventas creado con éxito')
        
#         try:
#             self.P = pd.read_csv(self.archivos_peliculas)
#         except FileNotFoundError:
#             print("Archivo de películas no encontrado. Asegúrese de que el archivo 'Peliculas.csv' exista.")
#             return
        
#         self.Cartelera()
        
#     def Cartelera(self):
#         print("\nPelículas en cartelera:")
#         print(self.P[['NOMBRE', 'HORARIO', 'PRECIO_TIQUETES']])
#         pelicula = input('Ingrese el nombre de la película que desea comprar: ')
        
#         pelicula_en_cartelera = self.P[self.P['NOMBRE'] == pelicula]
#         if not pelicula_en_cartelera.empty:
#             self.pelicula = pelicula
#             self.precio_base = pelicula_en_cartelera.iloc[0]['PRECIO_TIQUETES']
#             self.tiquetes_disponibles = pelicula_en_cartelera.iloc[0].get('TIQUETES', 0)
#             self.comidas_disponibles = pelicula_en_cartelera.iloc[0].get('COMIDAS_DISPONIBLES', 0)
#             print("\nInformación de la película seleccionada:")
#             print(pelicula_en_cartelera)
#             print(f"Tiquetes disponibles: {self.tiquetes_disponibles}")
#             print(f"Comidas disponibles: {self.comidas_disponibles}")
#             self.Compra_Tiquetes()
#         else:
#             print('No se encontró la película en cartelera.')

#     def Compra_Tiquetes(self):
#         self.tiquetes = int(input('Ingrese el número de tiquetes: '))

#         if self.tiquetes > self.tiquetes_disponibles:
#             print(f"No hay suficientes tiquetes disponibles. Solo quedan {self.tiquetes_disponibles} tiquetes.")
#             return

#         self.precio_tiquetes = self.tiquetes * self.precio_base
#         print('Tiquetes agregados. El precio de los tiquetes es de: ', self.precio_tiquetes)

#         nuevos_tiquetes_disponibles = self.tiquetes_disponibles - self.tiquetes
#         self.P.loc[self.P['NOMBRE'] == self.pelicula, 'TIQUETES'] = nuevos_tiquetes_disponibles
#         self.P.to_csv(self.archivos_peliculas, index=False, encoding='utf-8')

#         self.Venta_Comidas()

#     def Venta_Comidas(self):
#         self.comidas = int(input('Ingrese el número de comidas: '))

#         if self.comidas > self.comidas_disponibles:
#             print(f"No hay suficientes comidas disponibles. Solo quedan {self.comidas_disponibles} comidas.")
#             return

#         self.precio_comidas = self.comidas * 1000
#         print('Comidas agregadas. El precio de las comidas es de: ', self.precio_comidas)

#         nuevas_comidas_disponibles = self.comidas_disponibles - self.comidas
#         self.P.loc[self.P['NOMBRE'] == self.pelicula, 'COMIDAS_DISPONIBLES'] = nuevas_comidas_disponibles
#         self.P.to_csv(self.archivos_peliculas, index=False, encoding='utf-8')

#         self.Costo_total()

#     def Costo_total(self):
#         self.precio_total = self.precio_tiquetes + self.precio_comidas
#         nueva_venta = pd.DataFrame({
#             'NOMBRE': [self.pelicula],
#             'TIQUETES': [self.tiquetes],
#             'COMIDAS': [self.comidas],
#             'PRECIO_TIQUETES': [self.precio_tiquetes],
#             'PRECIO_COMIDAS': [self.precio_comidas],
#             'PRECIO_TOTAL': [self.precio_total]
#         })
        
#         self.V = pd.concat([self.V, nueva_venta], ignore_index=True)
#         self.V.to_csv(self.ventas, index=False, encoding='utf-8')
#         print('El precio total de la venta es de: ', self.precio_total)
#         print("Registro de ventas actualizado:")
#         print(self.V[['NOMBRE', 'TIQUETES', 'COMIDAS', 'PRECIO_TIQUETES', 'PRECIO_COMIDAS', 'PRECIO_TOTAL']])


# while True:
#     op = int(input('Digite:\n1. Empleado \n2. Cliente \n3. Salir\n'))
#     if op == 1:
#         a = Empleado()
#         opc = int(input('Digite:\n1. Tiquetes \n2. Inventario \n3. Ventas totales \n4. Salir\n'))
#         if opc == 1:
#             a.Tiquetes()
#         elif opc == 2:
#             a.Inventario()
#         elif opc == 3:
#             a.ventas_totales()
#         elif opc == 4:   
#             exit()
#         else:
#             print('Opción no válida')
#     elif op == 2:
#         a = Cliente()
#     elif op == 3:
#         exit()
#     else:
#         print('Opción no válida')


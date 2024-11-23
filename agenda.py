import pandas as pd  # Importa la librería pandas, que será utilizada para gestionar datos en formato DataFrame.

class Agenda:
    def __init__(self, archivo_csv='POO/agenda_POO.csv'):
        """
        Método constructor. Inicializa la clase Agenda. 
        Carga los datos desde un archivo CSV si existe, o crea uno nuevo si no.
        """
        self.archivo_csv = archivo_csv  # Define la ruta del archivo CSV donde se guardarán los contactos.
        try:
            self.df = pd.read_csv(self.archivo_csv)  # Intenta cargar el CSV si existe.
        except FileNotFoundError:
            # Si el archivo no existe, se crea un DataFrame vacío con las columnas necesarias.
            self.df = pd.DataFrame(columns=['Nombre', 'Correo', 'Telefono'])
            self.df.to_csv(self.archivo_csv, index=False)  # Guarda el DataFrame vacío en un nuevo archivo CSV.
        self.menu()  # Llama al método menu() que mostrará las opciones al usuario.

    def Agregar(self):
        """
        Método para añadir un nuevo contacto a la agenda.
        Solicita nombre, correo y teléfono del contacto, y lo guarda en el archivo CSV.
        """
        nombre = input("Ingresa su nombre: ")  # Pide al usuario que ingrese el nombre del contacto.
        correo = input("Ingresa su correo: ")  # Pide al usuario que ingrese el correo del contacto.
        telefono = input("Ingresa su telefono: ")  # Pide al usuario que ingrese el teléfono del contacto.
        
        # Crea un nuevo DataFrame con los datos ingresados por el usuario.
        nuevo_dato = pd.DataFrame({'Nombre': [nombre], 'Correo': [correo], 'Telefono': [telefono]})
        
        # Agrega el nuevo contacto al DataFrame existente que ya contiene otros contactos.
        self.df = pd.concat([self.df, nuevo_dato], ignore_index=True)
        
        # Guarda el DataFrame actualizado en el archivo CSV.
        self.df.to_csv(self.archivo_csv, index=False)
        print(f"Datos guardados correctamente en {self.archivo_csv}")  # Mensaje de confirmación.
        print(self.df)  # Muestra todos los contactos actualmente guardados.
        
    def Mostrar(self):
        """
        Método para mostrar un contacto en específico.
        Pide el nombre del contacto y lo busca en el DataFrame.
        """
        nombre = input("Ingrese el nombre del contacto que desea mostrar: ")  # Pide el nombre a buscar.
        contacto = self.df[self.df['Nombre'] == nombre]  # Filtra el DataFrame por el nombre ingresado.
        if not contacto.empty:
            print(contacto)  # Si el contacto existe, lo muestra.
        else:
            print(f"No se encontró el contacto con el nombre {nombre}.")  # Si no existe, muestra un mensaje de error.

    def Lista(self):
        """
        Método para mostrar la lista completa de contactos.
        """
        print(self.df)  # Imprime todos los contactos almacenados en el DataFrame.

    def Eliminar(self):
        """
        Método para eliminar un contacto por nombre.
        Solicita el nombre del contacto y lo elimina del DataFrame y del archivo CSV.
        """
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")  # Pide el nombre del contacto.
        if nombre in self.df['Nombre'].values:  # Comprueba si el nombre existe en el DataFrame.
            self.df = self.df[self.df['Nombre'] != nombre]  # Elimina el contacto filtrando el DataFrame.
            self.df.to_csv(self.archivo_csv, index=False)  # Guarda los cambios en el archivo CSV.
            print(f"Contacto {nombre} eliminado.")  # Confirma que el contacto ha sido eliminado.
        else:
            print(f"No se encontró el contacto con el nombre {nombre}.")  # Mensaje de error si no se encuentra.

    def Editar(self):
        """
        Método para editar un contacto existente.
        Permite al usuario cambiar el nombre, correo o teléfono del contacto.
        """
        nombre = input("Ingrese el nombre del contacto que desea editar: ")  # Pide el nombre del contacto.
        if nombre in self.df['Nombre'].values:  # Verifica si el contacto existe.
            # Solicita los nuevos datos para el contacto.
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_correo = input("Ingrese el nuevo correo: ")
            nuevo_telefono = input("Ingrese el nuevo telefono: ")
            # Actualiza los datos del contacto en el DataFrame.
            self.df.loc[self.df['Nombre'] == nombre, ['Nombre', 'Correo', 'Telefono']] = [nuevo_nombre, nuevo_correo, nuevo_telefono]
            self.df.to_csv(self.archivo_csv, index=False)  # Guarda los cambios en el archivo CSV.
            print(f"Contacto {nombre} editado.")  # Confirma la edición.
        else:
            print(f"No se encontró el contacto con el nombre {nombre}.")  # Si no se encuentra, muestra un error.

    def menu(self):
        """
        Método que muestra el menú de opciones al usuario.
        Permite navegar entre las diferentes funcionalidades de la agenda.
        """
        while True:
            # Muestra el menú con las opciones disponibles.
            print("\nMenu:")
            print("\t1. Agregar contacto")
            print("\t2. Mostrar contacto")
            print("\t3. Lista de contactos")
            print("\t4. Eliminar contactos")
            print("\t5. Editar contactos")
            print("\t6. Salir")
            op = input("Seleccione una opción: ")  # Pide al usuario que seleccione una opción.
            
            # Dependiendo de la opción seleccionada, llama al método correspondiente.
            if op == '1':
                self.Agregar()
            elif op == '2':
                self.Mostrar()
            elif op == '3':
                self.Lista()
            elif op == '4':
                self.Eliminar()
            elif op == '5':
                self.Editar()
            elif op == '6':
                exit()  # Sale del programa si selecciona la opción 6.
            else:
                print("Opción no válida. Por favor, intente nuevamente.")  # Si elige una opción inválida, lo notifica.

# Bucle que crea una nueva instancia de la clase Agenda y muestra el menú.
while True:
    agenda = Agenda()  # Se crea una nueva instancia de la agenda, lo que llama al constructor y muestra el menú.

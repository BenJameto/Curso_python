class Saludos:
    """
    Esta clase tendra dos funciones, buenos_dias y adios
    Ambas funciones recibiran como parametro un nombre
    """
    def buenos_dias(self, nombre):
        """Esta funcion sirve para dar los buenos dias a una persona"""
        print("buenos dias {}".format(nombre))

    def adios(self, nombre):
        """Esta funcion sirve para despedirnos de una persona"""
        print("nos vemos luego "+ nombre)
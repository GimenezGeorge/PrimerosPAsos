class Producto:
	def __init__(self, nombre, precio):
		self.__nombre = nombre
		self.__precio = precio
		self.__primera_necesidad = primera_necesidad

	def get_nombre(self):
		return self.__nombre

	def get_primera_necesidad(self):
		return self.__primera_necesidad

	def get_precio(self):
		if primera_necesidad():
			return self.__precio*self.__primera_necesidad
			
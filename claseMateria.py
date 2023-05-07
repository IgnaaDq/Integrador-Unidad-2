class Materia: 
	__DNI = ""
	__nombre = ""
	__fecha = ""
	__nota = 0.0
	__aprobacion = ""

	def __init__(self, dni:str, nom:str, fecha:str, nota:str, apr:str)->None:
		self.__DNI = dni
		self.__nombre = nom
		self.__fecha = fecha
		self.__nota = float(nota)
		self.__aprobacion = apr

	def __str__(self)->str:
		return f"{self.__DNI, self.__nombre, self.__fecha, self.__nota, self.__aprobacion}"

	def getNombre(self)->str:
		return self.__nombre
	
	def getAprobacion(self)->str:
		return self.__aprobacion
	
	def getNota(self)->float:
		return self.__nota
	
	def getDni(self)->str:
		return self.__DNI
	
	def getFecha(self)->str:
		return self.__fecha

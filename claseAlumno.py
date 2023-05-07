class Alumno:
	__DNI = ""
	__apellido = ""
	__nombre = ""
	__carrera = ""
	__año = 0

	def __init__(self, dni:str, ap:str, nom:str, carr:str, anio:str)->None:
		self.__DNI = dni
		self.__apellido = ap
		self.__nombre = nom
		self.__carrera = carr
		self.__año = int(anio)

	def __str__(self)->str:
		return f"{self.__DNI, self.__apellido, self.__nombre, self.__carrera, self.__año}"
	
	def getDni(self)->str:
		return self.__DNI
	
	def getNombrecompleto(self)->str:
		return f"{self.__apellido} {self.__nombre}"
	
	def getAño(self)->int:
		return self.__año
	
	def __lt__(self, otro: "Alumno")->bool:
		retorno = False
		if self.__año<otro.__año:
			retorno = not retorno
		elif self.__año == otro.__año:
			if self.__apellido < otro.__apellido:
				retorno = not retorno
			elif self.__apellido == otro.__apellido:
				return self.__nombre<otro.__nombre
		return retorno



	

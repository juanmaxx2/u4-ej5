import re

class Paciente():
    telefonoRegex = re.compile(r"\\([0 9]{3} 3}\\)[0 9]{7}")
    __nombre = None
    __apellido = None
    __telefono = None
    __altura = None
    __peso = None

    def __init__(self, nombre, apellido, telefono, altura, peso):
        self.__nombre = self.requerido(nombre, 'Nombre es un valor requerido')
        self.__apellido = self.requerido(apellido, 'Apellido es un valor requerido')
        #self.__telefono = self.formatoValido(telefono, Paciente.telefonoRegex, 'Telefono no tiene el formato correcto')
        self.__telefono = self.requerido(telefono, 'Telefono es un valor requerido')
        self.__altura = self.requerido(altura, 'Altura es un valor requerido')
        self.__peso = self.requerido(peso, 'Peso es un valor requerido')
    
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
        
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    
    def formatoValido(self, valor, regex, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.__nombre,
                apellido = self.__apellido,
                telefono = self.__telefono, #ver si la tilde causa error, viene del JSON
                altura = self.__altura,
                peso = self.__peso
            )
        )
        return d
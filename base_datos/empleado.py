class Empleado : # Clase principal de Empleado
    def __init__(self, nombre,apellido,direccion,edad,cargo,salario):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.edad = edad
        self.cargo = cargo
        self.sueldo = salario

# Clase Programador hereda de Empleado
class Programador(Empleado):
    def __init__(self, nombre,apellido,direccion,edad,cargo,salario):
        super().__init__(nombre,apellido,direccion,edad,cargo,salario)

# Calculo de sueldo de un Programador
    def calculo_del_sueldo(self):
        self.sueldo = self.sueldo*1.5
        self.sueldo = round(self.sueldo,2)
        return self.sueldo
    
# Hereda de Empleado, analista parecida a Programador
class Analista(Empleado):
    def __init__(self, nombre,apellido,direccion,edad,cargo,salario):
        super().__init__(nombre,apellido,direccion,edad,cargo,salario)

# Calculo de sueldo de un analista
    def calculo_del_sueldo(self):
        self.sueldo = self.sueldo*1.3
        self.sueldo = round(self.sueldo,2)
        return self.sueldo



class Empleado : # Clase principal de Empleado
    def __init__(self, nombre,sueldo,cargo):
        self.nombre = nombre
        self.sueldo = sueldo
        self.cargo = cargo
    # Calculo de sueldo del empleado promedio
    def calculo_del_sueldo(self):
        self.sueldo = self.sueldo*1.1
        self.sueldo = round(self.sueldo,2)
        return self.sueldo

# Clase Programador hereda de Empleado
class Programador(Empleado):
    def __init__(self, nombre,sueldo,cargo):
        super().__init__(nombre,sueldo,cargo)

# Calculo de sueldo de un Programador
    def calculo_del_sueldo(self):
        self.sueldo = self.sueldo*1.5
        self.sueldo = round(self.sueldo,2)
        return self.sueldo
# Hereda de Empleado, analista parecida a Programador
class Analista(Empleado):
    def __init__(self, nombre,sueldo,cargo):
        super().__init__(nombre,sueldo,cargo)

# Calculo de sueldo de un analista
    def calculo_del_sueldo(self):
        self.sueldo = self.sueldo*1.3
        self.sueldo = round(self.sueldo,2)
        return self.sueldo



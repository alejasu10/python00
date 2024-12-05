## ejercicio de POO 
### RETO: Sistema para calcular las nóminas 
# Acaba de irse de la empresa la programadora que se encargaba del desarrollo del proyecto de nóminas. 
# Ella ya ha creado una clase Sistema_Nominas, y ha hecho los primeros diseños para las clases de Empleados.
# Usando su trabajo ya hecho, termina el programa.


class Empleado : # Clase principal de Empleado
    def __init__(self, nombre,sueldo,cargo):
        self.nombre = nombre
        self.sueldo = sueldo
        self.cargo = cargo
    def crear_empleado():       # metodo para crear un nuevo empleado
        nombre=input("ingrese el nombre del nuevo empleado: ")
        nombre=nombre.capitalize()
        nuevo_sueldo=float(input("ingrese el sueldo del nuevo empleado: "))
        nuevo_cargo=input("ingrese el cargo del nuevo empleado: ")
        empleados=[nombre,nuevo_sueldo,nuevo_cargo] 
        return empleados
    
    def Nomina(self): # imprime la nomina del empleado en una tabla
        tabla = """\
        +-----------------------------------------------+
        | Nombre            Sueldo           Cargo      |
        |-----------------------------------------------|
        | {:<9} {:>14} $ {:>15}    |
        +-----------------------------------------------+\
        """# estructura de la tabla
        datos_Nomina = tabla.format(
            self.nombre,# nombre del empleado
            Empleado.calculo_del_sueldo(self),# calculo del sueldo
            self.cargo # cargo
            
        )
        return datos_Nomina # imprime una tabla con la info de la nomina
    
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
    
    def Nomina_Programador(self): # imprime la nomina del empleado en una tabla
        tabla = """\
        +-----------------------------------------------+
        | Nombre            Sueldo           Cargo      |
        |-----------------------------------------------|
        | {:<9} {:>14} $ {:>15}    |
        +-----------------------------------------------+\
        """# estructura de la tabla
        datos_Nomina = tabla.format(
            self.nombre,# nombre del empleado
            Programador.calculo_del_sueldo(self),# calculo del sueldo
            self.cargo # cargo
            
        )
        return datos_Nomina # imprime una tabla con la info de la nomina
# Hereda de Empleado, analista parecida a Programador
class Analista(Empleado):
    def __init__(self, nombre,sueldo,cargo):
        super().__init__(nombre,sueldo,cargo)

# Calculo de sueldo de un analista
    def calculo_del_sueldo(self):
        self.sueldo = self.sueldo*1.3
        self.sueldo = round(self.sueldo,2)
        return self.sueldo
    
    def Nomina_Analista(self): # imprime la nomina del empleado en una tabla
        tabla = """\
        +-----------------------------------------------+
        | Nombre            Sueldo           Cargo      |
        |-----------------------------------------------|
        | {:<9} {:>14} $ {:>15}    |
        +-----------------------------------------------+\
        """# estructura de la tabla
        datos_Nomina = tabla.format(
            self.nombre,# nombre del empleado
            Analista.calculo_del_sueldo(self),# calculo del sueldo
            self.cargo # cargo
            
        )
        return datos_Nomina # imprime una tabla con la info de la nomina

# Ejercicio de Base de datos.

Basado en el ejercicio de la clase de POO, se pide:

Crear una base de datos para gestionar los empleados de una empresa.

La base de datos debe permitir:
# - Crear un empleado
# - Modificar un empleado
# - Eliminar un empleado
# - Listar todos los empleados
# - Buscar un empleado
# - Salir

Breve explicación de cómo se ha realizado el ejercicio:

--Se creo una clase para la base de datos, la cual contiene los metodos para agregar,modificar,
eliminar, listar y buscar empleados.

--Se crea una clase para los empleados, la cual contiene los atributos y 2 clases para los empleados
de tipo programador y analista, cada una 
hereda de la clase empleado.

-- Se definieron funciones adicionales para la busqueda,modificacion y creacion del objeto empleado.

--La base de datos interactua con el usuario por medio de un menu, el cual a su vez interactua con 
las funciones adiciones de creacion,modificacion y busqueda.

-- Las funciones adicionales interactuan con el objeto empleado durante la creacion, para luego ser 
enviado al main y una vez ahi el main lo envia a la base de datos.

La base de datos cuenta con una tabla llamada "Empleado" la cual contiene los campos:

#"ID"," ","NOMBRE"," ","APELLIDO"," ","DIRECCION"," ","EDAD"," ","CARGO"," ","SALARIO"

--El ID es autoincremental, el nombre y apellido son obligatorios, la direccion es opcional, la edad es obligatoria
y el cargo y salario son opcionales.

-- El cargo  puede ser:
# - Programador
# - Analista

- el cargo es opcional pero si se ingresa el cargo, el salario varia de acuerdo al cargo., si el cargo
no se introduce tomara valor predeterminado por la clase empleado.

-- Los cargos listados tienen un incremento en el salario, la idea es aplicar polimorfismo a la hora de 
generar el salario.

# se uso:
-- Clases, con Herencia y polimorfismo
-- Funciones
-- Base de datos

# El ejercicio se puede ampliar, agregando mas funcionalidades,metodos y otras clases,
se pueden añadir mas cargos, calculo de horas extras, horas trabajadas, etc.


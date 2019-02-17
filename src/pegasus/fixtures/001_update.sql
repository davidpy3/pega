# Añade la columna id
ALTER TABLE Planilla ADD id INT IDENTITY;
ALTER TABLE Planilla_Trab ADD id INT IDENTITY;
ALTER TABLE Planilla_Detalle ADD id INT IDENTITY;
ALTER TABLE Marcaciones ADD id INT IDENTITY;
ALTER TABLE Meta ADD id INT IDENTITY;
ALTER TABLE nivel_remunerativo ADD id INT IDENTITY;
ALTER TABLE fuente_financ ADD id INT IDENTITY;

# Alimina la restricción de llave primaria
# ALTER TABLE Planilla_Trab DROP CONSTRAINT PK_Planilla_Trab;

# Define la columna id como llave primaria
# ALTER TABLE Planilla_Trab ADD CONSTRAINT PK_Planilla_Trab PRIMARY KEY(id);

# Mantener llave primaria
# ALTER TABLE Planilla_Trab ADD CONSTRAINT AK_Planilla_Trab UNIQUE (N_Expediente, Ano_eje, DNI);

# Lista las restricciones de una tabla
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE TABLE_NAME = 'Planilla_Trab';

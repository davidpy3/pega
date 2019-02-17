# coding=utf-8
SITUACION_BAJA = "13"
SITUACION_ALTA = "11"
SITUACION_CHOICES = ((SITUACION_BAJA, 'Baja'),
                     (SITUACION_ALTA, 'Alta'))

SEXO_CHOICES = (("0", 'Hombre'),
                ("1", 'Mujer'))

ESTADO_CHOICES = (("1", 'Nombrado'),
                  ("4", 'Construcción civil'),
                  ("5", 'CAS'),
                  ("8", 'Pensionista'),
                  ("9", 'Contratado eventual'))

MARCA_CHOICES = (("1", "0", "1", 'Ingreso'),
                 ("1", "0", "0", 'Refrigerio'),
                 ("1", "1", "1", 'Regreso'),
                 ("1", "1", "0", 'Salida'),
                 )

PLANILLA_DETALLE_IND_CHOICES = (("1", 'Ingresos'),
                                ("2", 'Descuentos'),
                                ("3", 'Aportaciones'),
                                )
ESTADO_ORDENES = (("0", 'Borrador'),
                  ("1", 'Tramite'),
                  ("4", 'Coizadp'),
                  ("9", 'Generado'),
                  )
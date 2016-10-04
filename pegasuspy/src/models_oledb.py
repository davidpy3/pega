from django.db import models


class Cas(models.Model):
    dni = models.CharField(max_length=8, blank=True)
    monto = models.DecimalField(db_column='MONTO', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    comi_afp = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    prima_afp = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    des_afp = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    snp = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ubigeo = models.IntegerField(blank=True, null=True)
    codi_afp = models.CharField(max_length=2, blank=True)
    rimac = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    num_comp = models.CharField(max_length=8, blank=True)
    ruc = models.CharField(max_length=11, blank=True)
    mes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CAS'


class Calendario(models.Model):
    ano_eje = models.CharField(max_length=4)
    mes_eje = models.CharField(max_length=2)
    fuente_financ = models.CharField(max_length=2)
    tipo_calendario = models.CharField(max_length=1)
    sec_fun = models.CharField(max_length=4)
    meta = models.CharField(max_length=5)
    total_meta = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Calendario'


class CalendarioDet(models.Model):
    ano_eje = models.ForeignKey('EspecificaDet', db_column='ano_eje')
    mes_eje = models.ForeignKey(Calendario, db_column='mes_eje')
    fuente_financ = models.ForeignKey(Calendario, db_column='fuente_financ')
    tipo_calendario = models.ForeignKey(Calendario, db_column='tipo_calendario')
    sec_fun = models.ForeignKey(Calendario, db_column='sec_fun')
    meta = models.CharField(max_length=5)
    tipo_transaccion = models.ForeignKey('EspecificaDet', db_column='tipo_transaccion')
    generica = models.ForeignKey('EspecificaDet', db_column='generica')
    subgenerica = models.ForeignKey('EspecificaDet', db_column='subgenerica')
    subgenerica_det = models.ForeignKey('EspecificaDet', db_column='subgenerica_det')
    especifica = models.ForeignKey('EspecificaDet', db_column='especifica')
    especifica_det = models.ForeignKey('EspecificaDet', db_column='especifica_det')
    monto = models.DecimalField(max_digits=18, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'Calendario_det'


class Cargo(models.Model):
    id_cargo = models.IntegerField(db_column='ID_cargo')  # Field name made lowercase.
    cod_pdt = models.CharField(max_length=6, blank=True)
    nom_cargo = models.CharField(max_length=70, blank=True)
    nivel = models.IntegerField(blank=True, null=True)
    orden_firma = models.IntegerField(blank=True, null=True)
    abreviatura = models.CharField(max_length=15, blank=True)
    abrev = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'Cargo'


class CategoriaCcv(models.Model):
    categoria = models.CharField(max_length=2)
    codigo = models.CharField(max_length=4)
    valor = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    porcen = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Categoria_CCV'


class CodigoPdt(models.Model):
    cod_pdt = models.CharField(primary_key=True, max_length=4)
    nombre_pdt = models.CharField(max_length=150, blank=True)

    class Meta:
        managed = False
        db_table = 'Codigo_PDT'


class Configuracion(models.Model):
    ano_eje = models.IntegerField()
    ruc_entidad = models.CharField(db_column='RUC_entidad', max_length=11)  # Field name made lowercase.
    nombre_entidad = models.CharField(max_length=50, blank=True)
    direccion_entidad = models.CharField(max_length=200, blank=True)
    telefono_entidad = models.CharField(max_length=20, blank=True)
    igv = models.DecimalField(db_column='IGV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    uit = models.DecimalField(db_column='UIT', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minimo_vital = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ano_doc = models.CharField(max_length=255, blank=True)
    ess_vida = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    porcentaje_ir = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True)
    tiene_gratif = models.IntegerField(blank=True, null=True)
    tiene_vacac = models.IntegerField(blank=True, null=True)
    tiene_escol = models.IntegerField(blank=True, null=True)
    nro_gratif = models.IntegerField(blank=True, null=True)
    nro_vacac = models.IntegerField(blank=True, null=True)
    nro_escol = models.IntegerField(blank=True, null=True)
    nro_uit = models.IntegerField(blank=True, null=True)
    nro_sueldos = models.IntegerField(blank=True, null=True)
    nro_dias_escol = models.IntegerField(blank=True, null=True)
    nro_dias_gratif = models.IntegerField(blank=True, null=True)
    nro_dias_mes = models.IntegerField(blank=True, null=True)
    mes_inicio_escol = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Configuracion'


class CotizaDetalle(models.Model):
    ano_eje = models.CharField(max_length=4)
    clasifica = models.CharField(max_length=1)
    n_requer = models.IntegerField()
    n_cotiza = models.IntegerField()
    item = models.IntegerField()
    ruc_item = models.CharField(max_length=11)
    id_item = models.CharField(max_length=13)
    detalle_item = models.CharField(max_length=7000, blank=True)
    desc_calidad = models.CharField(max_length=1000, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_postor = models.DecimalField(max_digits=14, decimal_places=6, blank=True, null=True)
    participa = models.CharField(max_length=1)
    ganador_item = models.CharField(max_length=1, blank=True)
    id_unidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Cotiza_detalle'


class Cotizacion(models.Model):
    ano_eje = models.ForeignKey('Requerimiento', db_column='ano_eje')
    clasifica = models.ForeignKey('Requerimiento', db_column='clasifica')
    n_requer = models.ForeignKey('Requerimiento', db_column='n_requer')
    n_cotiza = models.IntegerField()
    fecha = models.DateTimeField()
    condiciones = models.CharField(max_length=1000, blank=True)
    ruc_postor = models.ForeignKey('Proveedores', db_column='RUC_postor')  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=14, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(max_length=200, blank=True)
    ganador = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'Cotizacion'

class GrupoBienSeace(models.Model):
    tipo_bien = models.CharField(max_length=1)
    grupo_bien = models.CharField(max_length=2)
    nombre_gru = models.CharField(max_length=500, blank=True)
    alcance_gru = models.CharField(max_length=500, blank=True)
    flag_activ = models.CharField(max_length=1, blank=True)
    flag_sbn = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'Grupo_bien_SEACE'

class HccDetalle(models.Model):
    ano_eje = models.CharField(max_length=4)
    n_hcc = models.IntegerField()
    id_clasificador = models.CharField(max_length=7)
    monto = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True)
    fase = models.CharField(max_length=1, blank=True)
    correla = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'HCC_Detalle'

class HijosObra(models.Model):
    docuiden = models.CharField(max_length=8)
    nhijo = models.IntegerField()
    apat = models.CharField(max_length=20, blank=True)
    amat = models.CharField(max_length=20, blank=True)
    nombres = models.CharField(max_length=20, blank=True)
    fechanac = models.DateTimeField(blank=True, null=True)
    n_partida = models.CharField(max_length=50, blank=True)
    centro_estudios = models.CharField(max_length=80, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'Hijos_Obra'

class Horario(models.Model):
    tipo_hor = models.CharField(max_length=1)
    turno = models.CharField(db_column='Turno', max_length=1) # Field name made lowercase.
    registro = models.CharField(db_column='Registro', max_length=1) # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=30, blank=True) # Field name made lowercase.
    desde = models.DateTimeField(db_column='Desde', blank=True, null=True) # Field name made lowercase.
    hasta = models.DateTimeField(db_column='Hasta', blank=True, null=True) # Field name made lowercase.
    tolerancia = models.IntegerField(db_column='Tolerancia', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Horario'

class ItemSeace(models.Model):
    tipo_bien = models.CharField(max_length=1)
    grupo_bien = models.CharField(max_length=2)
    clase_bien = models.CharField(max_length=2)
    familia_bien = models.CharField(max_length=4)
    item_bien = models.CharField(max_length=4)
    nombre_item = models.CharField(max_length=1000, blank=True)
    flag_activo = models.CharField(max_length=1, blank=True)
    tipo_unidad = models.IntegerField(blank=True, null=True)
    fecha_alta = models.DateTimeField(blank=True, null=True)
    user_registra = models.CharField(max_length=8, blank=True)
    id_item = models.CharField(max_length=13, blank=True)
    divisionaria = models.CharField(max_length=11, blank=True)
    class Meta:
        managed = False
        db_table = 'ITEM_SEACE'

class ItemBienSeace(models.Model):
    tipo_bien = models.CharField(max_length=1)
    grupo_bien = models.CharField(max_length=2)
    clase_bien = models.CharField(max_length=2)
    familia_bien = models.CharField(max_length=4)
    item_bien = models.CharField(max_length=4)
    nombre_item = models.CharField(max_length=1000, blank=True)
    flag_activo = models.CharField(max_length=1, blank=True)
    tipo_unidad = models.ForeignKey('UnidadMef', db_column='tipo_unidad', blank=True, null=True)
    fecha_alta = models.DateTimeField(blank=True, null=True)
    user_registra = models.CharField(max_length=8, blank=True)
    id_item = models.CharField(unique=True, max_length=13, blank=True)
    divisionaria = models.CharField(max_length=11, blank=True)
    class Meta:
        managed = False
        db_table = 'Item_bien_SEACE'

class JudicialObra(models.Model):
    docuiden = models.CharField(max_length=8)
    docudem = models.CharField(max_length=8)
    nom_deman = models.CharField(max_length=100, blank=True)
    desc_judi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    porc_judi = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_abono = models.CharField(max_length=1, blank=True)
    cuenta_abono = models.CharField(max_length=50, blank=True)
    ind_desc = models.CharField(max_length=2, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'Judicial_Obra'

class Markantoni(models.Model):
    dni = models.CharField(db_column='DNI', max_length=8) # Field name made lowercase.
    fecha_hora = models.DateTimeField()
    tipo_hor = models.CharField(max_length=1, blank=True)
    turno = models.CharField(max_length=1, blank=True)
    registro = models.CharField(max_length=1, blank=True)
    tipo = models.CharField(max_length=1, blank=True)
    observ = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'MarkAntoni'

class Ordenes(models.Model):
    ano_eje = models.CharField(max_length=4)
    n_orden = models.IntegerField()
    tipo = models.CharField(max_length=1)
    cod_doc = models.CharField(max_length=3)
    num_doc = models.CharField(max_length=15)
    fecha = models.DateTimeField()
    sec_func = models.CharField(max_length=4)
    fuente_financ = models.CharField(max_length=2)
    ruc_prov = models.CharField(db_column='RUC_prov', max_length=11) # Field name made lowercase.
    condiciones = models.CharField(max_length=1000, blank=True)
    ruc_fact = models.CharField(db_column='RUC_fact', max_length=11, blank=True) # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    justificacion = models.CharField(max_length=400, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    est_cont = models.CharField(max_length=1, blank=True)
    n_reg_siaf = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True)
    fech_comp = models.DateTimeField(blank=True, null=True)
    referencia = models.CharField(max_length=50, blank=True)
    ano_requer = models.CharField(max_length=4, blank=True)
    fecha_anul = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ORDENES'

class Orden(models.Model):
    ano_eje = models.CharField(max_length=4)
    n_orden = models.IntegerField()
    tipo = models.CharField(max_length=1)
    cod_doc = models.CharField(max_length=3)
    num_doc = models.CharField(max_length=15)
    fecha = models.DateTimeField()
    sec_func = models.CharField(max_length=4)
    fuente_financ = models.CharField(max_length=2)
    ruc_prov = models.CharField(db_column='RUC_prov', max_length=11) # Field name made lowercase.
    condiciones = models.CharField(max_length=1000, blank=True)
    ruc_fact = models.CharField(db_column='RUC_fact', max_length=11, blank=True) # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    justificacion = models.CharField(max_length=400, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    est_cont = models.CharField(max_length=1, blank=True)
    n_reg_siaf = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True)
    fech_comp = models.DateTimeField(blank=True, null=True)
    referencia = models.CharField(max_length=50, blank=True)
    ano_requer = models.CharField(max_length=4, blank=True)
    fecha_anul = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Orden'

class OrdenDetalle(models.Model):
    ano_eje = models.ForeignKey(Orden, db_column='ano_eje')
    n_orden = models.ForeignKey(Orden, db_column='n_orden')
    tipo = models.ForeignKey(Orden, db_column='tipo')
    item = models.IntegerField()
    num_doc = models.CharField(max_length=15)
    especifica = models.CharField(max_length=16, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saldo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factor = models.IntegerField(blank=True, null=True)
    salida = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    id_item = models.CharField(max_length=13, blank=True)
    unidad = models.CharField(max_length=4, blank=True)
    desc_insumo = models.CharField(max_length=7000, blank=True)
    desc_calidad = models.CharField(max_length=1000, blank=True)
    precio_adj = models.DecimalField(max_digits=14, decimal_places=6, blank=True, null=True)
    cant_ing = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    temporal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unidad_alm = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'Orden_detalle'

class Organo(models.Model):
    cod_organo = models.CharField(max_length=2)
    nom_organo = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'Organo'

class Pecosa(models.Model):
    ano_eje = models.CharField(max_length=4)
    n_pecosa = models.IntegerField()
    ano_eje_o = models.CharField(max_length=4, blank=True)
    n_orden = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True)
    fecha = models.DateTimeField(blank=True, null=True)
    entregar_a = models.CharField(max_length=100, blank=True)
    n_siaf = models.IntegerField(blank=True, null=True)
    serie_fact = models.IntegerField(blank=True, null=True)
    num_fact = models.BigIntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=300, blank=True)
    class Meta:
        managed = False
        db_table = 'PECOSA'

class PatriMovDetalle(models.Model):
    ano_eje = models.ForeignKey('PatriMovimiento', db_column='ano_eje')
    tipo_mov = models.ForeignKey('PatriMovimiento', db_column='tipo_mov')
    num_mov = models.ForeignKey('PatriMovimiento', db_column='num_mov')
    codbien = models.ForeignKey('Mbienes0', db_column='codbien')
    correla = models.ForeignKey('Mbienes0', db_column='correla')
    ubica_bien = models.CharField(max_length=13, blank=True)
    class Meta:
        managed = False
        db_table = 'Patri_Mov_Detalle'

class PatriMovimiento(models.Model):
    ano_eje = models.CharField(max_length=4)
    tipo_mov = models.CharField(max_length=1)
    num_mov = models.CharField(max_length=7)
    fecha_reg = models.DateTimeField(blank=True, null=True)
    fecha_mov = models.DateTimeField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    fecha_retorno = models.DateTimeField(blank=True, null=True)
    retorno = models.CharField(max_length=1, blank=True)
    empl_origen = models.CharField(max_length=8, blank=True)
    empl_destino = models.CharField(max_length=8, blank=True)
    local_origen = models.CharField(max_length=3, blank=True)
    local_destino = models.CharField(max_length=3, blank=True)
    desc_destino = models.CharField(max_length=70, blank=True)
    area_origen = models.CharField(max_length=5, blank=True)
    area_destino = models.CharField(max_length=5, blank=True)
    oficina_origen = models.CharField(max_length=5, blank=True)
    oficina_destino = models.CharField(max_length=5, blank=True)
    motivo = models.CharField(max_length=500, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    selec = models.CharField(max_length=1, blank=True)
    observaciones = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'Patri_Movimiento'

class PersonalDscto(models.Model):
    dni = models.CharField(max_length=8)
    codigo = models.CharField(max_length=4)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_ini = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    glosa = models.CharField(max_length=80, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'Personal_dscto'

class Proceso(models.Model):
    ano_eje = models.CharField(max_length=4)
    clasifica = models.CharField(max_length=1)
    n_requer = models.IntegerField()
    item = models.IntegerField()
    ano_proceso = models.CharField(max_length=4, blank=True)
    tipo_proc = models.CharField(max_length=3, blank=True)
    n_proc = models.IntegerField(blank=True, null=True)
    contrato = models.IntegerField(db_column='Contrato', blank=True, null=True) # Field name made lowercase.
    ruc_buena_pro = models.CharField(db_column='RUC_Buena_Pro', max_length=11, blank=True) # Field name made lowercase.
    fecha_lanza = models.DateTimeField(blank=True, null=True)
    fecha_venta = models.DateTimeField(blank=True, null=True)
    dias_venta = models.IntegerField(blank=True, null=True)
    fecha_adj = models.DateTimeField(db_column='Fecha_Adj', blank=True, null=True) # Field name made lowercase.
    monto_adj = models.DecimalField(db_column='Monto_Adj', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    id_comite = models.IntegerField(blank=True, null=True)
    justificacion = models.CharField(db_column='Justificacion', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Proceso'

class ProcesoTabla(models.Model):
    tipo_proceso = models.ForeignKey('ProcesoTipo', db_column='Tipo_proceso') # Field name made lowercase.
    clasifica = models.CharField(max_length=1)
    anno = models.IntegerField()
    mayor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    menor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Proceso_tabla'

class ProcesoTipo(models.Model):
    tipo_proceso = models.CharField(db_column='Tipo_proceso', max_length=3) # Field name made lowercase.
    nom_proceso = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'Proceso_tipo'


class Proveedores(models.Model):
    ruc = models.CharField(db_column='RUC', max_length=11)  # Field name made lowercase.
    nombre_razon = models.CharField(db_column='Nombre_Razon', max_length=150)  # Field name made lowercase.
    tipo_contrib = models.CharField(db_column='Tipo_Contrib', max_length=70, blank=True)  # Field name made lowercase.
    prof_oficio = models.CharField(db_column='Prof_Oficio', max_length=200, blank=True)  # Field name made lowercase.
    nombre_comercial = models.CharField(db_column='Nombre_Comercial', max_length=200, blank=True)  # Field name made lowercase.
    condicion_contrib = models.CharField(db_column='Condicion_Contrib', max_length=80, blank=True)  # Field name made lowercase.
    estado_contrib = models.CharField(db_column='Estado_Contrib', max_length=80, blank=True)  # Field name made lowercase.
    fecha_inscrip = models.DateTimeField(db_column='Fecha_Inscrip', blank=True, null=True)  # Field name made lowercase.
    fecha_inicio = models.DateTimeField(db_column='Fecha_Inicio', blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='Departamento', max_length=80, blank=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=80, blank=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=80, blank=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=120, blank=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=80, blank=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=30, blank=True)  # Field name made lowercase.
    acti_exterior = models.CharField(db_column='Acti_exterior', max_length=200, blank=True)  # Field name made lowercase.
    ciiu_principal = models.CharField(db_column='CIIU_Principal', max_length=80, blank=True)  # Field name made lowercase.
    ciiu_secun1 = models.CharField(db_column='CIIU_Secun1', max_length=80, blank=True)  # Field name made lowercase.
    ciiu_secun2 = models.CharField(db_column='CIIU_Secun2', max_length=80, blank=True)  # Field name made lowercase.
    nuevo_rus = models.CharField(db_column='Nuevo_RUS', max_length=20, blank=True)  # Field name made lowercase.
    buen_contrib = models.CharField(db_column='Buen_Contrib', max_length=220, blank=True)  # Field name made lowercase.
    agente_reten = models.CharField(db_column='Agente_Reten', max_length=220, blank=True)  # Field name made lowercase.
    agente_percep1 = models.CharField(db_column='Agente_Percep1', max_length=220, blank=True)  # Field name made lowercase.
    agente_percep2 = models.CharField(db_column='Agente_Percep2', max_length=220, blank=True)  # Field name made lowercase.
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'Proveedores'


class ProyInv(models.Model):
    ano_eje = models.CharField(max_length=4)
    id_proy = models.IntegerField()
    nombre = models.CharField(max_length=500, blank=True)
    nivel_gob = models.CharField(max_length=2, blank=True)
    snip = models.CharField(max_length=6, blank=True)
    funcion = models.CharField(max_length=2, blank=True)
    monto = models.CharField(max_length=10, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    fec_reg = models.DateTimeField(blank=True, null=True)
    departamento = models.CharField(max_length=2, blank=True)
    provincia = models.CharField(max_length=2, blank=True)
    distrito = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'Proy_Inv'


class Requerimientos(models.Model):
    ano_eje = models.CharField(max_length=4)
    clasifica = models.CharField(max_length=1)
    n_requer = models.IntegerField()
    fecha = models.DateTimeField()
    mes = models.IntegerField()
    sec_func = models.CharField(max_length=4, blank=True)
    act_proy = models.CharField(max_length=7, blank=True)
    componente = models.CharField(max_length=7, blank=True)
    fuente_financ = models.CharField(max_length=2, blank=True)
    descripcion = models.CharField(max_length=1000, blank=True)
    condiciones = models.CharField(max_length=1000, blank=True)
    total = models.DecimalField(db_column='TOTAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=1, blank=True)
    dni = models.CharField(db_column='DNI', max_length=8, blank=True)  # Field name made lowercase.
    id_cargo = models.IntegerField(db_column='ID_cargo', blank=True, null=True)  # Field name made lowercase.
    insitu = models.IntegerField(blank=True, null=True)
    arch_bases = models.CharField(max_length=200, blank=True)
    grupo = models.CharField(max_length=2, blank=True)
    clase = models.CharField(max_length=2, blank=True)
    proc_seleccion = models.CharField(max_length=10, blank=True)
    igv = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True)
    selec = models.CharField(max_length=1, blank=True)
    paac = models.IntegerField(blank=True, null=True)
    fecha_autoriza = models.DateTimeField(blank=True, null=True)
    tipo_proc = models.CharField(max_length=3, blank=True)
    n_proc = models.IntegerField(blank=True, null=True)
    est_seace = models.CharField(max_length=1, blank=True)
    fecha_base = models.DateTimeField(blank=True, null=True)
    contrato = models.IntegerField(blank=True, null=True)
    fecha_contrato = models.DateTimeField(blank=True, null=True)
    fecha_fin_contrato = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REQUERIMIENTOS'


class RequerDetalle(models.Model):
    ano_eje = models.CharField(max_length=4)
    clasifica = models.CharField(max_length=1)
    n_requer = models.IntegerField()
    item = models.IntegerField()
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    id_item = models.CharField(max_length=13)
    precio_ref = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    detalle = models.CharField(max_length=7000, blank=True)
    id_unidad = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Requer_detalle'

class Requerimiento(models.Model):
    ano_eje = models.CharField(max_length=4)
    clasifica = models.CharField(max_length=1)
    n_requer = models.IntegerField()
    fecha = models.DateTimeField()
    mes = models.IntegerField()
    sec_func = models.CharField(max_length=4, blank=True)
    act_proy = models.CharField(max_length=7, blank=True)
    componente = models.CharField(max_length=7, blank=True)
    fuente_financ = models.CharField(max_length=2, blank=True)
    descripcion = models.CharField(max_length=1000, blank=True)
    condiciones = models.CharField(max_length=1000, blank=True)
    total = models.DecimalField(db_column='TOTAL', max_digits=12, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    estado = models.CharField(max_length=1, blank=True)
    dni = models.CharField(db_column='DNI', max_length=8, blank=True) # Field name made lowercase.
    id_cargo = models.IntegerField(db_column='ID_cargo', blank=True, null=True) # Field name made lowercase.
    insitu = models.IntegerField(blank=True, null=True)
    arch_bases = models.CharField(max_length=200, blank=True)
    grupo = models.CharField(max_length=2, blank=True)
    clase = models.CharField(max_length=2, blank=True)
    proc_seleccion = models.CharField(max_length=10, blank=True)
    igv = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True)
    selec = models.CharField(max_length=1, blank=True)
    paac = models.IntegerField(blank=True, null=True)
    fecha_autoriza = models.DateTimeField(blank=True, null=True)
    tipo_proc = models.CharField(max_length=3, blank=True)
    n_proc = models.IntegerField(blank=True, null=True)
    est_seace = models.CharField(max_length=1, blank=True)
    fecha_base = models.DateTimeField(blank=True, null=True)
    contrato = models.IntegerField(blank=True, null=True)
    fecha_contrato = models.DateTimeField(blank=True, null=True)
    fecha_fin_contrato = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Requerimiento'


class T4588DdjjDet(models.Model):
    num_ruc = models.CharField(db_column='NUM_RUC', max_length=11)  # Field name made lowercase.
    per_decla = models.CharField(db_column='PER_DECLA', max_length=6)  # Field name made lowercase.
    num_cor_per = models.IntegerField(db_column='NUM_COR_PER', blank=True, null=True)  # Field name made lowercase.
    cod_cat_pre = models.CharField(db_column='COD_CAT_PRE', max_length=1)  # Field name made lowercase.
    cod_tip_doc_ide = models.CharField(db_column='COD_TIP_DOC_IDE', max_length=2)  # Field name made lowercase.
    num_doc_ide = models.CharField(db_column='NUM_DOC_IDE', max_length=15)  # Field name made lowercase.
    num_efe_lab = models.IntegerField(db_column='NUM_EFE_LAB', blank=True, null=True)  # Field name made lowercase.
    mto_tot_deveng = models.DecimalField(db_column='MTO_TOT_DEVENG', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mto_tot_pagado = models.DecimalField(db_column='MTO_TOT_PAGADO', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mto_tot_descuen = models.DecimalField(db_column='MTO_TOT_DESCUEN', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mto_tot_apo_tra = models.DecimalField(db_column='MTO_TOT_APO_TRA', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mto_tot_apo_emp = models.DecimalField(db_column='MTO_TOT_APO_EMP', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mto_tot_essalud = models.DecimalField(db_column='MTO_TOT_ESSALUD', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mto_tot_ingreso = models.DecimalField(db_column='MTO_TOT_INGRESO', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mto_tot_net_pag = models.DecimalField(db_column='MTO_TOT_NET_PAG', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_sit_pre = models.CharField(db_column='IND_SIT_PRE', max_length=1, blank=True)  # Field name made lowercase.
    cod_tip_pre = models.CharField(db_column='COD_TIP_PRE', max_length=2, blank=True)  # Field name made lowercase.
    cod_reg_salud = models.CharField(db_column='COD_REG_SALUD', max_length=2, blank=True)  # Field name made lowercase.
    cod_reg_pension = models.CharField(db_column='COD_REG_PENSION', max_length=2, blank=True)  # Field name made lowercase.
    num_ruc_eps = models.CharField(db_column='NUM_RUC_EPS', max_length=11, blank=True)  # Field name made lowercase.
    ind_consist = models.CharField(db_column='IND_CONSIST', max_length=1, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T4588DDJJ_DET'

class Tipovia(models.Model):
    tipovia = models.CharField(primary_key=True, max_length=2)
    nombre_via = models.CharField(max_length=50)
    abrev = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'Tipovia'

class Unidad(models.Model):
    id_unidad = models.CharField(db_column='ID_unidad', max_length=4) # Field name made lowercase.
    nom_unidad = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'Unidad'

class View1(models.Model):
    dni = models.CharField(db_column='DNI', max_length=8) # Field name made lowercase.
    expr2 = models.CharField(db_column='Expr2', max_length=120, blank=True) # Field name made lowercase.
    dia01 = models.DateTimeField(blank=True, null=True)
    dia02 = models.DateTimeField(blank=True, null=True)
    dia03 = models.DateTimeField(blank=True, null=True)
    dia04 = models.DateTimeField(blank=True, null=True)
    dia05 = models.DateTimeField(blank=True, null=True)
    dia06 = models.DateTimeField(blank=True, null=True)
    dia07 = models.DateTimeField(blank=True, null=True)
    dia08 = models.DateTimeField(blank=True, null=True)
    dia09 = models.DateTimeField(blank=True, null=True)
    dia10 = models.DateTimeField(blank=True, null=True)
    dia11 = models.DateTimeField(blank=True, null=True)
    dia12 = models.DateTimeField(blank=True, null=True)
    dia13 = models.DateTimeField(blank=True, null=True)
    dia14 = models.DateTimeField(blank=True, null=True)
    dia15 = models.DateTimeField(blank=True, null=True)
    dia16 = models.DateTimeField(blank=True, null=True)
    dia17 = models.DateTimeField(blank=True, null=True)
    dia18 = models.DateTimeField(blank=True, null=True)
    dia19 = models.DateTimeField(blank=True, null=True)
    dia20 = models.DateTimeField(blank=True, null=True)
    dia21 = models.DateTimeField(blank=True, null=True)
    dia22 = models.DateTimeField(blank=True, null=True)
    dia23 = models.DateTimeField(blank=True, null=True)
    dia24 = models.DateTimeField(blank=True, null=True)
    dia25 = models.DateTimeField(blank=True, null=True)
    dia26 = models.DateTimeField(blank=True, null=True)
    dia27 = models.DateTimeField(blank=True, null=True)
    dia28 = models.DateTimeField(blank=True, null=True)
    dia29 = models.DateTimeField(blank=True, null=True)
    dia30 = models.DateTimeField(blank=True, null=True)
    dia31 = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'VIEW1'

class Valorizacion(models.Model):
    ano_eje = models.CharField(max_length=4)
    tipo = models.CharField(max_length=1)
    n_orden = models.IntegerField()
    n_valor = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    tipo_valor = models.CharField(max_length=1)
    porc_prop = models.IntegerField(blank=True, null=True)
    porc_valor = models.IntegerField(blank=True, null=True)
    monto_prop = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_valor = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'Valorizacion'

class View1(models.Model):
    dni = models.CharField(db_column='DNI', max_length=8) # Field name made lowercase.
    ap_paterno = models.CharField(max_length=40, blank=True)
    ap_materno = models.CharField(max_length=40, blank=True)
    nombres = models.CharField(max_length=50, blank=True)
    tipo_trab = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'View_1'

class ActProy(models.Model):
    ano_eje = models.ForeignKey('SubPrograma', db_column='ano_eje')
    funcion = models.ForeignKey('SubPrograma', db_column='funcion')
    programa = models.ForeignKey('SubPrograma', db_column='programa')
    sub_programa = models.ForeignKey('SubPrograma', db_column='sub_programa')
    act_proy = models.ForeignKey('ActProyNombre', db_column='act_proy')
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'act_proy'

class ActProyNombre(models.Model):
    ano_eje = models.CharField(max_length=4)
    act_proy = models.CharField(max_length=7)
    tipo_act_proy = models.CharField(max_length=1, blank=True)
    nombre = models.CharField(max_length=250, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'act_proy_nombre'

class ActProyXEntidad(models.Model):
    ano_eje = models.CharField(max_length=4)
    act_proy = models.CharField(max_length=7)
    sec_ejec = models.CharField(max_length=6, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'act_proy_x_entidad'

class AlmMovimiento(models.Model):
    ano_eje = models.CharField(max_length=4)
    cod_almacen = models.CharField(max_length=2)
    tipo_mov = models.CharField(max_length=1)
    nro_mov = models.IntegerField()
    id_doc_almacen = models.IntegerField(blank=True, null=True)
    nro_doc_almacen = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    obra = models.CharField(max_length=1, blank=True)
    ruc = models.CharField(max_length=11, blank=True)
    dni = models.CharField(max_length=8, blank=True)
    cod_oficina = models.CharField(max_length=5, blank=True)
    desc_cargo = models.CharField(max_length=75, blank=True)
    tipo_doc2 = models.CharField(max_length=3, blank=True)
    ano_doc2 = models.CharField(max_length=4, blank=True)
    nro_doc2 = models.IntegerField(blank=True, null=True)
    sec_func = models.CharField(max_length=4, blank=True)
    n_factura = models.CharField(max_length=100, blank=True)
    igv = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    comentario = models.CharField(max_length=100, blank=True)
    total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    user_registra = models.CharField(max_length=8, blank=True)
    user_anula = models.CharField(max_length=8, blank=True)
    fecha_anula = models.DateTimeField(blank=True, null=True)
    motivo = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'alm_movimiento'

class AlmMovimientoDetalle(models.Model):
    ano_eje = models.ForeignKey(AlmMovimiento, db_column='ano_eje')
    cod_almacen = models.ForeignKey('Almacen', db_column='cod_almacen')
    tipo_mov = models.ForeignKey(AlmMovimiento, db_column='tipo_mov')
    nro_mov = models.ForeignKey(AlmMovimiento, db_column='nro_mov')
    id_item = models.CharField(max_length=13)
    item = models.IntegerField()
    cantidad = models.DecimalField(max_digits=18, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=18, decimal_places=4)
    unidad = models.IntegerField(blank=True, null=True)
    divisionaria = models.CharField(max_length=11, blank=True)
    sec_func = models.CharField(max_length=4, blank=True)
    marca = models.CharField(max_length=20, blank=True)
    modelo = models.CharField(max_length=20, blank=True)
    serie = models.CharField(max_length=100, blank=True)
    comentario = models.CharField(max_length=1000, blank=True)
    stock = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo_ingreso = models.CharField(max_length=13, blank=True)
    saneado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'alm_movimiento_detalle'

class Almacen(models.Model):
    cod_almacen = models.CharField(primary_key=True, max_length=2)
    nomb_almacen = models.CharField(max_length=50, blank=True)
    abrev_almacen = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    ubigeo = models.CharField(max_length=6, blank=True)
    referencia = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'almacen'

class Ambientes(models.Model):
    codlocal = models.CharField(max_length=3)
    codambiente = models.CharField(max_length=5)
    ambiente = models.CharField(max_length=75, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'ambientes'

class ArchiDetalle(models.Model):
    ano_eje = models.ForeignKey('Archivador', db_column='ano_eje')
    n_archivador = models.ForeignKey('Archivador', db_column='n_archivador')
    n_siaf = models.IntegerField()
    fto_financ = models.CharField(max_length=2)
    ano_comprob = models.CharField(max_length=10)
    n_comprob = models.IntegerField()
    sec_func = models.CharField(max_length=4, blank=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tipo_docu = models.CharField(max_length=2, blank=True)
    n_doc = models.IntegerField(blank=True, null=True)
    ruc = models.CharField(max_length=11, blank=True)
    dni = models.CharField(max_length=8, blank=True)
    otro = models.CharField(max_length=80, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'archi_detalle'

class Archivador(models.Model):
    ano_eje = models.CharField(max_length=4)
    n_archivador = models.IntegerField()
    n_estante = models.ForeignKey('Estante', db_column='n_estante', blank=True, null=True)
    n_piso = models.IntegerField(blank=True, null=True)
    sec_func = models.CharField(max_length=4, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'archivador'

class Areas(models.Model):
    codarea = models.CharField(primary_key=True, max_length=5)
    codlocal = models.CharField(max_length=3, blank=True)
    area = models.CharField(max_length=80)
    siglas = models.CharField(max_length=6)
    class Meta:
        managed = False
        db_table = 'areas'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class CargoFuncional(models.Model):
    cargo_func = models.CharField(max_length=3)
    nombre = models.CharField(max_length=100, blank=True)
    depen_func = models.CharField(max_length=3, blank=True)
    zona = models.CharField(max_length=2, blank=True)
    class Meta:
        managed = False
        db_table = 'cargo_funcional'

class Cas3(models.Model):
    dni = models.CharField(max_length=8)
    n_serie = models.IntegerField()
    n_recibo = models.IntegerField()
    rem_aseg = models.DecimalField(max_digits=24, decimal_places=2, blank=True, null=True)
    retencion = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'cas3'

class Catalogo(models.Model):
    codigo = models.CharField(primary_key=True, max_length=8)
    denominaci = models.CharField(max_length=60)
    nro_resolu = models.CharField(max_length=15)
    class Meta:
        managed = False
        db_table = 'catalogo'

class ClaseBienSeace(models.Model):
    tipo_bien = models.ForeignKey(GrupoBienSeace, db_column='tipo_bien')
    grupo_bien = models.ForeignKey(GrupoBienSeace, db_column='grupo_bien')
    clase_bien = models.CharField(max_length=2)
    nombre_cla = models.CharField(max_length=1000, blank=True)
    alcance_cla = models.CharField(max_length=1000, blank=True)
    flag_activ = models.CharField(max_length=1, blank=True)
    flag_sbn = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'clase_bien_SEACE'

class Clases(models.Model):
    clase = models.CharField(primary_key=True, max_length=2)
    dscclase = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'clases'

class Componente(models.Model):
    ano_eje = models.ForeignKey('ComponenteNombre', db_column='ano_eje')
    funcion = models.ForeignKey(ActProy, db_column='funcion')
    programa = models.ForeignKey(ActProy, db_column='programa')
    sub_programa = models.ForeignKey(ActProy, db_column='sub_programa')
    act_proy = models.ForeignKey(ActProy, db_column='act_proy')
    componente = models.ForeignKey('ComponenteNombre', db_column='componente')
    estado = models.CharField(max_length=1, blank=True)
    finalidad = models.CharField(max_length=5, blank=True)

    class Meta:
        managed = False
        db_table = 'componente'


class ComponenteNombre(models.Model):
    ano_eje = models.CharField(max_length=4)
    componente = models.CharField(max_length=7)
    tipo_componente = models.CharField(max_length=1)
    nombre = models.CharField(max_length=250, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'componente_nombre'


class Cuarta(models.Model):
    dni = models.IntegerField(primary_key=True)
    n_serie = models.IntegerField(blank=True, null=True)
    n_recibo = models.IntegerField(blank=True, null=True)
    rem_aseg = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuarta'


class Cuentac(models.Model):
    ano_eje = models.CharField(max_length=4, blank=True)
    cuenta = models.CharField(primary_key=True, max_length=11)
    denomina = models.CharField(max_length=100)
    tipo_cta = models.CharField(max_length=20, blank=True)
    flag_cta_esp = models.NullBooleanField()
    tip_uso_cta = models.CharField(max_length=1, blank=True)
    procent_depre = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    flg_patri = models.CharField(max_length=1, blank=True)
    flg_alma = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'cuentac'


class Departamento(models.Model):
    departamento = models.CharField(max_length=2)
    nombre = models.CharField(max_length=150, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class DepreciacionBienes(models.Model):
    cod_periodo = models.ForeignKey('PeriodosDepreciacion', db_column='cod_periodo')
    cod_bien = models.CharField(max_length=8)
    correla = models.CharField(max_length=4)
    item = models.IntegerField()
    ano = models.CharField(max_length=4, blank=True)
    mes = models.CharField(max_length=2, blank=True)
    fecha_compra = models.DateTimeField(blank=True, null=True)
    fecha_origen = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    cuenta = models.CharField(max_length=11, blank=True)
    valor_libros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    factor_ajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    valor_actualizado = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    diferencia_ajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    depre_act_libros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    depre_act_actual = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    depre_act_diferencia = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    depre_per_libros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    depre_per_actual = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    depre_per_diferencia = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    valor_neto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'depreciacion_bienes'


class Distrito(models.Model):
    departamento = models.CharField(max_length=2)
    provincia = models.CharField(max_length=2)
    distrito = models.CharField(max_length=2)
    nombre = models.CharField(max_length=150, blank=True)
    region = models.CharField(max_length=2, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'distrito'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documento(models.Model):
    ano_eje = models.CharField(max_length=4)
    n_expediente = models.BigIntegerField()
    tipo_doc = models.IntegerField()
    n_doc = models.IntegerField()
    cod_oficina = models.CharField(max_length=5)
    dni = models.CharField(max_length=8)
    id_cargo = models.IntegerField()
    cod_oficina_des = models.CharField(max_length=5, blank=True)
    dni_des = models.CharField(max_length=8, blank=True)
    id_cargo_des = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    n_folios = models.IntegerField(blank=True, null=True)
    asunto = models.CharField(max_length=150, blank=True)
    referencia = models.CharField(max_length=200, blank=True)
    detalle = models.CharField(max_length=500, blank=True)
    observacion = models.CharField(max_length=250, blank=True)
    exterior = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'documento'


class Dtproperties(models.Model):
    id = models.AutoField()
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True)
    uvalue = models.CharField(max_length=255, blank=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'


class Especifica(models.Model):
    ano_eje = models.ForeignKey('SubgenericaDet', db_column='ano_eje')
    tipo_transaccion = models.ForeignKey('SubgenericaDet', db_column='tipo_transaccion')
    generica = models.ForeignKey('SubgenericaDet', db_column='generica')
    subgenerica = models.ForeignKey('SubgenericaDet', db_column='subgenerica')
    subgenerica_det = models.ForeignKey('SubgenericaDet', db_column='subgenerica_det')
    especifica = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=250, blank=True)
    ambito = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'especifica'


class EspecificaDet(models.Model):
    ano_eje = models.ForeignKey(Especifica, db_column='ano_eje')
    tipo_transaccion = models.ForeignKey(Especifica, db_column='tipo_transaccion')
    generica = models.ForeignKey(Especifica, db_column='generica')
    subgenerica = models.ForeignKey(Especifica, db_column='subgenerica')
    subgenerica_det = models.ForeignKey(Especifica, db_column='subgenerica_det')
    especifica = models.ForeignKey(Especifica, db_column='especifica')
    especifica_det = models.CharField(max_length=2)
    id_clasificador = models.CharField(max_length=7)
    descripcion = models.CharField(max_length=250, blank=True)
    ambito = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    exclusivo_tp = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'especifica_det'


class Estante(models.Model):

    n_estante = models.IntegerField(primary_key=True)
    cod_bien = models.CharField(max_length=8, blank=True)
    correla = models.CharField(max_length=4, blank=True)
    n_pisos = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    observaciones = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'estante'


class Expediente(models.Model):
    ano_eje = models.CharField(max_length=4)
    n_expediente = models.BigIntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    descripcion_exp = models.CharField(max_length=75, blank=True)
    cod_oficina = models.CharField(max_length=5, blank=True)
    dni = models.CharField(max_length=8, blank=True)
    id_cargo = models.IntegerField(blank=True, null=True)
    exp_origen = models.BigIntegerField(blank=True, null=True)
    flg_origen = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'expediente'


class ExpedienteDet(models.Model):
    ano_eje = models.ForeignKey(Expediente, db_column='ano_eje')
    n_expediente = models.ForeignKey(Expediente, db_column='n_expediente')
    item = models.IntegerField()
    tipo_doc = models.ForeignKey(Documento, db_column='tipo_doc', blank=True, null=True)
    n_doc = models.ForeignKey(Documento, db_column='n_doc', blank=True, null=True)
    cod_oficina = models.ForeignKey(Documento, db_column='cod_oficina', blank=True, null=True)
    dni = models.ForeignKey(Documento, db_column='dni', blank=True, null=True)
    id_cargo = models.ForeignKey(Documento, db_column='id_cargo', blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'expediente_det'


class FactoresAjuste(models.Model):
    ano_eje = models.CharField(max_length=4)
    mes_eje = models.CharField(max_length=2)
    factor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factores_ajuste'


class FamiliaBienSeace(models.Model):
    tipo_bien = models.ForeignKey(ClaseBienSeace, db_column='tipo_bien')
    grupo_bien = models.ForeignKey(ClaseBienSeace, db_column='grupo_bien')
    clase_bien = models.ForeignKey(ClaseBienSeace, db_column='clase_bien')
    familia_bien = models.CharField(max_length=4)
    nombre_fam = models.CharField(max_length=1000, blank=True)
    alcance_fam = models.CharField(max_length=1000, blank=True)
    flag_activ = models.CharField(max_length=1, blank=True)
    flag_sbn = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'familia_bien_SEACE'


class Feriado(models.Model):
    id_feriado = models.IntegerField()
    d_feriado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feriado'


class Finalidad(models.Model):
    ano_eje = models.CharField(max_length=4)
    finalidad = models.CharField(max_length=7)
    nombre = models.CharField(max_length=250, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    ambito = models.CharField(max_length=1, blank=True)
    es_presupuestal = models.CharField(max_length=1, blank=True)
    ambito_en = models.CharField(max_length=1, blank=True)
    ambito_programa = models.CharField(max_length=2, blank=True)
    es_generico = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'finalidad'


class Funcion(models.Model):
    ano_eje = models.CharField(max_length=4)
    funcion = models.CharField(max_length=2)
    nombre = models.CharField(max_length=150, blank=True)
    cuenta_bien = models.CharField(max_length=11, blank=True)
    clasi_contrata = models.CharField(max_length=7, blank=True)
    clasi_planilla = models.CharField(max_length=7, blank=True)
    clasi_bien = models.CharField(max_length=7, blank=True)
    clasi_servicio = models.CharField(max_length=7, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'funcion'


class Gasto(models.Model):
    ano_eje = models.CharField(max_length=4)
    sec_func = models.CharField(max_length=4)
    fuente_financ = models.CharField(max_length=2)
    clasificador = models.CharField(max_length=7)
    presupuesto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    modificacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_a_solicitado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_de_solicitado = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    ampliacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ejecucion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    compromiso = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    devengado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    girado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pagado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gasto'


class Generica(models.Model):
    ano_eje = models.ForeignKey('TipoTransaccion', db_column='ano_eje')
    tipo_transaccion = models.ForeignKey('TipoTransaccion', db_column='tipo_transaccion')
    generica = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=250, blank=True)
    id_grupo_clasificador = models.CharField(max_length=7)
    ambito = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'generica'


class Grupos(models.Model):
    grupo = models.CharField(primary_key=True, max_length=2)
    dscgrupo = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'grupos'


class GruposClases(models.Model):
    grupo = models.ForeignKey(Grupos, db_column='grupo')
    clase = models.ForeignKey(Clases, db_column='clase')

    class Meta:
        managed = False
        db_table = 'grupos_clases'


class Hcc(models.Model):
    ano_eje = models.CharField(max_length=4)
    n_hcc = models.IntegerField()
    mes = models.CharField(max_length=2, blank=True)
    fecha = models.DateTimeField(blank=True, null=True)
    cod_doc = models.CharField(max_length=3, blank=True)
    num_doc = models.CharField(max_length=25, blank=True)
    ruc = models.CharField(db_column='RUC', max_length=11, blank=True)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=8, blank=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=150, blank=True)
    fuente_financ = models.CharField(max_length=2, blank=True)
    sec_func = models.CharField(max_length=4, blank=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    n_reg_siaf = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'hcc'


class Inventario(models.Model):
    ano_eje = models.CharField(max_length=4)
    num_inv = models.CharField(max_length=4)
    tipo_inventario = models.CharField(max_length=1, blank=True)
    periodo = models.DateTimeField(blank=True, null=True)
    fecha_ini = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    responsable = models.CharField(max_length=8, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    observacion = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'inventario'

class InventarioDetalle(models.Model):
    ano_eje = models.ForeignKey(Inventario, db_column='ano_eje')
    num_inv = models.ForeignKey(Inventario, db_column='num_inv')
    codbien = models.CharField(max_length=8)
    correla = models.CharField(max_length=4)
    flg_verificado = models.CharField(max_length=1, blank=True)
    grupo = models.CharField(max_length=20, blank=True)
    fecha_verifica = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'inventario_detalle'

class Locales(models.Model):
    codlocal = models.CharField(primary_key=True, max_length=3)
    nombre_local = models.CharField(max_length=40)
    codinst = models.ForeignKey(Entidad, db_column='codinst', blank=True, null=True)
    tipovia = models.ForeignKey(Tipovia, db_column='tipovia', blank=True, null=True)
    direccion = models.CharField(max_length=40, blank=True)
    num_mun = models.CharField(max_length=10, blank=True)
    dsc_mz = models.CharField(max_length=10, blank=True)
    dsc_lote = models.CharField(max_length=10, blank=True)
    codubigeo = models.ForeignKey('Ubigeo', db_column='codubigeo', blank=True, null=True)
    ctd_area = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    flg_um = models.CharField(max_length=10, blank=True)
    flg_tiporeg = models.CharField(max_length=20, blank=True)
    dsc_asiento = models.CharField(max_length=10, blank=True)
    dsc_fojas = models.CharField(max_length=10, blank=True)
    dsc_tomo = models.CharField(max_length=10, blank=True)
    dsc_pelectro = models.CharField(max_length=10, blank=True)
    cod_predio = models.CharField(max_length=10, blank=True)
    dsc_beneficiario = models.CharField(max_length=20, blank=True)
    dsc_propietario = models.CharField(max_length=20, blank=True)
    dsc_ctactble = models.CharField(max_length=11, blank=True)
    flg_tipomoneda = models.CharField(max_length=10, blank=True)
    ctd_valor = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    flg_propiedad = models.CharField(max_length=10, blank=True)
    dsc_asinabip = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'locales'

class MaestroDocumento(models.Model):
    cod_doc = models.CharField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=150)
    abreviatura = models.CharField(max_length=20)
    estado = models.CharField(max_length=1)
    flg_tramite = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'maestro_documento'

class Mbienes0(models.Model):
    codbien = models.ForeignKey('Tipobien', db_column='codbien')
    correla = models.CharField(max_length=4)
    clasifica = models.CharField(max_length=1, blank=True)
    codlocal = models.CharField(max_length=3, blank=True)
    codarea = models.CharField(max_length=5, blank=True)
    codoficina = models.CharField(max_length=5, blank=True)
    codambiente = models.CharField(max_length=5, blank=True)
    codanterior = models.CharField(max_length=15, blank=True)
    codusuario = models.CharField(max_length=8, blank=True)
    tipo_cta = models.CharField(max_length=1, blank=True)
    cuenta = models.CharField(max_length=11, blank=True)
    valorlibro = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    valortasa = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    marca = models.CharField(max_length=15, blank=True)
    modelo = models.CharField(max_length=15, blank=True)
    tipo = models.CharField(max_length=15, blank=True)
    color = models.CharField(max_length=15, blank=True)
    serie = models.CharField(max_length=20, blank=True)
    titulo = models.CharField(max_length=100, blank=True)
    edicion = models.CharField(max_length=50, blank=True)
    autor = models.CharField(max_length=100, blank=True)
    product_name = models.CharField(max_length=100, blank=True)
    product_key = models.CharField(max_length=50, blank=True)
    vigencia_desde = models.DateTimeField(blank=True, null=True)
    vigencia_hasta = models.DateTimeField(blank=True, null=True)
    nummotor = models.CharField(max_length=20, blank=True)
    numchasis = models.CharField(max_length=20, blank=True)
    a_o = models.CharField(db_column='a\xf1o', max_length=4, blank=True) # Field renamed to remove unsuitable characters.
    dimension = models.CharField(max_length=15, blank=True)
    raza = models.CharField(max_length=15, blank=True)
    especie = models.CharField(max_length=15, blank=True)
    otros = models.CharField(max_length=500, blank=True)
    fec_reg = models.DateTimeField(blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True)
    edad = models.CharField(max_length=5, blank=True)
    pais = models.CharField(max_length=15, blank=True)
    condicion = models.CharField(max_length=1, blank=True)
    fec_act = models.DateTimeField(blank=True, null=True)
    asegurado = models.CharField(max_length=1, blank=True)
    est_bien = models.CharField(max_length=1, blank=True)
    flg_causal = models.CharField(max_length=1, blank=True)
    resol_baja = models.CharField(max_length=25, blank=True)
    fec_baja = models.DateTimeField(blank=True, null=True)
    user_baja = models.CharField(max_length=8, blank=True)
    flg_acto = models.CharField(max_length=1, blank=True)
    resol_disp = models.CharField(max_length=25, blank=True)
    fec_disp = models.DateTimeField(blank=True, null=True)
    causal_elim = models.CharField(max_length=50, blank=True)
    fecha_elim = models.DateTimeField(blank=True, null=True)
    user_elim = models.CharField(max_length=8, blank=True)
    est_gestion = models.CharField(max_length=1, blank=True)
    resol_afec = models.CharField(max_length=25, blank=True)
    fec_afec = models.DateTimeField(blank=True, null=True)
    fec_vafec = models.DateTimeField(blank=True, null=True)
    ent_afec = models.CharField(max_length=100, blank=True)
    resol_arre = models.CharField(max_length=25, blank=True)
    fec_arre = models.DateTimeField(blank=True, null=True)
    fec_varre = models.DateTimeField(blank=True, null=True)
    ent_arre = models.CharField(max_length=100, blank=True)
    doc_alta = models.CharField(max_length=25, blank=True)
    user_alta = models.CharField(max_length=8, blank=True)
    doc_baja = models.CharField(max_length=25, blank=True)
    flg_estado = models.CharField(max_length=1, blank=True)
    selec = models.CharField(max_length=1, blank=True)
    sbn = models.CharField(max_length=1, blank=True)
    ano_orden = models.CharField(max_length=4, blank=True)
    n_orden = models.IntegerField(blank=True, null=True)
    tipo_orden = models.CharField(max_length=1, blank=True)
    funcionario = models.CharField(max_length=5, blank=True)
    srp = models.CharField(max_length=1, blank=True)
    tasado = models.CharField(max_length=1, blank=True)
    n_notacargo = models.CharField(max_length=11, blank=True)
    cod_padre = models.CharField(max_length=12, blank=True)
    cod_madre = models.CharField(max_length=12, blank=True)
    sit_binv = models.CharField(max_length=1, blank=True)
    valoradq = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ent_disp = models.CharField(max_length=100, blank=True)
    matricula = models.CharField(max_length=25, blank=True)
    anho_fab = models.CharField(max_length=9, blank=True)
    longitud = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    altura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ancho = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codbien_aux = models.CharField(max_length=8, blank=True)
    correla_aux = models.CharField(max_length=4, blank=True)
    class Meta:
        managed = False
        db_table = 'mbienes0'

class MbienesSincerados(models.Model):
    codbien = models.CharField(max_length=8)
    correla = models.CharField(max_length=4)
    ano_eje = models.CharField(max_length=4)
    num_inv = models.CharField(max_length=4)
    marca = models.CharField(max_length=15, blank=True)
    modelo = models.CharField(max_length=15, blank=True)
    tipo = models.CharField(max_length=15, blank=True)
    color = models.CharField(max_length=15, blank=True)
    serie = models.CharField(max_length=15)
    nummotor = models.CharField(max_length=15, blank=True)
    numchasis = models.CharField(max_length=15, blank=True)
    a_o = models.CharField(db_column='a\xf1o', max_length=4, blank=True) # Field renamed to remove unsuitable characters.
    dimension = models.CharField(max_length=15, blank=True)
    raza = models.CharField(max_length=15, blank=True)
    especie = models.CharField(max_length=15, blank=True)
    otros = models.CharField(max_length=500, blank=True)
    placa = models.CharField(max_length=7, blank=True)
    edad = models.CharField(max_length=5, blank=True)
    class Meta:
        managed = False
        db_table = 'mbienes_sincerados'

class NivelEducativo(models.Model):
    nivel_educativo = models.CharField(primary_key=True, max_length=2)
    descripcion = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'nivel_educativo'

class Ocupacion(models.Model):
    ocupacion = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'ocupacion'

class Oficinas(models.Model):
    codarea = models.ForeignKey(Areas, db_column='codarea')
    codoficina = models.CharField(max_length=5)
    codlocal = models.CharField(max_length=3, blank=True)
    oficina = models.CharField(max_length=100, blank=True)
    abrev = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'oficinas'

class Pais(models.Model):
    pais = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=150, blank=True)
    class Meta:
        managed = False
        db_table = 'pais'

class Papeleta(models.Model):
    ano_eje = models.CharField(max_length=4)
    n_papeleta = models.CharField(max_length=6)
    tipo_pape = models.CharField(max_length=1, blank=True)
    regulariza = models.CharField(max_length=1, blank=True)
    peri_pape = models.CharField(max_length=1, blank=True)
    fecha_pape = models.DateTimeField(blank=True, null=True)
    fecha_del = models.DateTimeField(blank=True, null=True)
    fecha_al = models.DateTimeField(blank=True, null=True)
    hora_ini = models.DateTimeField(blank=True, null=True)
    hora_fin = models.DateTimeField(blank=True, null=True)
    dni = models.CharField(max_length=8, blank=True)
    lugar = models.CharField(max_length=100, blank=True)
    motivo = models.CharField(max_length=300, blank=True)
    observaciones = models.CharField(max_length=400, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'papeleta'

class Parametros(models.Model):
    id_param = models.IntegerField()
    nombre = models.CharField(max_length=100, blank=True)
    abrev = models.CharField(max_length=30, blank=True)
    fecha_ini = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)
    valor = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'parametros'

class Pbcatcol(models.Model):
    pbc_tnam = models.CharField(max_length=129)
    pbc_tid = models.IntegerField(blank=True, null=True)
    pbc_ownr = models.CharField(max_length=129)
    pbc_cnam = models.CharField(max_length=129)
    pbc_cid = models.SmallIntegerField(blank=True, null=True)
    pbc_labl = models.CharField(max_length=254, blank=True)
    pbc_lpos = models.SmallIntegerField(blank=True, null=True)
    pbc_hdr = models.CharField(max_length=254, blank=True)
    pbc_hpos = models.SmallIntegerField(blank=True, null=True)
    pbc_jtfy = models.SmallIntegerField(blank=True, null=True)
    pbc_mask = models.CharField(max_length=31, blank=True)
    pbc_case = models.SmallIntegerField(blank=True, null=True)
    pbc_hght = models.SmallIntegerField(blank=True, null=True)
    pbc_wdth = models.SmallIntegerField(blank=True, null=True)
    pbc_ptrn = models.CharField(max_length=31, blank=True)
    pbc_bmap = models.CharField(max_length=1, blank=True)
    pbc_init = models.CharField(max_length=254, blank=True)
    pbc_cmnt = models.CharField(max_length=254, blank=True)
    pbc_edit = models.CharField(max_length=31, blank=True)
    pbc_tag = models.CharField(max_length=254, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcatcol'

class Pbcatedt(models.Model):
    pbe_name = models.CharField(max_length=30)
    pbe_edit = models.CharField(max_length=254, blank=True)
    pbe_type = models.SmallIntegerField(blank=True, null=True)
    pbe_cntr = models.IntegerField(blank=True, null=True)
    pbe_seqn = models.SmallIntegerField()
    pbe_flag = models.IntegerField(blank=True, null=True)
    pbe_work = models.CharField(max_length=32, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcatedt'

class Pbcatfmt(models.Model):
    pbf_name = models.CharField(unique=True, max_length=30)
    pbf_frmt = models.CharField(max_length=254, blank=True)
    pbf_type = models.SmallIntegerField(blank=True, null=True)
    pbf_cntr = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pbcatfmt'

class Pbcattbl(models.Model):
    pbt_tnam = models.CharField(max_length=129)
    pbt_tid = models.IntegerField(blank=True, null=True)
    pbt_ownr = models.CharField(max_length=129)
    pbd_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fitl = models.CharField(max_length=1, blank=True)
    pbd_funl = models.CharField(max_length=1, blank=True)
    pbd_fchr = models.SmallIntegerField(blank=True, null=True)
    pbd_fptc = models.SmallIntegerField(blank=True, null=True)
    pbd_ffce = models.CharField(max_length=18, blank=True)
    pbh_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fitl = models.CharField(max_length=1, blank=True)
    pbh_funl = models.CharField(max_length=1, blank=True)
    pbh_fchr = models.SmallIntegerField(blank=True, null=True)
    pbh_fptc = models.SmallIntegerField(blank=True, null=True)
    pbh_ffce = models.CharField(max_length=18, blank=True)
    pbl_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fitl = models.CharField(max_length=1, blank=True)
    pbl_funl = models.CharField(max_length=1, blank=True)
    pbl_fchr = models.SmallIntegerField(blank=True, null=True)
    pbl_fptc = models.SmallIntegerField(blank=True, null=True)
    pbl_ffce = models.CharField(max_length=18, blank=True)
    pbt_cmnt = models.CharField(max_length=254, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcattbl'

class Pbcatvld(models.Model):
    pbv_name = models.CharField(unique=True, max_length=30)
    pbv_vald = models.CharField(max_length=254, blank=True)
    pbv_type = models.SmallIntegerField(blank=True, null=True)
    pbv_cntr = models.IntegerField(blank=True, null=True)
    pbv_msg = models.CharField(max_length=254, blank=True)
    class Meta:
        managed = False
        db_table = 'pbcatvld'

class PecosaDetalle(models.Model):
    ano_eje = models.ForeignKey(Pecosa, db_column='ano_eje')
    n_pecosa = models.ForeignKey(Pecosa, db_column='n_pecosa')
    item = models.IntegerField()
    cantidad = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pecosa_detalle'

class PeriodosDepreciacion(models.Model):
    cod_periodo = models.BigIntegerField(primary_key=True)
    periodo = models.DateTimeField(blank=True, null=True)
    user_registra = models.CharField(max_length=8, blank=True)
    fecha_registra = models.DateTimeField(blank=True, null=True)
    user_cierre = models.CharField(max_length=8, blank=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    ano_inv = models.CharField(db_column='ANO_INV', max_length=4, blank=True) # Field name made lowercase.
    num_inv = models.CharField(db_column='NUM_INV', max_length=4, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'periodos_depreciacion'

class Programa(models.Model):
    ano_eje = models.ForeignKey('ProgramaNombre', db_column='ano_eje')
    funcion = models.ForeignKey(Funcion, db_column='funcion')
    programa = models.ForeignKey('ProgramaNombre', db_column='programa')
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'programa'

class ProgramaNombre(models.Model):
    ano_eje = models.CharField(max_length=4)
    programa = models.CharField(max_length=3)
    nombre = models.CharField(max_length=150, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'programa_nombre'

class Provincia(models.Model):
    departamento = models.CharField(max_length=2)
    provincia = models.CharField(max_length=2)
    nombre = models.CharField(max_length=150, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'provincia'

class Proyecto(models.Model):
    id_proy = models.IntegerField(primary_key=True)
    act_proy = models.CharField(max_length=7, blank=True)
    nombre = models.CharField(max_length=256, blank=True)
    snip = models.CharField(max_length=6, blank=True)
    monto = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'proyecto'

class Prueba(models.Model):
    ruc = models.CharField(db_column='RUC', max_length=11) # Field name made lowercase.
    serie = models.IntegerField(db_column='SERIE', blank=True, null=True) # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=8, blank=True) # Field name made lowercase.
    monto = models.DecimalField(db_column='MONTO', max_digits=18, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'prueba'

class Prueba1(models.Model):
    dni = models.CharField(max_length=8)
    n_serie = models.IntegerField()
    recibo = models.CharField(max_length=8)
    fecha = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'prueba1'

class SituacionLaboral(models.Model):
    situacion_laboral = models.CharField(primary_key=True, max_length=1)
    nombre = models.CharField(max_length=150, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'situacion_laboral'

class Squid(models.Model):
    ip = models.CharField(max_length=15)
    pagina = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'squid'

class SubPrograma(models.Model):
    ano_eje = models.ForeignKey('SubProgramaNombre', db_column='ano_eje')
    funcion = models.ForeignKey(Programa, db_column='funcion')
    programa = models.ForeignKey(Programa, db_column='programa')
    sub_programa = models.ForeignKey('SubProgramaNombre', db_column='sub_programa')
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'sub_programa'

class SubProgramaNombre(models.Model):
    ano_eje = models.CharField(max_length=4)
    sub_programa = models.CharField(max_length=4)
    nombre = models.CharField(max_length=150, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'sub_programa_nombre'

class Subgenerica(models.Model):
    ano_eje = models.ForeignKey(Generica, db_column='ano_eje')
    tipo_transaccion = models.ForeignKey(Generica, db_column='tipo_transaccion')
    generica = models.ForeignKey(Generica, db_column='generica')
    subgenerica = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=250, blank=True)
    ambito = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'subgenerica'

class SubgenericaDet(models.Model):
    ano_eje = models.ForeignKey(Subgenerica, db_column='ano_eje')
    tipo_transaccion = models.ForeignKey(Subgenerica, db_column='tipo_transaccion')
    generica = models.ForeignKey(Subgenerica, db_column='generica')
    subgenerica = models.ForeignKey(Subgenerica, db_column='subgenerica')
    subgenerica_det = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=250, blank=True)
    categoria_gasto = models.CharField(max_length=1, blank=True)
    tipo_act_proy = models.CharField(max_length=1, blank=True)
    tipo_gasto = models.CharField(max_length=1, blank=True)
    ambito = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'subgenerica_det'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'


class Temp2(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    cuenta = models.CharField(max_length=15, blank=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp2'


class TipoContrato(models.Model):
    tipo_contrato = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=60, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_contrato'


class TipoDocumento(models.Model):
    tipo_doc = models.CharField(max_length=2)
    nombre = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoDocumentoUe(models.Model):
    tipo_doc = models.IntegerField()
    nombre = models.CharField(max_length=70, blank=True)
    abrev = models.CharField(max_length=15, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_documento_UE'


class TipoMovAlmacen(models.Model):
    tipo_mov = models.IntegerField(primary_key=True)
    tipo_transac = models.CharField(max_length=1, blank=True)
    nombre_mov = models.CharField(max_length=50, blank=True)
    abrev_mov = models.CharField(max_length=15, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_mov_almacen'


class TipoPapeleta(models.Model):
    tipo_pape = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_papeleta'


class TipoPersona(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class TipoProveido(models.Model):
    cod_proveido = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_proveido'


class TipoTransaccion(models.Model):
    ano_eje = models.CharField(max_length=4)
    tipo_transaccion = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=250, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_transaccion'


class Tipobien(models.Model):
    codbien = models.CharField(primary_key=True, max_length=8)
    descripcio = models.CharField(max_length=60)
    correla = models.IntegerField()
    tipo = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'tipobien'


class TmpHorario(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    dia01 = models.DateTimeField(blank=True, null=True)
    dia02 = models.DateTimeField(blank=True, null=True)
    dia03 = models.DateTimeField(blank=True, null=True)
    dia04 = models.DateTimeField(blank=True, null=True)
    dia05 = models.DateTimeField(blank=True, null=True)
    dia06 = models.DateTimeField(blank=True, null=True)
    dia07 = models.DateTimeField(blank=True, null=True)
    dia08 = models.DateTimeField(blank=True, null=True)
    dia09 = models.DateTimeField(blank=True, null=True)
    dia10 = models.DateTimeField(blank=True, null=True)
    dia11 = models.DateTimeField(blank=True, null=True)
    dia12 = models.DateTimeField(blank=True, null=True)
    dia13 = models.DateTimeField(blank=True, null=True)
    dia14 = models.DateTimeField(blank=True, null=True)
    dia15 = models.DateTimeField(blank=True, null=True)
    dia16 = models.DateTimeField(blank=True, null=True)
    dia17 = models.DateTimeField(blank=True, null=True)
    dia18 = models.DateTimeField(blank=True, null=True)
    dia19 = models.DateTimeField(blank=True, null=True)
    dia20 = models.DateTimeField(blank=True, null=True)
    dia21 = models.DateTimeField(blank=True, null=True)
    dia22 = models.DateTimeField(blank=True, null=True)
    dia23 = models.DateTimeField(blank=True, null=True)
    dia24 = models.DateTimeField(blank=True, null=True)
    dia25 = models.DateTimeField(blank=True, null=True)
    dia26 = models.DateTimeField(blank=True, null=True)
    dia27 = models.DateTimeField(blank=True, null=True)
    dia28 = models.DateTimeField(blank=True, null=True)
    dia29 = models.DateTimeField(blank=True, null=True)
    dia30 = models.DateTimeField(blank=True, null=True)
    dia31 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_horario'


class TmpRicardo(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    afp = models.CharField(max_length=10, blank=True)
    afp1 = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'tmp_ricardo'


class TramiteMovimientos(models.Model):
    ano_eje = models.ForeignKey(Expediente, db_column='ano_eje')
    n_expediente = models.ForeignKey(Expediente, db_column='n_expediente')
    num_mov = models.CharField(max_length=2)
    oficina_origen = models.CharField(max_length=5, blank=True)
    oficina_destino = models.CharField(max_length=5, blank=True)
    entidad_origen = models.CharField(max_length=3, blank=True)
    entidad_destino = models.CharField(max_length=3, blank=True)
    usuario_origen = models.CharField(max_length=8, blank=True)
    usuario_destino = models.CharField(max_length=8, blank=True)
    id_cargo_origen = models.IntegerField(blank=True, null=True)
    id_cargo_destino = models.IntegerField(blank=True, null=True)
    fecha_envio = models.DateTimeField(blank=True, null=True)
    fecha_recepcion = models.DateTimeField(blank=True, null=True)
    fecha_archivado = models.DateTimeField(blank=True, null=True)
    tipo_proveido = models.IntegerField(blank=True, null=True)
    proveido = models.CharField(max_length=100, blank=True)
    prioridad = models.CharField(max_length=1, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'tramite_movimientos'


class TurnosVigilantes(models.Model):
    dni = models.CharField(db_column='DNI', max_length=8)  # Field name made lowercase.
    tipo_hor = models.CharField(max_length=1)
    fecha_ini = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    activo = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'turnos_vigilantes'


class Ubigeo(models.Model):
    codubigeo = models.CharField(primary_key=True, max_length=6)
    coddpto = models.CharField(max_length=2)
    codprov = models.CharField(max_length=2)
    coddist = models.CharField(max_length=2)
    nmbubigeo = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ubigeo'


class UnidadMef(models.Model):
    id_unidad = models.IntegerField(primary_key=True)
    nomb_unidad = models.CharField(max_length=50, blank=True)
    abrev_unidad = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'unidad_mef'


class Zona(models.Model):
    zona = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'zona'

# coding=utf-8

from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models

from . import constants


class Mes(models.Model):
    mes_eje = models.CharField(primary_key=True, max_length=2)
    n_mes = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'mes'

    def __unicode__(self):
        return self.nombre


class ModalidadLaboral(models.Model):
    mod_laboral = models.CharField(primary_key=True, max_length=1)
    nombre = models.CharField(max_length=30, blank=True)
    abrev = models.CharField(max_length=15, blank=True)
    tipo_trab = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'modalidad_laboral'

    def __unicode__(self):
        return self.nombre


class Entidad(models.Model):
    codinst = models.CharField(primary_key=True, max_length=10)
    entidad = models.CharField(max_length=100)
    siglas = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'entidad'


class Sectores(models.Model):
    cod_sect = models.CharField(primary_key=True, max_length=2)
    nombres = models.CharField(max_length=100)
    abrev = models.CharField(max_length=30)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'sectores'

    def __unicode__(self):
        return self.nombres


class Personal(models.Model):
    dni = models.CharField(db_column='DNI', max_length=8, primary_key=True)  # Field name made lowercase.
    ap_paterno = models.CharField(max_length=40, blank=True)
    ap_materno = models.CharField(max_length=40, blank=True)
    nombres = models.CharField(max_length=50, blank=True)
    nomb_comp = models.CharField(max_length=120, blank=True)
    fecha_nac = models.DateTimeField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, choices=constants.SEXO_CHOICES)
    # nacionalidad = models.ForeignKey(Pais, db_column='nacionalidad', blank=True, null=True)
    entidad = models.ForeignKey(Sectores, db_column='Entidad', blank=True)  # Field name made lowercase.
    telefono = models.CharField(max_length=20, blank=True)
    correo_e = models.CharField(max_length=50, blank=True)
    essalud_vida = models.CharField(max_length=1, blank=True)
    domicilio = models.CharField(max_length=150, blank=True)
    estado_civil = models.CharField(max_length=1, blank=True)
    nombre_pareja = models.CharField(max_length=120, blank=True)
    num_hijos = models.IntegerField(blank=True, null=True)
    ubica_foto = models.CharField(max_length=255, blank=True)
    ruc = models.CharField(db_column='RUC', max_length=11, blank=True)  # Field name made lowercase.
    retencion = models.CharField(max_length=1, blank=True)
    # tipo_trab = models.ForeignKey('TipoTrabajador', db_column='tipo_trab', blank=True, null=True)
    # nivel_educativo = models.ForeignKey(NivelEducativo, db_column='nivel_educativo', blank=True, null=True)
    # ocupacion = models.ForeignKey(Ocupacion, db_column='ocupacion', blank=True, null=True)
    discapacidad = models.CharField(max_length=1, blank=True)
    # reg_pension = models.ForeignKey('RegimenPensionario', db_column='reg_pension', blank=True, null=True)
    fecha_inscrip = models.DateTimeField(blank=True, null=True)
    cuspp = models.CharField(db_column='CUSPP', max_length=12, blank=True)  # Field name made lowercase.
    sctr_salud = models.CharField(db_column='SCTR_salud', max_length=1, blank=True)  # Field name made lowercase.
    sctr_pension = models.CharField(db_column='SCTR_pension', max_length=1, blank=True)  # Field name made lowercase.
    # tipo_contrato = models.ForeignKey('TipoContrato', db_column='tipo_contrato', blank=True, null=True)
    hor_nocturno = models.CharField(max_length=1, blank=True)
    sindicalizado = models.CharField(max_length=1, blank=True)
    desc_judicial = models.CharField(max_length=1, blank=True)
    periodicidad = models.CharField(max_length=1, blank=True)
    situacion = models.CharField(max_length=2, blank=True, choices=constants.SITUACION_CHOICES)
    sit_especial = models.CharField(max_length=1, blank=True)
    tipo_pago = models.CharField(max_length=1, blank=True)
    num_cuenta = models.CharField(max_length=11, blank=True)
    mod_laboral = models.ForeignKey(ModalidadLaboral, db_column='mod_laboral', blank=True, null=True)
    nivel_rem = models.CharField(max_length=2, blank=True)
    id_cargo = models.IntegerField(blank=True, null=True)
    cargo_func = models.CharField(max_length=3, blank=True)
    desc_cargo = models.CharField(max_length=100, blank=True)
    tipo_hor = models.CharField(max_length=1, blank=True)
    # zona = models.ForeignKey('Zona', db_column='zona', blank=True, null=True)
    monto_rem = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    monto_incafp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # codarea = models.ForeignKey(Oficinas, db_column='codarea', blank=True, null=True)
    # codoficina = models.ForeignKey(Oficinas, db_column='codoficina', blank=True, null=True)
    # codlocal = models.ForeignKey(Locales, db_column='codlocal', blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    fecha_cese = models.DateTimeField(blank=True, null=True)
    fecha_reg = models.DateTimeField(blank=True, null=True)
    fecha_mod = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    selec = models.CharField(max_length=1, blank=True)
    marcacion = models.CharField(max_length=1, blank=True)
    indexdb = models.BigIntegerField(blank=True, null=True)
    sec_fun = models.CharField(max_length=4, blank=True)
    fuente_f = models.CharField(max_length=2, blank=True)
    funcionario = models.CharField(max_length=5, blank=True)
    cod_reso = models.CharField(max_length=200, blank=True)
    cod_plza = models.CharField(max_length=10, blank=True)
    cod_cts = models.CharField(max_length=20, blank=True)
    tipo_pension = models.CharField(max_length=1, blank=True)

    class Meta:
        db_table = 'personal'
        verbose_name = "Personal"

    def __unicode__(self):
        return self.nomb_comp

    def get_years_old(self):
        now = datetime.now()
        delta = relativedelta(now, self.fecha_nac)
        return delta.years


class TipoPlanilla(models.Model):
    tipo_planilla = models.CharField(db_column='Tipo_planilla', max_length=1, primary_key=True)  # Field name made lowercase.
    nombre_planilla = models.CharField(max_length=50, blank=True)
    abrev_planilla = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'Tipo_Planilla'

    def __unicode__(self):
        return self.nombre_planilla


class FuenteFinanc(models.Model):
    ano_eje = models.CharField(max_length=4)
    fuente_financ = models.CharField(max_length=2)
    nombre = models.CharField(max_length=150, blank=True)
    abrev = models.CharField(max_length=15, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'fuente_financ'

    def __unicode__(self):
        return self.nombre


class Meta(models.Model):
    ano_eje = models.CharField(max_length=4)
    sec_ejec = models.CharField(max_length=6, blank=True)
    sec_func = models.CharField(max_length=4)
    funcion = models.CharField(max_length=2, blank=True)
    programa = models.CharField(max_length=3, blank=True)
    sub_programa = models.CharField(max_length=4, blank=True)
    act_proy = models.CharField(max_length=7, blank=True)
    componente = models.CharField(max_length=7, blank=True)
    meta = models.CharField(max_length=5, blank=True)
    finalidad = models.CharField(max_length=7, blank=True)
    nombre = models.CharField(max_length=150, blank=True)
    departamento = models.CharField(max_length=2, blank=True)
    provincia = models.CharField(max_length=2, blank=True)
    distrito = models.CharField(max_length=2, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    nm = models.CharField(db_column='NM', max_length=4, blank=True)  # Field name made lowercase.
    nombre_nm = models.CharField(max_length=250, blank=True)

    class Meta:
        managed = False
        db_table = 'meta'

    def __unicode__(self):
        return self.nombre_nm


class Planilla(models.Model):
    n_expediente = models.CharField(db_column='N_Expediente', max_length=8)  # Field name made lowercase.
    ano_eje = models.CharField(db_column='Ano_eje', max_length=4)  # Field name made lowercase.
    mes = models.ForeignKey(Mes, db_column='Mes', blank=True, null=True)  # Field name made lowercase.
    n_planilla = models.CharField(db_column='N_Planilla', max_length=8, blank=True)  # Field name made lowercase.
    tipo_planilla = models.ForeignKey(TipoPlanilla, db_column='Tipo_planilla', blank=True, null=True)  # Field name made lowercase.
    entidad = models.ForeignKey(Sectores, db_column='entidad', blank=True)
    sec_func = models.ForeignKey(Meta, db_column='Sec_Func', blank=True)  # Field name made lowercase.
    fuente_financ = models.CharField(db_column='Fuente_Financ', max_length=2, blank=True)  # Field name made lowercase.
    tipo_trab = models.CharField(db_column='Tipo_Trab', max_length=2, blank=True)  # Field name made lowercase.
    mod_laboral = models.ForeignKey(ModalidadLaboral, db_column='Mod_Laboral', blank=True)  # Field name made lowercase.
    trabajos = models.CharField(max_length=300, blank=True)
    fecha_exp = models.DateTimeField(db_column='Fecha_exp', blank=True, null=True)  # Field name made lowercase.
    fecha_plan = models.DateTimeField(db_column='Fecha_plan', blank=True, null=True)  # Field name made lowercase.
    periodo_ini = models.DateTimeField(db_column='Periodo_Ini', blank=True, null=True)  # Field name made lowercase.
    periodo_fin = models.DateTimeField(db_column='Periodo_Fin', blank=True, null=True)  # Field name made lowercase.
    elaborado_por = models.CharField(db_column='Elaborado_por', max_length=8, blank=True)  # Field name made lowercase.
    tareado_por = models.CharField(db_column='Tareado_por', max_length=8, blank=True)  # Field name made lowercase.
    observaciones = models.CharField(max_length=100, blank=True)
    estado = models.CharField(db_column='Estado', max_length=1, blank=True)  # Field name made lowercase.
    selec = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'Planilla'

    def get_meta(self):
        return Meta.objects.get(ano_eje=self.ano_eje, sec_func=self.sec_func)

    def get_fuente_financ(self):
        return FuenteFinanc.objects.get(ano_eje=self.ano_eje, fuente_financ=self.fuente_financ)

    def get_planilla_trabs(self):
        return PlanillaTrab.objects.filter(ano_eje=self.ano_eje, n_expediente=self.n_expediente
                                           ).prefetch_related('personal', 'reg_pension', )


class TipoTrabajador(models.Model):
    tipo_trab = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_trabajador'


class NivelRemunerativo(models.Model):
    tipo_trab = models.ForeignKey(TipoTrabajador, db_column='tipo_trab')
    nivel_rem = models.CharField(max_length=2)
    nombre = models.CharField(max_length=50, blank=True)
    abrev = models.CharField(max_length=15, blank=True)
    periodicidad = models.CharField(max_length=1, blank=True)
    monto_basico = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    monto_tope = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    buc = models.DecimalField(db_column='BUC', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nivel_remunerativo'

    def __unicode__(self):
        return self.nombre


class RegimenPensionario(models.Model):
    reg_pension = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=60, blank=True)
    abrev = models.CharField(max_length=15, blank=True)
    afpnet = models.CharField(max_length=2, blank=True)
    aporte = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prima = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    comision = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regimen_pensionario'

    def __unicode__(self):
        return self.nombre


class PlanillaTrab(models.Model):
    n_expediente = models.CharField(db_column='N_Expediente', max_length=8)  # Field name made lowercase.
    ano_eje = models.CharField(db_column='Ano_eje', max_length=4)  # Field name made lowercase.
    personal = models.ForeignKey(Personal, db_column='DNI')  # Field name made lowercase.
    reg_pension = models.ForeignKey(RegimenPensionario, db_column='Reg_pension', blank=True)  # Field name made lowercase.
    n_orden = models.IntegerField(db_column='N_Orden', blank=True, null=True)  # Field name made lowercase.
    tipo_trab = models.ForeignKey(TipoTrabajador, db_column='Tipo_Trab', blank=True)  # Field name made lowercase.
    nivel_rem = models.CharField(db_column='Nivel_rem', max_length=2)  # Field name made lowercase.
    cargo_func = models.CharField(max_length=3, blank=True)
    desc_cargo = models.CharField(max_length=100, blank=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    fecha_modi = models.DateTimeField(blank=True, null=True)
    dni_modi = models.CharField(max_length=8, blank=True)
    monto_rem = models.DecimalField(db_column='Monto_rem', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rem_aseg = models.DecimalField(db_column='Rem_aseg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dias_nor = models.IntegerField(db_column='Dias_Nor', blank=True, null=True)  # Field name made lowercase.
    dias_dom = models.IntegerField(db_column='Dias_Dom', blank=True, null=True)  # Field name made lowercase.
    dias_agua = models.IntegerField(db_column='Dias_Agua', blank=True, null=True)  # Field name made lowercase.
    dias_falt = models.IntegerField(db_column='Dias_Falt', blank=True, null=True)  # Field name made lowercase.
    min_tard = models.BigIntegerField(db_column='Min_Tard', blank=True, null=True)  # Field name made lowercase.
    dias_fer = models.IntegerField(db_column='Dias_Fer', blank=True, null=True)  # Field name made lowercase.
    dias_ftrab = models.IntegerField(db_column='Dias_FTrab', blank=True, null=True)  # Field name made lowercase.
    hora_extra = models.IntegerField(blank=True, null=True)
    dias_dm = models.IntegerField(db_column='Dias_DM', blank=True, null=True)  # Field name made lowercase.
    dias_vac = models.IntegerField(db_column='Dias_Vac', blank=True, null=True)  # Field name made lowercase.
    dias_tot = models.IntegerField(db_column='Dias_TOT', blank=True, null=True)  # Field name made lowercase.
    n_hijos = models.IntegerField(db_column='N_Hijos', blank=True, null=True)  # Field name made lowercase.
    n_serie = models.CharField(db_column='N_serie', max_length=3, blank=True)  # Field name made lowercase.
    n_recibo = models.CharField(db_column='N_recibo', max_length=8, blank=True)  # Field name made lowercase.
    total_ingr = models.DecimalField(db_column='Total_Ingr', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_desc = models.DecimalField(db_column='Total_Desc', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_apor = models.DecimalField(db_column='Total_Apor', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    d01 = models.CharField(max_length=1, blank=True)
    d02 = models.CharField(max_length=1, blank=True)
    d03 = models.CharField(max_length=1, blank=True)
    d04 = models.CharField(max_length=1, blank=True)
    d05 = models.CharField(max_length=1, blank=True)
    d06 = models.CharField(max_length=1, blank=True)
    d07 = models.CharField(max_length=1, blank=True)
    d08 = models.CharField(max_length=1, blank=True)
    d09 = models.CharField(max_length=1, blank=True)
    d10 = models.CharField(max_length=1, blank=True)
    d11 = models.CharField(max_length=1, blank=True)
    d12 = models.CharField(max_length=1, blank=True)
    d13 = models.CharField(max_length=1, blank=True)
    d14 = models.CharField(max_length=1, blank=True)
    d15 = models.CharField(max_length=1, blank=True)
    d16 = models.CharField(max_length=1, blank=True)
    d17 = models.CharField(max_length=1, blank=True)
    d18 = models.CharField(max_length=1, blank=True)
    d19 = models.CharField(max_length=1, blank=True)
    d20 = models.CharField(max_length=1, blank=True)
    d21 = models.CharField(max_length=1, blank=True)
    d22 = models.CharField(max_length=1, blank=True)
    d23 = models.CharField(max_length=1, blank=True)
    d24 = models.CharField(max_length=1, blank=True)
    d25 = models.CharField(max_length=1, blank=True)
    d26 = models.CharField(max_length=1, blank=True)
    d27 = models.CharField(max_length=1, blank=True)
    d28 = models.CharField(max_length=1, blank=True)
    d29 = models.CharField(max_length=1, blank=True)
    d30 = models.CharField(max_length=1, blank=True)
    d31 = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'Planilla_Trab'
        verbose_name = "Planilla del trabajador"
        verbose_name_plural = "Planillas del trabajador"

    def get_nivel_remunerativo(self):
        return NivelRemunerativo.objects.get(tipo_trab=self.tipo_trab_id, nivel_rem=self.nivel_rem)

    def get_planilla_detalles(self):
        return PlanillaDetalle.objects.filter(n_expediente=self.n_expediente, ano_eje=self.ano_eje, personal=self.personal)


class Conceptos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=4)
    concepto = models.CharField(max_length=100, blank=True)
    cod_pdt = models.CharField(db_column='cod_PDT', max_length=4)  # Field name made lowercase.
    calculo = models.CharField(max_length=1, blank=True)
    procesar = models.CharField(max_length=1, blank=True)
    selec = models.CharField(max_length=1, blank=True)
    glosa = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'conceptos'

    def __unicode__(self):
        return self.concepto


class PlanillaDetalle(models.Model):
    n_expediente = models.CharField(db_column='N_Expediente', max_length=8)  # Field name made lowercase.
    ano_eje = models.CharField(db_column='Ano_eje', max_length=4)  # Field name made lowercase.
    personal = models.ForeignKey(Personal, db_column='DNI')  # Field name made lowercase.
    concepto = models.ForeignKey(Conceptos, db_column='Codigo')  # Field name made lowercase.
    ind = models.CharField(db_column='Ind', max_length=1, choices=constants.PLANILLA_DETALLE_IND_CHOICES)  # Field name made lowercase.
    valor = models.DecimalField(db_column='Valor', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcen = models.DecimalField(db_column='Porcen', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    debe_gasto = models.CharField(db_column='Debe_Gasto', max_length=8, blank=True)  # Field name made lowercase.
    debe_monto = models.DecimalField(db_column='Debe_Monto', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    haber_gasto = models.CharField(db_column='Haber_Gasto', max_length=8, blank=True)  # Field name made lowercase.
    haber_monto = models.DecimalField(db_column='Haber_Monto', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=6, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Planilla_Detalle'




class Usuario(models.Model):
    ano_eje = models.CharField(max_length=4)
    dni = models.CharField(db_column='DNI', max_length=8)  # Field name made lowercase.
    usuario = models.CharField(max_length=30)
    clave = models.CharField(max_length=20, blank=True)
    id_cargo = models.IntegerField(db_column='ID_cargo', blank=True, null=True)  # Field name made lowercase.
    anio = models.CharField(max_length=4, blank=True)
    obra = models.NullBooleanField()
    act_proy = models.CharField(max_length=7, blank=True)
    sec_func = models.CharField(max_length=4, blank=True)
    estado = models.CharField(max_length=1, blank=True)
    autoriza = models.CharField(max_length=1, blank=True)
    local_host = models.CharField(max_length=50, blank=True)
    local_ip = models.CharField(max_length=15, blank=True)
    fec_hora = models.DateTimeField(blank=True, null=True)
    ventana = models.CharField(max_length=50, blank=True)
    p_config = models.CharField(max_length=1, blank=True)
    p_presu = models.CharField(max_length=1, blank=True)
    p_reque = models.CharField(max_length=1, blank=True)
    p_altad = models.CharField(max_length=1, blank=True)
    p_abast = models.CharField(max_length=1, blank=True)
    p_adqui = models.CharField(max_length=1, blank=True)
    p_almac = models.CharField(max_length=1, blank=True)
    p_perso = models.CharField(max_length=1, blank=True)
    p_paac = models.CharField(max_length=1, blank=True)
    p_conta = models.CharField(max_length=1, blank=True)
    p_patri = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'Usuario'


class Marcacion(models.Model):
    personal = models.ForeignKey(Personal, db_column='DNI', related_name='marcaciones')  # Field name made lowercase.
    fecha_hora = models.DateTimeField()
    tipo_hor = models.CharField(max_length=1, blank=True)
    turno = models.CharField(max_length=1, blank=True)
    registro = models.CharField(max_length=1, blank=True)
    tipo = models.CharField(max_length=1, blank=True)
    observ = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'marcaciones'
        ordering = ('-fecha_hora', )

    def __unicode__(self):
        return self.dni

    def get_tipo(self):
        if self.tipo_hor == '1' and self.turno == '0' and self.registro == '1':
            return 'Ingreso'
        elif self.tipo_hor == '1' and self.turno == '0' and self.registro == '0':
            return 'Refrigerio'
        elif self.tipo_hor == '1' and self.turno == '1' and self.registro == '1':
            return 'Regreso'
        elif self.tipo_hor == '1' and self.turno == '1' and self.registro == '0':
            return 'Salida'
        elif self.tipo_hor == '9' and self.turno == '9' and self.registro == '1':
            return 'Papeleta'
        elif self.tipo_hor == '9' and self.turno == '9' and self.registro == '0':
            return 'Regreso de papeleta'
        else:
            return '----'


class Afectaciones(models.Model):
    tipo_trab = models.CharField(max_length=2)
    codigo = models.CharField(max_length=4)
    iden = models.CharField(max_length=1)
    valor = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    valor_men = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    porcen = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    porcen_mensual = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tabla_monto = models.CharField(max_length=50, blank=True)
    columna_monto = models.CharField(max_length=10, blank=True)
    dn = models.IntegerField(db_column='DN', blank=True, null=True)  # Field name made lowercase.
    dd = models.IntegerField(db_column='DD', blank=True, null=True)  # Field name made lowercase.
    dfer = models.IntegerField(db_column='DFER', blank=True, null=True)  # Field name made lowercase.
    dftrab = models.IntegerField(db_column='DFTRAB', blank=True, null=True)  # Field name made lowercase.
    hora_ext = models.IntegerField(db_column='HORA_EXT', blank=True, null=True)  # Field name made lowercase.
    gasto_debe = models.IntegerField(blank=True, null=True)
    gasto_haber = models.IntegerField(blank=True, null=True)
    cuenta = models.CharField(max_length=4, blank=True)
    rem_aseg = models.CharField(max_length=1, blank=True)
    ex_codigo = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'Afectaciones'




# -*- coding: utf-8 -*- 

from django.contrib import admin
from .models import Personal, Planilla, PlanillaTrab, TipoPlanilla,Orden


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['dni', 'nombres', 'ap_paterno', 'fecha_nac']
    list_filter = ('situacion', )
    list_display = ('dni', 'nombres', 'ap_paterno', 'fecha_nac')


class PlanillaTrabAdmin(admin.ModelAdmin):
    search_fields = ['personal__nombres', 'personal__ap_paterno', 'personal__dni', 'n_expediente']
    list_display = ('n_expediente', 'ano_eje', 'personal', )
    list_filter = ('ano_eje', )

class OrdenTipo(admin.ModelAdmin):
    search_fields = ['ano_eje', 'n_orden', 'tipo', 'num_doc','fecha']
    list_display = ('ano_eje', 'n_orden', 'num_doc' , 'num_doc','fecha')
    list_filter = ('ano_eje', )


admin.site.register(Personal, AuthorAdmin)
admin.site.register(Planilla, admin.ModelAdmin)
admin.site.register(PlanillaTrab, PlanillaTrabAdmin)
admin.site.register(TipoPlanilla, admin.ModelAdmin)
admin.site.register(Orden, OrdenTipo)

# -*- coding: utf-8 -*- 

from django.contrib import admin
from .models import Personal, Planilla, PlanillaTrab, TipoPlanilla


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['dni', 'nombres', 'ap_paterno', 'fecha_nac']
    list_filter = ('situacion', )
    list_display = ('dni', 'nombres', 'ap_paterno', 'fecha_nac')


class PlanillaTrabAdmin(admin.ModelAdmin):
    search_fields = ['personal__nombres', 'personal__ap_paterno', 'personal__dni', 'n_expediente']
    list_display = ('n_expediente', 'ano_eje', 'personal', )
    list_filter = ('ano_eje', )


admin.site.register(Personal, AuthorAdmin)
admin.site.register(Planilla, admin.ModelAdmin)
admin.site.register(PlanillaTrab, PlanillaTrabAdmin)
admin.site.register(TipoPlanilla, admin.ModelAdmin)

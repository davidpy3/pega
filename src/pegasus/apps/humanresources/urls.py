from django.conf.urls import patterns, url
from django.contrib import admin

from .views import (PersonalList, PersonalEdit, PersonalAdd, MarcacionList, PlanillaList,
                    PlanillaDetail, PlanillaAddView, PlanillaTrabDetail, PlanillaModalAddView,OrdenList,RequerimientoList )


admin.autodiscover()

urlpatterns = patterns(
    '',
    # Personal

    url(r'^personal$', PersonalList.as_view(), name='personal_list'),
    url(r'^personal/crear$', PersonalAdd.as_view(), name='personal_add'),
    url(r'^personal/(?P<pk>[0-9]{8})/editar$', PersonalEdit.as_view(), name='personal_edit'),


    # Planillas

    url(r'^(?P<current_year>[0-9]{4})/planillas$', PlanillaList.as_view(), name='planilla_list'),
    url(r'^(?P<current_year>[0-9]{4})/planilla/add$', PlanillaAddView.as_view(), name='planilla_add'),
    url(r'^planilla/modal/add$', PlanillaModalAddView.as_view(), name='planilla_modal_add'),
    url(r'^(?P<current_year>[0-9]{4})/planilla/(?P<pk>[0-9]+)/ver$', PlanillaDetail.as_view(), name='planilla_detail'),
    url(r'^(?P<current_year>[0-9]{4})/planilla_trab/(?P<pk>[0-9]+)/ver$', PlanillaTrabDetail.as_view(), name='planilla_trab_detail'),


    # Marcaciones

    url(r'^(?P<current_year>[0-9]{4})/marcaciones$', MarcacionList.as_view(), name='marcaciones_list'),



    #Ordenes de compra y servicio

    # url(r'^orden$', OrdenList.as_view(), name='orden_list'),
    url(r'^(?P<current_year>[0-9]{4})/orden$', OrdenList.as_view(), name='orden_list'),


    #Requerimiento de bienes y servicios

    # url(r'^orden$', OrdenList.as_view(), name='orden_list'),
    url(r'^(?P<current_year>[0-9]{4})/requerimiento$', RequerimientoList.as_view(), name='requerimiento_list'),




)

# coding=utf-8
from django.views.generic import UpdateView, DetailView, CreateView, TemplateView
from django_genericfilters.views import FilteredListView

from .models import Personal, Marcacion, Planilla, PlanillaTrab,Orden,Requerimiento
from .forms import SearchForm, PlanillaForm, PlanillaPersonalForm
from . import constants


class DashboardView(TemplateView):
    template_name = 'pegasus/dashboard.html'


class RequerimientoList(FilteredListView):
    # Normal ListView options
    model = Requerimiento
    paginate_by = 20
    template_name = 'humanresources/requerimiento_list.html'

    # FilteredListView options
    form_class = SearchForm
    search_fields = ['ano_eje']

class OrdenList(FilteredListView):
    # Normal ListView options
    model = Orden
    paginate_by = 20
    template_name = 'humanresources/orden_list.html'

    # FilteredListView options
    form_class = SearchForm
    search_fields = ['ano_eje']

    
    # def get_queryset(self):
    #     queryset = super(OrdenList, self).get_queryset()
    #     return queryset.prefetch_related('estado', )



class PersonalList(FilteredListView):
    # Normal ListView options
    model = Personal
    paginate_by = 15
    template_name = 'humanresources/personal_list.html'

    # FilteredListView options
    form_class = SearchForm
    search_fields = ['dni', 'nomb_comp', ]

    def get_queryset(self):
        queryset = super(PersonalList, self).get_queryset()
        return queryset.prefetch_related('mod_laboral', )


class PlanillaAddView(FilteredListView):
    model = Personal
    paginate_by = 100
    form_class = PlanillaPersonalForm
    template_name = 'humanresources/planilla_add.html'

    # filter_fields = ['mod_laboral', ]

    def form_valid(self, form):
        """Return the queryset when form has been submitted."""
        queryset = super(PlanillaAddView, self).form_valid(form)

        mod_laboral = form.cleaned_data['mod_laboral']
        queryset = queryset.filter(mod_laboral=mod_laboral)

        entidad = form.cleaned_data['entidad']
        queryset = queryset.filter(entidad=entidad)

        return queryset.filter(situacion=constants.SITUACION_ALTA)

    def form_invalid(self, form):
        return Personal.objects.none()


class PlanillaModalAddView(CreateView):
    form = Planilla
    form_class = PlanillaForm
    template_name = 'humanresources/modals/planilla_add.html'


class MarcacionList(FilteredListView):
    # Normal ListView options
    model = Marcacion
    paginate_by = 15
    template_name = 'humanresources/marcacion_list.html'

    # FilteredListView options
    form_class = SearchForm
    search_fields = ['personal__dni', ]

    def get_queryset(self):
        queryset = super(MarcacionList, self).get_queryset()
        if self.request.current_year:
            queryset = queryset.filter(fecha_hora__year=self.request.current_year)
        return queryset.prefetch_related('personal', )


class PlanillaList(FilteredListView):
    # Normal ListView options
    model = Planilla
    paginate_by = 15
    template_name = 'humanresources/planilla_list.html'

    # FilteredListView options
    form_class = SearchForm
    search_fields = ['n_expediente', ]

    def get_queryset(self):
        queryset = super(PlanillaList, self).get_queryset()
        if self.request.current_year:
            queryset = queryset.filter(ano_eje=self.request.current_year)
        return queryset.prefetch_related('mod_laboral', 'tipo_planilla', 'entidad', )


class PersonalEdit(UpdateView):
    model = Personal
    template_name = 'humanresources/personal_add_edit.html'
    fields = ['dni', 'ap_paterno', 'ap_materno']


class PersonalAdd(CreateView):
    model = Personal
    template_name = 'humanresources/personal_add_edit.html'


class PlanillaDetail(DetailView):
    model = Planilla
    template_name = 'humanresources/planilla_detail.html'


class PlanillaTrabDetail(DetailView):
    model = PlanillaTrab
    template_name = 'humanresources/planilla_trab_detail.html'

#class PlanillaTrabDetailEdit(UpdateView):
    #model = PlanillaTrab
    #template_name = 'planilla_trab_detail.html'

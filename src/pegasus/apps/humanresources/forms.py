from django import forms

from .models import Planilla, ModalidadLaboral, Sectores, Mes, TipoPlanilla, Meta


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres o DNI'}))


class PlanillaForm(forms.ModelForm):
    class Meta:
        model = Planilla
        fields = ['mes', 'tipo_planilla', 'mod_laboral', 'fuente_financ', 'sec_func', 'entidad']


class PlanillaPersonalForm(forms.Form):
    mod_laboral = forms.ModelChoiceField(ModalidadLaboral.objects)
    entidad = forms.ModelChoiceField(Sectores.objects)
    mes = forms.ModelChoiceField(Mes.objects)
    tipo_planilla = forms.ModelChoiceField(TipoPlanilla.objects)
    sec_func = forms.ModelChoiceField(Meta.objects)
    fuente_financ = forms.CharField()

    def __init__(self, ano_eje='2014', *args, **kwargs):
        super(PlanillaPersonalForm, self).__init__(*args, **kwargs)
        self.fields['sec_func'].queryset = Meta.objects.filter(ano_eje=ano_eje)

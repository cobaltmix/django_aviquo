from django import forms
from .models import Subject

class TypeForm(forms.Form):
    extracurricular_type = forms.ChoiceField(
        choices=[('Summer Program', 'Summer Program'),
                 ('Competition', 'Competition'),
                 ('Scholarship', 'Scholarship')],
        widget=forms.RadioSelect()
    )

class SubjectForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)

class YearForm(forms.Form):
    year = forms.ChoiceField(choices=[('9th', '9th grade'), ('10th', '10th grade'), ('11th', '11th grade'), ('12th', '12th grade')])

class CostForm(forms.Form):
    cost = forms.ChoiceField(choices=[('Free', 'Free'), ('Paid', 'Paid')], widget=forms.RadioSelect())

class EffortForm(forms.Form):
    effort = forms.ChoiceField(choices=[('Low', 'Low effort'), ('Medium', 'Medium effort'), ('High', 'High effort'), ('Hypercompetitive', 'Hypercompetitive')], widget=forms.RadioSelect())
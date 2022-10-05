
from django import forms
from main.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course()
        fields = '__all__'

class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups()
        fields = '__all__'


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students()
        fields = '__all__'


class YearForm(forms.ModelForm):
    class Meta:
        model = Year()
        fields = '__all__'

class DavomatForm(forms.ModelForm):
    class Meta:
        model = Davomat()
        fields = '__all__'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog()
        fields = '__all__'



class MoliyaForm(forms.ModelForm):
    class Meta:
        model = Moliya()
        fields = '__all__'

class FantaForm(forms.ModelForm):
    class Meta:
        model = Fanta()
        fields = '__all__'

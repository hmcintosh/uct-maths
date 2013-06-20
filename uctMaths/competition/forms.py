# forms.py
from django import forms
from django.forms import ModelForm
from django.forms import ModelChoiceField
from competition.models import SchoolStudent, School, Invigilator, Venue

#**********************************
#FORM TO ENTER A NEW SCHOOL STUDENT
class StudentForm (ModelForm):
    class Meta:
        model=SchoolStudent

class StudentForm (forms.Form):
        fields = ['firstname', 'surname', 'language', 'school','grade','sex','venue']
        firstname = forms.CharField()
        surname = forms.CharField()
        language = forms.CharField()
        school = forms.ModelChoiceField(required=False, widget = forms.Select(), queryset = School.objects.all())
        grade = forms.IntegerField()
        sex = forms.CharField ()

#*********************************
#FORM TO ENTER A NEW SCHOOL
class SchoolForm (ModelForm):
    class Meta:
        model=School

class SchoolForm (forms.Form):
        fields = ['name', 'language', 'address','phone','fax','contact','email']
        name = forms.CharField()
        language = forms.CharField()
        address = forms.CharField()
        phone = forms.CharField()
        fax = forms.CharField ()   
        contact = forms.CharField()
        email = forms.CharField ()    

#********************************  
#FORM TO ENTER NEW INVIGILATOR
class InvigilatorForm (ModelForm):
    class Meta:
        model=Invigilator

class InvigilatorForm (forms.Form):
        fields = ['school','firstname','surname', 'grade', 'invig_reg','phone_h','phone_w','fax','fax_w','email','responsible']
        school = forms.ModelChoiceField(required=False, widget = forms.Select(), queryset = School.objects.all())
        firstname = forms.CharField()
        surname = forms.CharField()
        grade = forms.IntegerField()
        venue = forms.ModelChoiceField(queryset = Venue.objects.all())
        inv_reg = forms.CharField()
        phone_h = forms.CharField()
        phone_w = forms.CharField ()   
        fax = forms.CharField()
        fax_w= forms.CharField()
        email = forms.CharField ()  
        responsible = forms.CharField()

#*****************************************
#FORM TO ENTER NEW VENUE
class VenueForm(ModelForm):
    class Meta:
        model=Venue

class VenueForm(forms.Form):
        fields = ['code','building','seats','bums','grade','pairs']
        code = forms.IntegerField()
        building = forms.CharField()
        seats = forms.IntegerField ()   
        bums = forms.IntegerField()
        grade = forms.IntegerField ()  
        pairs = forms.IntegerField()

#*****************************************
#TESTING TO FILTER
class testForm(forms.Form):
        building = forms.CharField()
        
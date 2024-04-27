from django.forms import ModelForm
from matrimony_app.models import Contact, Profile, Interest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class contact_form(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class reg_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class profile_form(ModelForm):
    class Meta:
        model = Profile
        fields = ['Phone_Number', 'Age', 'Height', 'Weight', 'Blood_Group',  'Marital_Status', 'Nationality', 'My_Complexion',  'Smoke', 'Time_of_Birth', 'Date_of_Birth', 'City',  'Religion', 'Cast', 'State', 'Education','About',
                  'Occupation', 'Side_Income', 'Annual_Income', 'Father_Name',  'Father_Occupation', 'Mother_Name', 'Mother_Occupation', 'No_of_Brothers', 'No_of_Sisters', 'Complexion', 'Partner_Height', 'Partner_Educationt', 'Partner_Religion',
                  'Partner_Preference','image']

class user_profile_form(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','email']
        
class interest_form(ModelForm):
    class Meta:
        model = Interest
        fields = ['user','interested']
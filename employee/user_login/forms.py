from django import forms
from .models import User



class  UserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ('firstname','lastname','mobile','emp_id','emailaddress','password','confirmpassword')
        labels = {
           'firstname':'First Name',
           'lastname':'Last Name',
           'emp_id':'Employee ID',
           'emailaddress':'Email Address',
           'confirmpassword':'Confirm Password',

        }

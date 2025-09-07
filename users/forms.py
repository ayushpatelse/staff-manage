from django import forms
from .models import CustomUser,Employee

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)
    
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','sec_id','email']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password") 
        password2 = cleaned_data.get("password2") 
        if password!=password2 :
            raise forms.ValidationError("Passwords do match")
        
    def save(self, commit = False):
        instance = super().save(commit=False)
        if 'password' in self.cleaned_data and self.cleaned_data['password']:
            instance.set_password(self.cleaned_data['password'])
            print(instance.password)
            commit = True
        if commit:
            instance.save()
            
        return instance
class LoginForm(forms.Form):
    sec_id = forms.CharField(max_length=10,label="Security ID")
    password = forms.CharField(widget=forms.PasswordInput)


# Editing Forms 

class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email']
        
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email Address',
        }
        
        

class EmployeeEditForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ['phone','address']
        
        labels = {
            'phone': "Phone No.",
            'address' : "Current Address"
        }

       

class ManagerEmployeeEditForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ['role','status','address','phone','department']
        
        labels = {
            'phone': "Phone No.",
            'address' : "Current Address",
            
        }

from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from snitches.models import Profile, Group_Member
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('token',)
        
class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name', max_length=32)
    
class AddMember(forms.Form):
    def __init__(self, *args,**kwargs):
        try:
            group = kwargs.pop('group')
            user = kwargs.pop('user')
            members = Group_Member.objects.filter(belongs=group)
            users = User.objects.all().exclude(id=user.id)
            for member in members:
                users = users.exclude(id=member.user.id)
            
            names = forms.ModelMultipleChoiceField(queryset=users)
            super(AddMember,self).__init__(*args,**kwargs)
            self.fields['name'] = names
        except KeyError:
            super(AddMember,self).__init__(*args,**kwargs)
    
    name = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    permission = forms.CharField(
            max_length=2,
            widget=forms.Select(choices=Group_Member.PERMISSIONS),
        )
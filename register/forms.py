from django import forms
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    first_name = forms.CharField(max_length = 200, required = True)
    last_name = forms.CharField(max_length = 200, required = True)
    email = forms.EmailField(required = True)
    # date_of_birth = forms.DateField(widget=forms.DateInput(attrs = {'type':'date'}))

    # # single choice example, drop down
    # GENDER_CHOICES = (('male', 'Male'),
    #                   ('female','Female'),
    #                   ('transgender','Transgender'),
    #                   ('non-binary','Non-binary'),
    #                   ('prefer not to respond','Prefer not to respond')
    #                   )
    
    # gender = forms.ChoiceField(choices=GENDER_CHOICES )

    # # select choice example
    # COUNTRY_CHOICES = [('US', 'United States'),
    #                 ('CA','Canada'),
    #                 ('MX','Mexico')
    #                 ]
    # city = forms.SelectField(choices = COUNTRY_CHOICES)

    # # multiple choice example
    # SOCIAL_MEDIA_CHOICES = [
    #     ('1', "Whatsapp"),
    #     ('2',"Facebook"),
    #     ('3',"Instagram"),
    #     ('4',"X"),
    #     ('5',"None")
    # ]
    # social_media = forms.MultipleChoiceField(choices = SOCIAL_MEDIA_CHOICES)

    # image field -> profile photo
    profile_photo = forms.ImageField()

    # file field -> resume

    # url field -> linkedin profile

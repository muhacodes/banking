from django.forms import ModelForm
from .models import Transaction


class create_form(ModelForm):
    class Meta:
        model = Transaction
        exclude = ('mode',)
        

    def __init__(self, *args, **kwargs):
        super(create_form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
        })

from django.forms import ModelForm
from .models import Client


class create_form(ModelForm):
    class Meta:
        model = Client
        exclude = ('amount', )

    def __init__(self, *args, **kwargs):
        super(create_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
        })

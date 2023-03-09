from django.forms import ModelForm, DateField, CharField, ModelChoiceField
from django.core.exceptions import ValidationError
from .models import Building, Room, Reservation
from django import forms


def zip_code_validator(value):
    error_message = "Niepoprawny kod pocztowy"
    if len(value) > 6 or len(value) < 5:
        raise ValidationError(error_message)
    if len(value) == 5:
        for c in value:
            if not c.isdigit():
                raise ValidationError(error_message)
    if len(value) == 6:
        for i in range(len(value)):
            if i == 2 and value[i] != "-":
                raise ValidationError(error_message)
            if i != 2 and not value[i].isdigit():
                raise ValidationError(error_message)


class BuildingForm(ModelForm):
    number = CharField(label='Numer')
    street = CharField(label='Ulica')
    town = CharField(label='Miasto')
    zip_code = CharField(label='Kod pocztowy', validators=[zip_code_validator])

    class Meta:
        model = Building
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'
class ReservationForm(ModelForm):
    room = ModelChoiceField(label='Pokój', queryset=Room.objects.all())
    date = DateField(label = 'Data pobytu', widget=DateInput())

    class Meta:
        model = Reservation
        fields = '__all__'
class RoomForm(ModelForm):
    number = CharField(label='Numer')
    area = CharField(label='Powierzchnia w m2')
    building = ModelChoiceField(label='Budynek', queryset=Building.objects.all())

    class Meta:
        model = Reservation
        fields = '__all__'

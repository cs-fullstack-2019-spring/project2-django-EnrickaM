from django import forms
from .models import newuserModel,relativeItemsModel,wikipostModel

YEARS=[x for x in range(1950,2018)]

class newuserForm(forms.ModelForm):
    class Meta:
        model=newuserModel
        fields='__all__'
    widgets={"date_of_birth":forms.SelectDateWidget(years=YEARS,)}


class relativeItemsForm(forms.ModelForm):
    class Meta:
        model=relativeItemsModel
        fields='__all__'


class wikipostForm(forms.ModelForm):
    class Meta:
        model=wikipostModel
        fields='title','text','datecreated','lastupdate'

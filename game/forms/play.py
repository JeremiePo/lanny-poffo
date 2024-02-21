from django import forms

class ClassicQuestion(forms.Form):
    question_subject = forms.CharField(max_length=255)
    question_attribute = forms.CharField(max_length=255)



class IntegerQuestion(forms.Form):
    integer_question_subject = forms.CharField(max_length=255)
    integer_question_attribute = forms.IntegerField()


class CareerDataQuestion(forms.Form):
    #career_data_subject = forms.CharField(max_length=255)
    year = forms.IntegerField(required=False)

    year_between_min = forms.IntegerField(required=False)

    year_between_max = forms.IntegerField(required=False)

    federation = forms.CharField(max_length=255, required=False)
    number_of_matches = forms.IntegerField(required=False)
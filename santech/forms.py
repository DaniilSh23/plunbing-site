from django import forms
from santech.models import Applications, PhotoForWorks, OurWorks


class ApplicationsForms(forms.ModelForm):
    '''Форма для отправки заявки'''

    def __init__(self, *args, **kwargs):
        ''' Переопределяем конструктор класса, чтобы указать атрибуты тегов для стилизации полей формы'''
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control col-3',
            'placeholder': "Как мы можем к Вам обратиться ?",
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control col-2',
            'placeholder': "+7",
        })
        self.fields['text'].widget.attrs.update({
            'class': 'form-control col-4',
            'placeholder': "Чем мы можем Вам помочь ?",
            'cols': "40",
            'rows': "5",
        })
        self.fields['applications_type'].widget.attrs.update({'class': 'form-control col-2 row-2'})

    class Meta:
        model = Applications
        fields = ['name', 'phone_number', 'text', 'applications_type']


class UpdatePriceListForm(forms.Form):
    '''Форма для загрузки файла с целью обновления прайс-листа'''
    file_for_update_price_list = forms.FileField()


class PhotoForWorksForm(forms.ModelForm):
    '''Форма для множественного добавления фото работ'''
    class Meta:
        model = PhotoForWorks
        fields = ['file']
        widgets = {'file': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control-file'})}


class WorkForm(forms.ModelForm):
    ''' Форма для заполнения информации о выполненной работе '''

    def __init__(self, *args, **kwargs):
        ''' Переопределяем конструктор класса, чтобы указать атрибуты тегов для стилизации полей формы'''

        super().__init__(*args, **kwargs)
        self.fields['works_title'].widget.attrs.update({
            'class': 'form-control col-3',
            'placeholder': "Введите название работы"
        })
        self.fields['works_price'].widget.attrs.update({
            'class': 'form-control col-3',
            'placeholder': "Укажите итоговую цену работы"
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control col-4',
            'placeholder': "Опишите порядок выполнения работы.\n"
                           "И несколько полезных правил:\n"
                           "- загрузка хотя бы 1 фото работы обязательна, так как функционал сайта привязан к фотке;\n"
                           "- если нету фотки, то и нех заливать эту работу, "
                           "хотя бы потому, что никому не интересно читать голый текст. ",
            'cols': "40",
            'rows': "5",
        })

    class Meta:
        model = OurWorks
        fields = ['works_title', 'works_price', 'description']

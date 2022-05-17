from _csv import reader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from santech.forms import ApplicationsForms, UpdatePriceListForm, WorkForm, PhotoForWorksForm
from santech.models import Applications, Masters, ImageForMasters, PriceList, OurWorks, PhotoForWorks


class HeadPage(View):
    '''Класс-представление для главной страницы'''

    def get(self, request):
        applications_form = ApplicationsForms()
        update_prices_form = UpdatePriceListForm()
        return render(request, 'santech/index.html', context={
            'applications_form': applications_form,
            'update_prices_form': update_prices_form,
        })

    def post(self, request):
        applications_form = ApplicationsForms(request.POST)
        if applications_form.is_valid():
            name = applications_form.cleaned_data.get('name')
            phone_number = applications_form.cleaned_data.get('phone_number')
            text = applications_form.cleaned_data.get('text')
            applications_type = applications_form.cleaned_data.get('applications_type')
            Applications.objects.create(
                name=name,
                phone_number=phone_number,
                text=text,
                applications_type=applications_type
            )
            return render(request, 'santech/index.html', context={'applications_form': applications_form})
        else:
            return render(request, 'santech/index.html', context={'applications_form': applications_form})


class MastersView(View):
    '''Класс-представление для отображения информации о мастерах'''

    def get(self, request):
        all_masters = Masters.objects.all()
        all_masters_photo = ImageForMasters.objects.all()
        return render(request, 'santech/our_masters.html', context={
            'all_masters': all_masters,
            'all_masters_photo': all_masters_photo
        })


def update_prices(request):
    '''
    Функция-представление для загрузки и обработки
    файла csv с целью обновления прайс-листа
    '''
    if request.method == 'POST':
        upload_file_form = UpdatePriceListForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            # file_for_update_price_list - это название поля в форме, используется как ключ
            file_data = upload_file_form.cleaned_data['file_for_update_price_list']
            price_list_file = file_data.read()
            price_str = price_list_file.decode('windows-1251').split('\n')
            csv_reader = reader(price_str, delimiter=';', quotechar='"')
            for i_line in csv_reader:
                try:
                    i_line_data = {
                        'works_title': i_line[0],
                        'works_price': float(i_line[1]),
                    }
                    print(f'Чистые данные по ключу file {i_line_data}')
                    res = PriceList.objects.update_or_create(works_title=i_line[0], defaults=i_line_data)
                    print(f'Результат {res}')
                except IndexError:
                    continue
            return HttpResponse(
                'Цены успешно обновлены\n'
                '<p><a href="/">Перейти на главную</a></p>'
            )
        else:
            return redirect('/')


class AllPrices(View):
    '''Представление для отображения прайс листа'''

    def get(self, request):
        all_prices = PriceList.objects.all()
        update_prices_form = UpdatePriceListForm()
        return render(request, 'santech/price_list.html', context={
            'all_prices': all_prices,
            'update_prices_form': update_prices_form,
        })


class OurWorksList(View):
    '''Представление для списка выполненных работ'''

    def get(self, request):
        works_list = OurWorks.objects.only('pk', 'works_title', 'works_price').all()
        photo_list = []
        for i_work in works_list:
            i_photo = PhotoForWorks.objects.filter(for_work=i_work.pk).first()
            print(i_photo)
            print(i_photo.file)
            photo_list.append(i_photo)
        info_form_by_work = WorkForm()
        photo_form_by_work = PhotoForWorksForm()
        return render(request, 'santech/our_works_list.html', context={
            'works_list': works_list,
            'info_form_by_work': info_form_by_work,
            'photo_form_by_work': photo_form_by_work,
            'photo_list': photo_list,
        })

    def post(self, request):
        ''' Добавление новой работы с фото в БД '''

        if request.user.is_authenticated:
            info_form_by_work = WorkForm(request.POST)
            photo_form_by_work = PhotoForWorksForm(request.POST, request.FILES)

            if info_form_by_work.is_valid() and photo_form_by_work.is_valid():
                files_list = request.FILES.getlist('file')
                work_instance = info_form_by_work.save()
                for i_file in files_list:
                    file_instance = PhotoForWorks(file=i_file, for_work=work_instance)
                    file_instance.save()
                return HttpResponse(
                    'Новая работа успешно добавлена\n'
                    '<p><a href="/our_works_list/">Перейти к списку работ</a></p>')


class OurWorksDetail(View):
    '''Представление для детальной информации о выполненной работе'''

    def get(self, request, pk):
        work_photo_list = PhotoForWorks.objects.filter(for_work=pk).select_related('for_work')
        work = work_photo_list[0].for_work
        first_photo = work_photo_list[0].file
        other_photo_list = work_photo_list[1:]
        info_form_by_work = WorkForm()
        photo_form_by_work = PhotoForWorksForm()

        return render(request, 'santech/our_works_detail.html', context={
            'first_photo': first_photo,
            'other_photo_list': other_photo_list,
            'work': work,
            'info_form_by_work': info_form_by_work,
            'photo_form_by_work': photo_form_by_work,
        })
















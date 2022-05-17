from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from santech.views import HeadPage, MastersView, update_prices, AllPrices, OurWorksList, OurWorksDetail

urlpatterns = [
    path('', HeadPage.as_view(), name='head_page'),
    path('our_masters/', MastersView.as_view(), name='our_masters'),
    path('update_prices/', update_prices, name='update_prices'),
    path('price_list/', AllPrices.as_view(), name='price_list'),
    path('our_works_list/', OurWorksList.as_view(), name='works_list'),
    path('our_works_detail/<int:pk>', OurWorksDetail.as_view(), name='works_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path

from main.apps import MainConfig
from main.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, MailingCreateView, \
    MailingUpdateView, MailingDeleteView, MailingListView, MailingDetailView, HomeView

app_name = MainConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('client_list', ClientListView.as_view(), name='client_list'),
    path('create_client', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('create_mailing', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing_list', MailingListView.as_view(), name='mailing_list'),
    path('mailing_detail', MailingDetailView.as_view(), name='mailing_detail'),
    path('update_mailing', MailingUpdateView.as_view(), name='update_mailing'),
    path('delete_mailing', MailingDeleteView.as_view(), name='delete_mailing'),
]
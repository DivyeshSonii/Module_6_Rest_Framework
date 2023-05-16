from django.urls import path
from .views import *
urlpatterns = [
    path('get_data/', GetData.as_view() ,name='get_data'),
    path('create_data/', CreateData.as_view() ,name='create_data'),
    path('update_data/', UpdateData.as_view() ,name='update_data'),
    path('delete_data/', DeleteData.as_view() ,name='delete_data'),
]
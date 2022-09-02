from django.urls import path
from .views import BBLogoutView, index
from .views import other_page
from .views import BBLoginView, BBLogoutView
from .views import profile

app_name = 'main'
urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
]

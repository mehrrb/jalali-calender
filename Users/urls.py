
# from django.urls import path
# from .views import BirthdayListView, BirthdayCreateView


# urlpatterns = [
#     path('', BirthdayListView.as_view(), name='home'),
#     path('add/', BirthdayCreateView.as_view(), name='add_birthday'),
# ]

from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import CustomUserViewSet


router = SimpleRouter()
router.register('register', CustomUserViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls




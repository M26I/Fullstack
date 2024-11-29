from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token



router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view(), name='menu_items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
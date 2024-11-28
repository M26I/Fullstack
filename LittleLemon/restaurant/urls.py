from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view(), name='menu_items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
    # Include the router's URLs directly
    path('booking/', include(router.urls)),  # Correctly include the router URLs here
]
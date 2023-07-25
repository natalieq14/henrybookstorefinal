from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('books', views.BookView.as_view(), name='book'),
    path('branches', views.BranchView.as_view(), name='branch'),
    path('inventory/branch/<int:id>', views.BranchInventoryView.as_view(), name='branch_inventory'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
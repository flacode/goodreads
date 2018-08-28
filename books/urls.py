from django.urls import path
from .views import BookView, BookUpdate

urlpatterns = [
    path('', BookView.as_view(), name='add-book'),
    path('<int:id>/', BookUpdate.as_view(), name='update-book'),
]

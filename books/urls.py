from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from .views import BookView, BookUpdate, UserSignUp

urlpatterns = [
    path('', BookView.as_view(), name='add-book'),
    path('<int:id>/', BookUpdate.as_view(), name='update-book'),
    path('signup/', UserSignUp.as_view(), name='add-user'),
    path('auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='GOODREADS', public=False)),
]

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from webapp.views import IndexView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('create/', PhotoCreateView.as_view(), name='create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


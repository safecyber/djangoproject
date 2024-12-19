from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Hoofdpagina (lijst van posts)
    path('post/<int:pk>/', views.post_detail, name='post_inhoud'),  # Detailpagina van een post
    path('post/nieuw/', views.post_nieuw, name='post_nieuw'),  # Pagina voor nieuwe post
]
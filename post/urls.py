from django.urls import path
from .import views
from  .views import (
    
    ProfileView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,  
    RegistroView, 

)

urlpatterns = [
   
    path('', PostListView.as_view(), name='post_lista'),  # Muestra la lista de publicaciones
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_detalles'),  # Muestra el detalle de una publicación
    path('posts/create/', PostCreateView.as_view(), name='post_crear'),  # Muestra el formulario para crear una nueva publicación
    path('posts/<int:id>/edit/', PostUpdateView.as_view(), name='post_editar'),  # Permite editar una publicación
    path('posts/<int:id>/delete/', PostDeleteView.as_view(), name='post_eliminar'),  # Permite eliminar una publicación
    path('accounts/register/', RegistroView.as_view(), name='registro'),  # URL para registro   
    path('accounts/profile/', ProfileView.as_view(), name='profile'),  # Ruta para el perfil
     ]

   

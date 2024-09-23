from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'

    def get(self, request):
        context = {
            'user': request.user,  # Pasar el usuario autenticado al contexto
        }

        return render(request, self.template_name, context)
    
class PostListView(ListView):
    model = Post
    template_name = 'post/post_lista.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detalles.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        """Override to add get_object_or_404."""
        return get_object_or_404(Post, pk=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        """Agrega los comentarios al contexto."""
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()  
        return context

    def post(self, request, *args, **kwargs):
        """Maneja la creación de un comentario."""
        post = self.get_object()
        comment_content = request.POST.get('content')
        if request.user.is_authenticated and comment_content:
            Comment.objects.create(post=post, author=request.user, content=comment_content)
        return redirect('post_detalles', id=post.id)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_crear.html'
    success_url = reverse_lazy('post_lista')

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asignar el autor como el usuario autenticado
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_formulario.html'
    success_url = reverse_lazy('post_lista')

    def get_object(self, queryset=None):
        """Override to add get_object_or_404."""
        obj = get_object_or_404(Post, pk=self.kwargs['id'])
        return obj

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/post_eliminar.html'  # Plantilla para confirmar eliminación
    success_url = reverse_lazy('post_lista')

    def get_object(self, queryset=None):
        """Override to add get_object_or_404."""
        obj = get_object_or_404(Post, pk=self.kwargs['id'])
        return obj

class RegistroView(View):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('post_lista')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente
            return redirect(self.success_url)
        # En caso de error, vuelve a mostrar el formulario con los errores
        return render(request, self.template_name, {'form': form})


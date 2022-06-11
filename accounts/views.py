from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, logout_then_login, PasswordChangeView as AuthPasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from instagram.models import Post
from .forms import SignupForm, ProfileForm
from django.contrib.auth import login as auth_login, get_user_model
from django.contrib.auth.decorators import login_required


def logout(request):
    return logout_then_login(request)
login = LoginView.as_view(template_name="accounts/login_form.html ")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user )
            messages.success(request,"회원가입 환영합니다")
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            
            messages.success(request, "수정완료")
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'accounts/profile_edit_form.html', {
        'form': form,
    })


class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
    success_url = reverse_lazy("password_change")
    template_name = 'accounts/password_change_form.html'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, "암호를 변경했습니다.")
        return super().form_valid(form)

password_change = PasswordChangeView.as_view()






# instagram/views.py
def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    return render(request, 'instagram/user_page.html', {
        'page_user': page_user,
        'post_list': post_list
    })
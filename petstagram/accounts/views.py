from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from petstagram.accounts.forms import SignUpForm, UserProfileForm
from petstagram.accounts.models import UserProfile
from django.views import generic as views


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'pets': user.userprofile.pet_set.all(),
            'form': UserProfileForm(),

        }
        return render(request, 'accounts/user_profile.html', context)

    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')


class SignUpView(views.CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('current user profile')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()

        login(self.request, user)
        return valid


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login.html'

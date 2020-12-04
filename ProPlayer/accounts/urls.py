
from django.urls import path
from . import views
from django.urls.base import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView ,PasswordResetConfirmView, PasswordResetDoneView
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout'),
    path('change-password/', PasswordChangeView.as_view(success_url = reverse_lazy('change-password-done')), name='change-password'),
    path('change-password-done/', PasswordChangeDoneView.as_view()),
    path('update/<int:pk>',  UpdateView.as_view(
                        success_url=reverse_lazy('profile'),
                        model=User,
                        fields=[
                            'first_name',
                            'last_name',
                            'email',
                        ]
                    ), name='update'),
    path('reset/', PasswordResetView.as_view(
            success_url=reverse_lazy('reset-done'),
            from_email='webmaster_do_site@aqui.com.br', #???
            subject_template_name='accounts/password_reset_subject.txt',
            email_template_name='accounts/password_reset_email.html',
         ), name='reset'),
    path('reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='reset-confirm'),
    path('reset-done/', PasswordResetDoneView.as_view(), name='reset-done'),
    path('verify_username/', views.verify_username, name='verify-username'),

]

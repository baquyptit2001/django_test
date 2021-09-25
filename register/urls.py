from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    # path('password_change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
    #      name='password_change_done'),
    #
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
    #      name='password_change'),
    #
    # path('password_reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
    #      name='password_reset_done'),
    #
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
    #      name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

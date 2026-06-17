from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
path('a-propos/', views.about, name='about'),
path('services/', views.services, name='services'),
path('actualites/', views.news, name='news'),
    path(
        'contact/',
        views.contact,
        name='contact'
    ),

path(
    'boutique/',
    views.boutique,
    name='boutique'
),

path(
    'carrieres/',
    views.carrieres,
    name='carrieres'
),

path(
        'zencard/',
        views.zencard,
        name='zencard'
    ),

path(
    'stations/',
    views.stations,
    name='stations'
),
path(
    'bon_plan/',
    views.bon_plan,
    name='bon_plan'
),
path(
    'carrieres/offre/<int:pk>/',
    views.job_detail,
    name='job_detail'
),
path(
    'carrieres/offre/<int:pk>/',
    views.job_detail,
    name='job_detail'
),
path('news/<int:id>/', views.news_detail, name='news_detail'),




path(
        'admin-panel',
        views.dashboard_home,
        name='dashboard_home'
    ),


path(
    'admin-panel/carrieres/offres/',
    views.admin_job_list,
    name='admin_job_list'
),

path(
    'admin-panel/carrieres/offres/ajouter/',
    views.admin_job_create,
    name='admin_job_create'
),

path(
    'admin-panel/carrieres/offres/<int:pk>/modifier/',
    views.admin_job_edit,
    name='admin_job_edit'
),

path(
    'admin-panel/carrieres/offres/<int:pk>/supprimer/',
    views.admin_job_delete,
    name='admin_job_delete'
),
path(
    'admin-panel/carrieres/offres/<int:pk>/modifier/',
    views.admin_job_edit,
    name='admin_job_edit'
),

path(
    'admin-panel/carrieres/offres/<int:pk>/supprimer/',
    views.admin_job_delete,
    name='admin_job_delete'
),
path(
    'admin-panel/carrieres/candidatures/',
    views.admin_candidatures_list,
    name='admin_candidatures_list'
),

path(
    'admin-panel/carrieres/candidatures/<int:pk>/',
    views.admin_candidature_detail,
    name='admin_candidature_detail'
),
path(
    'admin-panel/contact/',
    views.admin_contact_list,
    name='admin_contact_list'
),

path(
    'admin-panel/contact/<int:pk>/',
    views.admin_contact_detail,
    name='admin_contact_detail'
),

    # Liste des demandes ZenCard
    path(
        'admin-panel/zencard/',
        views.admin_zencard_list,
        name='admin_zencard_list'
    ),

    # Détail d'une demande ZenCard
    path(
        'admin-panel/zencard/<int:id>/',
        views.admin_zencard_detail,
        name='admin_zencard_detail'
    ),

    path(
    'admin/login/',
    views.admin_login,
    name='admin_login'
),

path(
    'admin/logout/',
    views.admin_logout,
    name='admin_logout'
),

path('admin-logout/', views.admin_logout, name='admin_logout'),

path('admin-panel/news/', views.admin_news_list, name='admin_news_list'),
path('admin-panel/news/create/', views.admin_news_create, name='admin_news_create'),

path('admin-panel/news/<int:id>/', views.admin_news_detail, name='admin_news_detail'),

path('admin-panel/news/<int:id>/delete/', views.admin_news_delete, name='admin_news_delete'),



]
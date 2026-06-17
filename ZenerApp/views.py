from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
def admin_required(user):
    return user.is_authenticated and user.is_staff

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'clients/index.html')

def about(request):
    return render(request, "clients/about.html")

def services(request):
    return render(request, "clients/services.html")

from .models import Actualite

def news(request):

    actualites = Actualite.objects.filter(actif=True).order_by('-created_at')

    return render(request, 'clients/actualites.html', {
        'actualites': actualites
    })

from django.shortcuts import render, get_object_or_404
from .models import Actualite

def news_detail(request, id):

    actualite = get_object_or_404(Actualite, id=id, actif=True)

    return render(request, 'clients/news_detail.html', {
        'actualite': actualite
    })



from django.contrib import messages
from .models import ContactMessage

def contact(request):

    if request.method == "POST":

        ContactMessage.objects.create(
            nom=request.POST.get('nom'),
            email=request.POST.get('email'),
            telephone=request.POST.get('telephone'),
            sujet=request.POST.get('sujet'),
            message=request.POST.get('message')
        )

        messages.success(
            request,
            "Votre message a été envoyé avec succès."
        )

        return redirect('contact')

    return render(
        request,
        'clients/contact.html'
    )


def boutique(request):
    return render(request, "clients/boutique.html")

from .models import JobOffer

from django.contrib import messages
from django.shortcuts import render, redirect

from .models import JobOffer, JobApplication


def carrieres(request):

    if request.method == "POST":

        JobApplication.objects.create(

            nom=request.POST.get("nom"),
            email=request.POST.get("email"),
            telephone=request.POST.get("telephone"),
            message=request.POST.get("message"),

            cv=request.FILES.get("cv"),

            lettre_motivation=request.FILES.get(
                "lettre_motivation"
            )
        )

        messages.success(
            request,
            "Votre candidature a été envoyée avec succès."
        )

        return redirect("carrieres")

    offres = JobOffer.objects.filter(
        actif=True
    ).order_by("-created_at")

    return render(
        request,
        "clients/carrieres.html",
        {
            "offres": offres
        }
    )

from django.shortcuts import render, get_object_or_404
from .models import JobOffer

def job_detail(request, pk):

    offre = get_object_or_404(
        JobOffer,
        pk=pk,
        actif=True
    )

    return render(
        request,
        'clients/job_detail.html',
        {
            'offre': offre
        }
    )

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import DemandeZenCard


def zencard(request):

    if request.method == "POST":

        DemandeZenCard.objects.create(
            nom=request.POST.get('nom'),
            telephone=request.POST.get('telephone'),
            email=request.POST.get('email'),
            ville=request.POST.get('ville'),
            type_demande=request.POST.get('type'),
            station_retrait=request.POST.get('station'),
            cni=request.FILES.get('cni')
        )

        messages.success(
            request,
            "Votre demande de ZenCard a été envoyée avec succès."
        )

        return redirect('zencard')

    return render(
        request,
        'clients/zencard.html'
    )



def stations(request):
    return render(
        request,
        'clients/stations.html'
    )

def bon_plan(request):
    return render(
        request,
        'clients/bon_plan.html'
    )


from django.shortcuts import render
from django.utils import timezone

from .models import (
    JobOffer,
    JobApplication,
    ContactMessage,
)


@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def dashboard_home(request):

    # ==========================
    # STATISTIQUES
    # ==========================

    offres_count = JobOffer.objects.count()

    candidatures_count = JobApplication.objects.count()

    contacts_count = ContactMessage.objects.count()

    stations_count = 25

    offres_actives = JobOffer.objects.filter(
        actif=True
    ).count()

    offres_total = JobOffer.objects.count()
    candidatures_traitees = JobApplication.objects.filter(
        traitee=True
    ).count()

    candidatures_total = JobApplication.objects.count()

    if candidatures_total > 0:

        pourcentage_candidatures = int(
            (candidatures_traitees / candidatures_total) * 100
        )

    else:

        pourcentage_candidatures = 0

    if offres_total > 0:

        pourcentage_offres = int(
            (offres_actives / offres_total) * 100
        )

    else:

        pourcentage_offres = 0

    # ==========================
    # ACTIVITÉS RÉCENTES
    # ==========================

    dernieres_candidatures = (
        JobApplication.objects
        .select_related('offre')
        .order_by('-created_at')[:5]
    )

    derniers_messages = (
        ContactMessage.objects
        .order_by('-created_at')[:5]
    )

    dernieres_offres = (
        JobOffer.objects
        .order_by('-created_at')[:5]
    )

    # ==========================
    # CONTEXTE
    # ==========================

    context = {

        'today': timezone.now(),

        'offres_count': offres_count,

        'candidatures_count': candidatures_count,

        'contacts_count': contacts_count,

        'stations_count': stations_count,

        'offres_actives': offres_actives,

        'offres_total': offres_total,

        'pourcentage_offres': pourcentage_offres,

        'dernieres_candidatures': dernieres_candidatures,

        'derniers_messages': derniers_messages,

        'dernieres_offres': dernieres_offres,
        'pourcentage_candidatures': pourcentage_candidatures,

    }

    return render(
        request,
        'admin/dashboard/index.html',
        context
    )


@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_job_list(request):

    offres = JobOffer.objects.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'admin/carrieres/offres_list.html',
        {
            'offres': offres
        }
    )

@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_job_create(request):

    if request.method == "POST":

        JobOffer.objects.create(

            titre=request.POST.get('titre'),

            ville=request.POST.get('ville'),

            type_contrat=request.POST.get(
                'type_contrat'
            ),

            departement=request.POST.get(
                'departement'
            ),

            description=request.POST.get(
                'description'
            ),

            missions=request.POST.get(
                'missions'
            ),

            profil=request.POST.get(
                'profil'
            ),
        )

        return redirect(
            'admin_job_list'
        )

    return render(
        request,
        'admin/carrieres/offre_create.html'
    )


from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import JobOffer


@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_job_edit(request, pk):

    offre = get_object_or_404(
        JobOffer,
        pk=pk
    )

    if request.method == "POST":

        offre.titre = request.POST.get(
            'titre'
        )

        offre.ville = request.POST.get(
            'ville'
        )

        offre.type_contrat = request.POST.get(
            'type_contrat'
        )

        offre.departement = request.POST.get(
            'departement'
        )

        offre.description = request.POST.get(
            'description'
        )

        offre.missions = request.POST.get(
            'missions'
        )

        offre.profil = request.POST.get(
            'profil'
        )

        offre.date_limite = request.POST.get(
            'date_limite'
        ) or None

        offre.actif = (
            request.POST.get('actif')
            == 'on'
        )

        offre.save()

        return redirect(
            'admin_job_list'
        )

    return render(
        request,
        'admin/carrieres/offre_edit.html',
        {
            'offre': offre
        }
    )

@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_job_delete(request, pk):

    offre = get_object_or_404(
        JobOffer,
        pk=pk
    )

    offre.delete()

    return redirect(
        'admin_job_list'
    )


from .models import JobApplication

@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_candidatures_list(request):

    candidatures = JobApplication.objects.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'admin/carrieres/candidatures_list.html',
        {
            'candidatures': candidatures
        }
    )

@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_candidature_detail(request, pk):

    candidature = get_object_or_404(
        JobApplication,
        pk=pk
    )

    return render(
        request,
        'admin/carrieres/candidature_detail.html',
        {
            'candidature': candidature
        }
    )



from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from .models import JobOffer, JobApplication


def job_detail(request, pk):

    offre = get_object_or_404(
        JobOffer,
        pk=pk,
        actif=True
    )

    if request.method == "POST":

        # Récupération des données
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        message = request.POST.get('message')

        cv = request.FILES.get('cv')
        lettre = request.FILES.get('lettre_motivation')

        # ⚠️ Vérification minimale (important)
        if not nom or not email or not telephone or not cv:
            messages.error(
                request,
                "Veuillez remplir tous les champs obligatoires."
            )
            return redirect('job_detail', pk=offre.id)

        JobApplication.objects.create(

            offre=offre,
            nom=nom,
            email=email,
            telephone=telephone,
            message=message,
            cv=cv,
            lettre_motivation=lettre
        )

        messages.success(
            request,
            "Votre candidature a été envoyée avec succès."
        )

        return redirect('job_detail', pk=offre.id)

    return render(
        request,
        'clients/job_detail.html',
        {
            'offre': offre
        }
    )


from .models import ContactMessage

@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_contact_list(request):

    contacts = ContactMessage.objects.all()

    return render(
        request,
        'admin/contact/contact_list.html',
        {
            'contacts': contacts
        }
    )



@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_contact_detail(request, pk):

    contact = get_object_or_404(
        ContactMessage,
        pk=pk
    )

    if not contact.lu:
        contact.lu = True
        contact.save()

    return render(
        request,
        'admin/contact/contact_detail.html',
        {
            'contact': contact
        }
    )


@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_zencard_list(request):

    demandes = DemandeZenCard.objects.order_by(
        '-date_creation'
    )

    return render(
        request,
        'admin/zencard/zencard_list.html',
        {
            'demandes': demandes
        }
    )


@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_zencard_detail(request, id):

    demande = get_object_or_404(
        DemandeZenCard,
        id=id
    )

    if request.method == "POST":

        action = request.POST.get("action")

        if action == "valider":
            demande.statut = "validee"

        elif action == "rejeter":
            demande.statut = "rejetee"

        demande.save()

        return redirect(
            'admin_zencard_detail',
            id=demande.id
        )

    return render(
        request,
        'admin/zencard/zencard_detail.html',
        {
            'demande': demande
        }
    )


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def admin_login(request):

    if request.user.is_authenticated:
        return redirect('admin_dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:

            login(request, user)

            return redirect('admin_dashboard')

        messages.error(
            request,
            "Identifiants invalides."
        )

    return render(
        request,
        'admin/login.html'
    )

from django.contrib.auth import logout

def admin_logout(request):

    logout(request)

    return redirect('admin_login')



from .models import Actualite
@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_news_list(request):

    news = Actualite.objects.all().order_by('-created_at')

    return render(request, 'admin/news/news_list.html', {
        'news': news
    })


@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_news_create(request):

    if request.method == "POST":

        Actualite.objects.create(

            titre=request.POST.get('titre'),
            categorie=request.POST.get('categorie'),
            contenu=request.POST.get('contenu'),
            image=request.FILES.get('image')
        )

        return redirect('admin_news_list')

    return render(request, 'admin/news/news_create.html')


from django.shortcuts import get_object_or_404, redirect
from .models import Actualite
@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_news_detail(request, id):

    actualite = get_object_or_404(Actualite, id=id)

    return render(request, 'admin/news/detail.html', {
        'actualite': actualite
    })


@login_required(login_url='admin_login')
@user_passes_test(admin_required, login_url='admin_login')
def admin_news_delete(request, id):

    actualite = get_object_or_404(Actualite, id=id)

    actualite.delete()

    return redirect('admin_news_list')
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, LoginForm
from .models import ContactMessage, Project
from .site_content import FOCUS_AREAS, RESUME_CONTENT, SITE_PROFILE, SKILLS_LIST


def is_portfolio_superuser(user):
    return (
        user.is_authenticated
        and user.is_superuser
        and user.username == settings.PORTFOLIO_SUPERUSER_USERNAME
    )


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    context = {
        "featured_projects": featured_projects,
        "profile": SITE_PROFILE,
    }
    return render(request, "portfolio/home.html", context)


def about(request):
    context = {
        "profile": SITE_PROFILE,
        "focus_areas": FOCUS_AREAS,
    }
    return render(request, "portfolio/about.html", context)


def projects(request):
    query = request.GET.get("q", "").strip()
    selected_category = request.GET.get("category", "").strip()

    all_projects = Project.objects.all()

    if query:
        all_projects = all_projects.filter(
            Q(title__icontains=query)
            | Q(summary__icontains=query)
            | Q(tools_used__icontains=query)
        )

    if selected_category:
        all_projects = all_projects.filter(category=selected_category)

    categories = Project.objects.values_list("category", flat=True).distinct().order_by(
        "category"
    )

    context = {
        "projects": all_projects,
        "categories": categories,
        "selected_category": selected_category,
        "search_query": query,
        "result_count": all_projects.count(),
    }
    return render(request, "portfolio/projects.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {"project": project}
    return render(request, "portfolio/project_detail.html", context)


def skills(request):
    context = {"skills": SKILLS_LIST}
    return render(request, "portfolio/skills.html", context)


def resume(request):
    context = {
        "profile": SITE_PROFILE,
        "resume": RESUME_CONTENT,
        "education_items": RESUME_CONTENT["education_items"],
        "strength_items": RESUME_CONTENT["strength_items"],
        "experience_items": RESUME_CONTENT["experience_items"],
        "interview_points": RESUME_CONTENT["interview_points"],
    }
    return render(request, "portfolio/resume.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
            )
            messages.success(
                request,
                "Your message was submitted successfully.",
            )
            return redirect("contact")
    else:
        form = ContactForm()

    context = {
        "form": form,
        "profile": SITE_PROFILE,
    }
    return render(request, "portfolio/contact.html", context)


def login_view(request):
    if is_portfolio_superuser(request.user):
        return redirect("dashboard")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if is_portfolio_superuser(user):
                login(request, user)
                messages.success(request, "You are now logged in.")
                return redirect("dashboard")

            form.add_error(
                None,
                "Only the portfolio owner superuser account is allowed to log in here.",
            )
    else:
        form = LoginForm()

    context = {"form": form}
    return render(request, "portfolio/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


@login_required
def dashboard(request):
    if not is_portfolio_superuser(request.user):
        return HttpResponseForbidden("Only the portfolio owner can access this page.")

    all_projects = Project.objects.all()
    projects_with_images = all_projects.filter(image__isnull=False).exclude(image="")
    projects_with_any_link = all_projects.filter(
        Q(github_link__gt="") | Q(demo_link__gt="")
    ).count()
    context = {
        "project_count": all_projects.count(),
        "featured_count": all_projects.filter(is_featured=True).count(),
        "message_count": ContactMessage.objects.count(),
        "unread_message_count": ContactMessage.objects.filter(is_read=False).count(),
        "projects_with_images": projects_with_images.count(),
        "projects_missing_images": all_projects.count() - projects_with_images.count(),
        "projects_with_any_link": projects_with_any_link,
        "projects": all_projects[:5],
    }
    return render(request, "portfolio/dashboard.html", context)

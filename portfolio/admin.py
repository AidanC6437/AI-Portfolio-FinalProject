from django.conf import settings
from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import ContactMessage, Project


class PortfolioAdminSite(AdminSite):
    site_header = "Portfolio Project Admin"
    site_title = "Portfolio Admin"
    index_title = "Manage Portfolio Content"

    def has_permission(self, request):
        user = request.user
        return (
            user.is_active
            and user.is_superuser
            and user.username == settings.PORTFOLIO_SUPERUSER_USERNAME
        )


portfolio_admin_site = PortfolioAdminSite(name="portfolio_admin")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("category", "is_featured")
    search_fields = ("title", "summary", "tools_used")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "summary",
                    "description",
                    "category",
                    "tools_used",
                    "key_features",
                    "contribution",
                    "challenges",
                    "lessons_learned",
                )
            },
        ),
        (
            "Screenshots",
            {"fields": ("image", "image_2", "image_3", "image_4", "image_5", "image_6", "image_7")},
        ),
        ("Links and visibility", {"fields": ("github_link", "demo_link", "is_featured")}),
    )


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "submitted_at", "is_read")
    list_filter = ("is_read", "submitted_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "submitted_at")


portfolio_admin_site.register(Project, ProjectAdmin)
portfolio_admin_site.register(ContactMessage, ContactMessageAdmin)

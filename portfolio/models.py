from django.db import models
from django.urls import reverse


class Project(models.Model):
    # Basic information shown on the projects list and detail page.
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)

    # We store tools as plain text to keep the model beginner-friendly.
    tools_used = models.TextField(help_text="Example: Django, Bootstrap, OpenAI API")
    key_features = models.TextField()
    contribution = models.TextField(verbose_name="Your role / contribution")
    challenges = models.TextField(verbose_name="Biggest challenge")
    lessons_learned = models.TextField()

    image = models.ImageField(
        upload_to="project_images/",
        blank=True,
        null=True,
        verbose_name="Screenshot 1",
    )
    image_2 = models.ImageField(
        upload_to="project_images/",
        blank=True,
        null=True,
        verbose_name="Screenshot 2",
    )
    image_3 = models.ImageField(
        upload_to="project_images/",
        blank=True,
        null=True,
        verbose_name="Screenshot 3",
    )
    image_4 = models.ImageField(
        upload_to="project_images/",
        blank=True,
        null=True,
        verbose_name="Screenshot 4",
    )
    image_5 = models.ImageField(
        upload_to="project_images/",
        blank=True,
        null=True,
        verbose_name="Screenshot 5",
    )
    image_6 = models.ImageField(
        upload_to="project_images/",
        blank=True,
        null=True,
        verbose_name="Screenshot 6",
    )
    image_7 = models.ImageField(
        upload_to="project_images/",
        blank=True,
        null=True,
        verbose_name="Screenshot 7",
    )
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", args=[self.slug])

    @property
    def github_link_label(self):
        return f"{self.clean_display_title} GitHub"

    @property
    def demo_link_label(self):
        labels = {
            "chatbot-project": "Chatbot Demo",
            "google-ai-studio-media-project": "Google AI Studio Media Video",
            "campus-skillswap-django-project": "SkillSwap Demo",
            "langchain-agent-project": "LangChain Agent Demo",
            "machine-learning-project-scikit-learn": "Machine Learning Demo",
            "n8n-agent-workflow-project": "n8n Workflow Demo",
            "image-generation-project": "Image Generation Demo",
        }
        return labels.get(self.slug, f"{self.clean_display_title} Demo")

    @property
    def tools_used_list(self):
        return [tool.strip() for tool in self.tools_used.split(",") if tool.strip()]

    @property
    def clean_display_title(self):
        title = self.title
        for phrase in (" Django Project", " Project", " (scikit-learn)"):
            title = title.replace(phrase, "")
        return title


class ContactMessage(models.Model):
    # This stores messages submitted through the portfolio contact form.
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"
